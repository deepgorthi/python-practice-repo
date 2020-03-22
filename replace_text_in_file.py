#!/usr/bin/python

import os

with open(os.path.abspath('./test'), "rt") as fin:
    with open("out", "wt") as fout:
        for line in fin:
            fout.write(line.replace('ac', 'aac'))


