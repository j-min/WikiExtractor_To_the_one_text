import glob
import re
import sys
"""
Input: directory address that contains output files from WikiExtractor.py

Output: name of output file


Usage: python To_the_one_text.py input output
ex) python To_the_one_text.py kowiki_output kowiki_one_file
"""

directory_name = sys.argv[1]
output_name = sys.argv[2]

input_file_list = glob.iglob(directory_name + '/**/wiki_*', recursive=True)

def remove_tags(input_line):
    """
    Remove tags and title of the wiki contents
    """
    if '</doc>' in input_line:
        return ''
    if '<doc' in input_line:
        title = re.search('title="(.*)"', input_line).groups()[0]
        return '', title
    else:
        return input_line


f = open(output_name, 'a')

for input_file in input_file_list:
    with open(input_file, 'r') as temp_input_file:
        title = ''
        for line in temp_input_file:

            #remove multilple whitespace
            line = " ".join(line.split())

            #remove html tag
            try:
                line, title = remove_tags(line)
            except:
                line = remove_tags(line)

            #remove new_line_character
            line = line.rstrip('\n')

            if line == title or line == '\n' or line == '':
                pass
            else:
                f.write(line + ' ')

f.close()