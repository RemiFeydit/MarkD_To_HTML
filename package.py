import argparse
from markdown2 import Markdown
import re

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory", help="The file you want to convert", type = str)
parser.add_argument("-o", "--output-directory", help="The name of HTML file", type = str)
arg = parser.parse_args()

if arg.input_directory.endswith('.md'):
    md = arg.input_directory
else:
    md = arg.input_directory + '.md'

if arg.output_directory.endswith('.html'):
    html = arg.output_directory
else:
    html = arg.output_directory + '.html'


with open(md, 'r+') as f:
    link_patterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]
    link = Markdown(extras=["link-patterns"],link_patterns=link_patterns)
    convert_html = link.convert(f.read())
    Markdown(convert_html)
    f2 = open(html, 'w')
    f2.write("<!DOCTYPE html>\n<html>\n<head>\n\t<meta charset='utf-8' />\n\t<title>"+ "Page Title" +" </title>\n\t<link rel='stylesheet' type='text/css' href='main.css' />\n</head>\n<body>\n")
    f2.write(convert_html)
    f2.write("</body>\n</html>")

print("Votre fichier dans le chemin " + md + " a bien été converti sur le chemin " + html + ".")