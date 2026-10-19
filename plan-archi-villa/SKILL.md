---
name: plan-archi-villa
description: Établit le plan architectural d’une villa ou d’une maison individuelle. À utiliser pour un plan de niveau, un RDC, un étage, une coupe, une façade, un plan de situation simplifié, un tableau de surfaces ou une mise au net AutoCAD/DXF. Ne pas l’utiliser pour le ferraillage, le métré structurel IFC, ni un plan mécanique.
---

# Plan architectural de villa

Produire un plan lisible, coté et mesuré. Le texte du programme ne remplace pas le dessin. Les surfaces annoncées sont celles relues sur le dessin.

## 1. Quand s’arrêter pour demander

Demander uniquement ce qui empêche de tracer :

- gabarit du terrain ou du bâtiment, ou un plan déjà fourni ;
- nombre de niveaux ;
- liste des pièces attendues ;
- une cote manquante ou contradictoire (deux largeurs pour la même pièce, une baie plus large que le mur).

Si le nord, l’étage, ou une préférence de façade n’est pas donné, choisir et l’écrire dans les hypothèses. Ne pas inventer une dimension de pièce que l’utilisateur a laissée vide.

## 2. Hypothèses, si rien n’est précisé

Les noter sur le plan, préfixe `HYP.`

| Élément | Valeur |
| --- | --- |
| Unité du modèle | mètre |
| Cotes | mètres, deux décimales |
| Échelle des plans et façades | 1:100 |
| Échelle de la coupe | 1:100, ou 1:50 si le niveau est petit |
| Mur extérieur | 0,20 m |
| Refend | 0,15 m |
| Cloison | 0,07 m |
| Hauteur sous plafond, RDC | 2,70 m |
| Hauteur sous plafond, étage | 2,50 m |
| Porte intérieure | 0,90 × 2,10 m |
| Porte d’entrée | 0,90 × 2,20 m |
| Allège des fenêtres de séjour | 0,00 m si baie, sinon 0,90 m |
| Allège des autres fenêtres | 0,90 m |

Ces épaisseurs sont architecturales. Elles ne valent pas un dimensionnement béton.

## 3. Ordre

1. Tableau de programme : pièce, niveau, surface demandée, surface retenue.
2. Emprise et sens du nord. L’entrée et le séjour se placent avant les chambres.
3. Murs extérieurs, puis refends, puis cloisons. Les pièces d’eau sont groupées.
4. Portes et fenêtres. Une porte ne coupe pas un mur porteur sans linteau indiqué en note.
5. Noms, surfaces et cotes de chaque pièce. Cotes extérieures du bâtiment, puis cotes intérieures des pièces principales.
6. Coupe sur le séjour et l’escalier dès qu’il y a plus d’un niveau, ou dès qu’une hauteur est demandée.
7. Façades seulement si elles sont demandées. Quatre façades si la demande dit « toutes les façades ».
8. Cartouche : `Theta Ingénierie`, nom du projet, niveau, échelle, date, liste des `HYP.`

Pièces usuelles d’une villa, à ne dessiner que si elles sont au programme ou manifestement nécessaires pour relier les pièces demandées : séjour, cuisine, chambre, salle d’eau, WC, dégagement, garage, terrasse. Un dégagement de 1,10 m minimum relie les chambres aux pièces d’eau. Ne pas ajouter de piscine, d’annexe ou d’étage non demandé.

## 4. Calques

| Calque | Contenu |
| --- | --- |
| `A-MUR-EXT` | murs extérieurs |
| `A-MUR-INT` | refends |
| `A-CLOISON` | cloisons |
| `A-OUV-PORTE` | portes, sens d’ouverture |
| `A-OUV-FEN` | fenêtres et baies |
| `A-ESCALIER` | escalier, sens de montée |
| `A-COTE` | cotations |
| `A-TEXTE` | noms de pièces et surfaces |
| `A-HACH` | hachures de murs |
| `A-AXE` | axes et nord |
| `A-CART` | cartouche et hypothèses |

Couleur et épaisseur suivent le fichier déjà ouvert. Sur un fichier neuf : murs extérieurs plus forts que les cloisons, cotes et textes plus fins.

## 5. Dessiner

- AutoCAD pour Windows ouvert, avec un dessin chargé : passer par le skill `autocad-drawing`. Vérifier la connexion avec `check-autocad` si l’écriture échoue.
- Dessin existant à modifier sans fenêtre AutoCAD : passer par `cad-edit`. Ne pas écraser le DWG sans le dire.
- Ni AutoCAD ni DWG de départ : produire le plan en DXF, calques ci-dessus, unité mètre, et donner le chemin du fichier.

Ne pas vider un modèle déjà rempli. Dessiner à côté, ou sur un nouveau fichier `villa-<nom>-archi.dxf`.

Après le tracé, relire chaque surface fermée et la comparer au tableau. Un écart supérieur à 0,05 m² se corrige ou s’explique. Les surfaces livrées sont les surfaces lues, pas les surfaces espérées.

## 6. Ce que le skill ne fait pas

- Il ne signe pas une conformité PLU, code de la construction ou performance énergétique.
- Il ne dimensionne pas les semelles, poutres, voiles ni le ferraillage.
- Il ne fait pas le métré béton ou acier d’un IFC : cela reste le connecteur `ifc`.
- Il ne présente pas une vue 3D inventée si aucun modèle Rhino, Blender, SketchUp ou Revit n’est ouvert.

## 7. Compte-rendu

Livrer, dans cet ordre :

1. le tableau pièce / niveau / surface lue ;
2. les hypothèses réellement utilisées ;
3. la liste des feuilles (niveaux, coupe, façades) ;
4. le chemin du DWG ou du DXF ;
5. ce qui reste à confirmer par l’utilisateur.
