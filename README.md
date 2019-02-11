# Markdown to HTML

## Présentation du projet

Le programme a pour but de de convertir un dossier contenant des fichiers markdown (avec l'extension `.md`) en fichiers HTML (avec l'extension `.html`) grâce à un programme en Python.

Pour cela j'ai utilisé un package pour faciliter le programme (markdown2).

### Avant de convertir

Avant de pouvoir convertir vos fichiers markdown vous devez d'abord télécharger le package `markdown2`.

Pour cela rentrer dans votre Powershell:
```bash
pip install -r requirements.txt
```
----
### Commande et arguments

Pour utiliser le convertisseur, mettez vos fichiers à convertir dans le fichier `markdown_file`, puis dans votre PowerShell exécutez le programme `markdownToHTML.py`.
Pour connaître les arguments nécessaires pour convertir tapez:
```bash
python markdownToHTML.py -h
```
OU
```bash
python markdown.py --help
```

On appelle ensuite le programme avec `markdownToHTML.py`.

Voici les arguments que l'on peut passer dans notre commande:

Argument version courte | Argument version longue | Explications
------------ | ------------- |-----------
-h | --help | Affiche tous les arguments possibles et vous explique comment les utiliser
-i | --input-directory | Dossier contenant les fichiers Markdown
-o | --output-directory | Dossier destination pour les fichiers HTML
-t | --template-directory | Fichier template pour votre HTML converti

### Les différents types de templates

`template1.html`:
* Texte converti en rouge et avec la police 'Courier New'
* Titre en h1 en vert pomme et titre aligné

`template2.html`:
* Lien en violet et les liens ne sont pas souligné
* Fond en bleu ciel
* Aligne les listes au centre

`template3.html`:
* Texte converti en blanc et fond en noir
* Lien en blanc et les liens ne sont pas soulignés

`template4.html`:
* Titre h1 en rouge
* Titre h2 en vert
* Titre h3 en bleu
* Lien en violet et les liens ne sont pas soulignés
* Paragraphe en jaune
* Fond en rose saumon