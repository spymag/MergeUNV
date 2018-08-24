#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:25:02 2018

@author: spymag
"""

import glob
import os

if os.path.exists("CombinedUNV.UNV"):
    os.remove("CombinedUNV.UNV")
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
def get_body(fname):
    s=""
    lines = []
    linesclean=[]
    with open(fname) as f:
        for line in f:
            lines.append(line.rstrip()+ "\n")
    #cleanup the body from header and -1 
    for i in range(15,len(lines)-1):       
        linesclean.append(lines[i])
             #write into string
    for i in range(0,len(linesclean)):
        s=s+linesclean[i]            
    return s


#get the header of the first file
def get_header(fname):
    s=""
    headerFlag="  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00"
    with open(fname) as f:
        for line in f:
            s=s+line
            if line.find(headerFlag)!=-1:
                break
    s=s+"  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00  0.00000E+00"+"\n"
   # s=s+"\n"              
    return s


bodies=""
for fname in filenames:
    bodies=bodies+(get_body(fname))

header=get_header(filenames[0])
    
footer="    -1"
        


with open("CombinedUNV.UNV", 'w') as outfile:
    outfile.write(header)
    outfile.write(bodies)
    outfile.write(footer)
                