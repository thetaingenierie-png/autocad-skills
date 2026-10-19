"""
AutoCAD Connection Check
Tests whether a running AutoCAD instance is accessible via COM.

Usage:
    python check_autocad.py

Outputs a JSON result to stdout:
    {"status": "ok",    "version": "...", "document": "..."}
    {"status": "error", "code": "...",   "message": "...", "fix": "..."}
"""

import sys
import json


def check() -> dict:
    # ── 1. Check pywin32 is installed ──────────────────────────────────────
    try:
        import win32com.client
        import pywintypes
    except ImportError:
        return {
            "status": "error",
            "code": "NO_PYWIN32",
            "message": "pywin32 is not installed.",
            "fix": "Run:  pip install pywin32"
        }

    # ── 2. Try to attach to a running AutoCAD instance ────────────────────
    try:
        acad = win32com.client.GetActiveObject("AutoCAD.Application")
    except pywintypes.com_error:
        # No running instance — try to give a useful distinction
        import winreg
        autocad_installed = False
        try:
            winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE,
                           r"SOFTWARE\Autodesk\AutoCAD")
            autocad_installed = True
        except FileNotFoundError:
            pass

        if autocad_installed:
            return {
                "status": "error",
                "code": "NOT_RUNNING",
                "message": "AutoCAD is installed but not running.",
                "fix": "Open AutoCAD and make sure a drawing (.dwg) is open, then try again."
            }
        else:
            return {
                "status": "error",
                "code": "NOT_INSTALLED",
                "message": "AutoCAD does not appear to be installed on this computer.",
                "fix": (
                    "Install a COM-capable version of AutoCAD (full AutoCAD or "
                    "AutoCAD LT for Windows). AutoCAD for Mac does not support COM."
                )
            }
    except Exception as e:
        return {
            "status": "error",
            "code": "COM_ERROR",
            "message": f"COM error when connecting: {e}",
            "fix": (
                "Try: (1) restart AutoCAD, (2) run AutoCAD as Administrator once "
                "to re-register COM, (3) repair the AutoCAD installation."
            )
        }

    # ── 3. Check a drawing is open ────────────────────────────────────────
    try:
        doc = acad.ActiveDocument
        if doc is None:
            raise AttributeError("ActiveDocument is None")
        doc_name = doc.Name
    except Exception:
        return {
            "status": "error",
            "code": "NO_DOCUMENT",
            "message": "AutoCAD is running but no drawing is open.",
            "fix": "Open or create a .dwg file in AutoCAD, then try again."
        }

    # ── 4. Quick write test — draw then delete a point ────────────────────
    try:
        import win32com.client as wc
        import pythoncom
        space = doc.ModelSpace
        pt = wc.VARIANT(
            pythoncom.VT_ARRAY | pythoncom.VT_R8,
            [0.0, 0.0, 0.0]
        )
        test_obj = space.AddPoint(pt)
        test_obj.Delete()
    except Exception as e:
        return {
            "status": "error",
            "code": "READONLY",
            "message": f"AutoCAD is connected but the drawing is read-only or locked: {e}",
            "fix": (
                "Make sure the drawing is not opened read-only, not checked out "
                "by another user, and not in a non-editable state (e.g. Print Preview)."
            )
        }

    # ── 5. Write hello text ───────────────────────────────────────────────
    try:
        import pythoncom
        space = doc.ModelSpace
        insert_pt = win32com.client.VARIANT(
            pythoncom.VT_ARRAY | pythoncom.VT_R8,
            [0.0, 0.0, 0.0]
        )
        txt = space.AddText(
            "Hello from Claude. You are connected to AutoCAD.",
            insert_pt,
            250.0          # height in drawing units (250mm — visible at any zoom)
        )
        txt.Layer = "0"
        doc.Regen(1)       # regen All — makes text appear immediately
        text_written = True
    except Exception as e:
        text_written = False
        text_error = str(e)

    # ── 6. Collect version info ───────────────────────────────────────────
    try:
        version = acad.Version
        product = acad.Caption
    except Exception:
        version = "unknown"
        product = "AutoCAD"

    result = {
        "status": "ok",
        "version": version,
        "product": product,
        "document": doc_name,
        "text_written": text_written
    }
    if not text_written:
        result["text_warning"] = f"Connected but could not write text: {text_error}"

    return result


if __name__ == "__main__":
    result = check()
    print(json.dumps(result, indent=2))
    sys.exit(0 if result["status"] == "ok" else 1)
