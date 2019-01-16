def doLine(line):
    if (line.lstrip('\t\n\r').startswith('#')):
        if (line.lstrip('\t\n\r').startswith('###')):
            line = line.replace('###', '<h3>')
            line = line.rstrip('\t\n\r')
            line = line + ' </h3>\n'
        elif (line.lstrip('\t\n\r').startswith('##')):
            line = line.replace('##', '<h2>')
            line = line.rstrip('\t\n\r')
            line = line + ' </h2>\n'
        else:
            line = line.replace('#', '<h1>')
            line = line.rstrip('\t\n\r')
            line = line + ' </h1>\n'
    return line


with open('text.txt', 'r+') as f:
    f2=open("text1.txt", 'w')
    for line in f:
        f2.write(doLine(line))