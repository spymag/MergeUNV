#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:25:02 2018

@author: spymag
"""

import glob
import os

if os.path.exists("CombinedUNV"):
    os.remove("CombinedUNV")
else:
    print("The file does not exist")
  
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

filenames = glob.glob("*.unv")
s = "File lines are {} for file {}".format(repr(file_len(filenames[0])),repr(filenames[0]))
print(s)

#get the body of the files



#get the header of the first file
def get_header(fname):
    s=""
    headerFlag="Body"
    with open(fname) as f:
        for line in f:
            s=s+line
            if line.find(headerFlag)!=-1:
                break              
    return s


print(get_header(filenames[0]))

with open("CombinedUNV", 'w') as outfile:
    for fname in filenames:
        with open(fname) as infile:
            for line in infile:
                if line.find('UNV1')!=-1:
                    outfile.write(line) 
            outfile.write("\n")
                