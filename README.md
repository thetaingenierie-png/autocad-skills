# Skills AutoCAD

Skills installés sur ce dépôt. Chacun reste sous sa licence MIT d’origine.

| Dossier | Rôle | Source |
| --- | --- | --- |
| [check-autocad](check-autocad) | Vérifie qu’AutoCAD est ouvert et accessible | pack Design & Draft |
| [autocad-drawing](autocad-drawing) | Dessine dans AutoCAD ouvert, via COM, puis relit la géométrie | [MiaTxxx/autocad-skill-marketplace](https://github.com/MiaTxxx/autocad-skill-marketplace) |
| [cad-edit](cad-edit) | Lit, modifie et trace des DWG sans fenêtre AutoCAD | [xy425yi/claude-cad-skill](https://github.com/xy425yi/claude-cad-skill) |
| [mechanical-drafting-gbt](mechanical-drafting-gbt) | Plans mécaniques, assemblages, contrôle DRC et sortie | [beiming183-cloud/AutoCAD-skills](https://github.com/beiming183-cloud/AutoCAD-skills) |

Le dépôt est [thetaingenierie-png/autocad-skills](https://github.com/thetaingenierie-png/autocad-skills).

## Claude

Compte Claude : `thetaingenierie@gmail.com`. Le catalogue est [`.claude-plugin/marketplace.json`](.claude-plugin/marketplace.json). Il charge les quatre skills de ce dépôt et les connecteurs de [thetaingenierie-png/architecture](https://github.com/thetaingenierie-png/architecture).

```text
/plugin install autocad-drawing --marketplace thetaingenierie-png/autocad-skills
/plugin install cad-edit --marketplace thetaingenierie-png/autocad-skills
/plugin install mechanical-drafting-gbt --marketplace thetaingenierie-png/autocad-skills
/plugin install check-autocad --marketplace thetaingenierie-png/autocad-skills
/plugin install theta-architecture --marketplace thetaingenierie-png/autocad-skills
```
