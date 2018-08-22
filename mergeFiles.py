#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 22:07:08 2018

@author: spymag
"""

import glob
import os

if os.path.exists("CombinedUNV"):
  os.remove("CombinedUNV")
else:
  print("The file does not exist")

readFiles = glob.glob("*.unv")

with open("CombinedUNV","wb") as outfile:
    for f in readFiles:
        with open(f,"rb") as infile:
            outfile.write(infile.read())
     
        
        