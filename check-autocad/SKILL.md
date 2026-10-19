---
name: check-autocad
description: Vérifie qu’AutoCAD pour Windows est ouvert, qu’un dessin est chargé et que Claude peut y écrire. À utiliser quand on demande si AutoCAD est connecté, visible, ou prêt à dessiner.
---

# Check AutoCAD Connection

Utiliser ce skill quand on demande si AutoCAD est connecté, ouvert, ou si Claude peut dessiner dedans.

Le script est `tools/check_autocad.py`, à côté de ce fichier. Depuis la racine du skill :

```bash
python tools/check_autocad.py
```

Il se termine par le code **0** (succès) ou **1** (échec) et imprime un seul objet JSON.

## Succès — `"status": "ok"`

Si `"text_written": true`, dire que Claude est connecté à **{product}** version {version}, dessin actif **{document}**. Le texte « Hello from Claude. You are connected to AutoCAD. » est placé à l’origine du dessin, hauteur 250. S’il n’est pas visible : `ZOOM` puis `E`.

Si `"text_written": false`, la connexion est établie mais l’écriture a échoué. Montrer `text_warning` et vérifier que le dessin n’est pas verrouillé.

## Échec — lire `"code"`

| Code | Quoi dire |
| --- | --- |
| `NO_PYWIN32` | Installer le pont COM : `pip install pywin32`, puis réessayer. |
| `NOT_RUNNING` | Ouvrir AutoCAD et un fichier .dwg, puis réessayer. |
| `NOT_INSTALLED` | AutoCAD pour Windows est requis. AutoCAD pour Mac n’a pas COM. |
| `NO_DOCUMENT` | Ouvrir ou créer un .dwg dans AutoCAD. |
| `READONLY` | Rouvrir le dessin en écriture. |
| `COM_ERROR` | Redémarrer AutoCAD. Une fois, le lancer en administrateur pour réenregistrer COM. |

Toujours montrer le champ `"fix"` du JSON.

Windows seulement. Le texte de preuve reste dans le dessin ; l’utilisateur peut le supprimer.
