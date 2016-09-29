import sys
import os
import random
def parse_folder(folder,duplication =2):
    levels = []
    for file in os.listdir(folder):
        with open(os.path.join(folder,file),'rb') as infile:
            level = [list(line.rstrip()) for line in infile]
            levels.append(level)
    duplication = 2
    for ii in range(duplication):
        levels = levels + levels
    random.shuffle(levels)

    outstr = ''
    for level in levels:
        width = len(level[0])
        height = len(level)
        outstr += '\n'
        for column in range(width):
            outstr += '('
            for row in range(height):
                outstr += level[row][column]
    return outstr




