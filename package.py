import argparse
from markdown2 import Markdown
import re
from random import choice
import os

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--input-directory", help="The file you want to convert", type = str)
parser.add_argument("-o", "--output-directory", help="The name of HTML file", type = str)
parser.add_argument("-k", "--kikoo-lol", help = "Add randomly 'kikoo', 'lol', 'mdr' or 'ptdr' in your convert file", action = "store_true")
arg = parser.parse_args()


def convert():
    for md_file in os.listdir(arg.input_directory):
        with open(arg.input_directory + '/' + md_file, 'r+') as fileToConvert:
            ajustedFile = fileToConvert.read()
            ajustedFile = ajustedFile.replace('  ##', '##')
            print(ajustedFile)
            htmlFile = open(arg.output_directory + '/' + md_file.replace('.md', '.html'), 'w')
            linkPatterns=[(re.compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]
            link = Markdown(extras=["link-patterns", "cuddled-lists", "target-blank-links", "xml"],link_patterns=linkPatterns)
            convertHTML = link.convert(ajustedFile)
            Markdown(convertHTML)
            htmlFile.write(convertHTML)
    print("ouais super c'est fini")

if arg.input_directory == None or arg.output_directory == None :
    print("Veuillez rentrer les options requises ou utiliser --help")
else:
    convert()