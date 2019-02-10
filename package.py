from argparse import ArgumentParser
from markdown2 import Markdown
from re import compile
from os import listdir

parser = ArgumentParser()
parser.add_argument("-i", "--input-directory", help="The folder you want to convert", type = str)
parser.add_argument("-o", "--output-directory", help="The name of HTML folder", type = str)
parser.add_argument("-t", "--template-directory", help="The name of your template file", type = str)
arg = parser.parse_args()


def convert():
    for md_file in listdir(arg.input_directory):
        with open(arg.input_directory + '/' + md_file, 'r+') as fileToConvert:
            template = open('template/' + arg.template_directory , 'r+')
            adjustedFile = fileToConvert.read()
            adjustedFile = adjustedFile.replace('  ##', '##')
            htmlFile = open(arg.output_directory + '/' + md_file.replace('.md', '.html'), 'w')
            linkPatterns=[(compile(r'((([A-Za-z]{3,9}:(?:\/\/)?)(?:[\-;:&=\+\$,\w]+@)?[A-Za-z0-9\.\-]+(:[0-9]+)?|(?:www\.|[\-;:&=\+\$,\w]+@)[A-Za-z0-9\.\-]+)((?:\/[\+~%\/\.\w\-_]*)?\??(?:[\-\+=&;%@\.\w_]*)#?(?:[\.\!\/\\\w]*))?)'),r'\1')]
            link = Markdown(extras=["link-patterns", "cuddled-lists", "target-blank-links", "xml"],link_patterns=linkPatterns)
            convertHTML = link.convert(adjustedFile)
            templates = template.read()
            templates = templates.replace('replace', convertHTML)
            templates = templates.replace('Page_Title', md_file.replace('.md', ''))
            htmlFile.write(templates)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nVotre conversion est terminée\n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


if arg.input_directory == None or arg.output_directory == None or arg.template_directory == None:
    print("Veuillez rentrer les options requises ou utiliser --help")
else:
    convert()