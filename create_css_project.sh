#!/bin/bash

# Créer le répertoire principal
mkdir -p CSS_advanced/styles
mkdir -p CSS_advanced/images

# Créer les fichiers d'images
touch CSS_advanced/images/pic-about-01.jpg
touch CSS_advanced/images/pic-work-01.jpg
touch CSS_advanced/images/pic-work-02.jpg
touch CSS_advanced/images/pic-work-03.jpg
touch CSS_advanced/images/pic-article-01.jpg
touch CSS_advanced/images/pic-article-02.jpg
touch CSS_advanced/images/pic-article-03.jpg
touch CSS_advanced/images/pic-person-01.jpg
touch CSS_advanced/images/pic-person-02.jpg
touch CSS_advanced/images/pic-person-03.jpg

# Créer les fichiers de style
for i in {1..32}
do
    touch CSS_advanced/styles/${i}-style.css
done

# Créer le fichier README.md avec son contenu
cat << EOF > CSS_advanced/README.md
# Advanced CSS

Ce projet couvre les concepts avancés de CSS, incluant :

- Sélecteurs, propriétés et valeurs
- Les différences entre block et inline styling
- Comment s'assurer que la cohérence entre les navigateurs grâce à la normalisation CSS
- Comment mettre en place un CSS debug
- Comment utiliser les pseudo-classes et pseudo-éléments
- Comment utiliser un grid system avec des floats ou flex
- La différence entre icônes de police et image SVG
- La différence entre pseudo-classes et pseudo-éléments
- Comment créer un effet de transition sur un élément
- Comment animer des éléments dans CSS
- Comment transformer (2d, 3d) éléments
- Les principes du design responsive

## Fichiers

- \`styles/[1-24]-style.css\`: Fichiers de style pour chaque exercice
- \`images/\`: Dossier contenant les images utilisées dans le projet

## Auteur

[Votre nom]

## Licence

Ce projet est sous licence MIT.
EOF

echo "Structure de fichiers créée avec succès!"