#!/usr/bin/python
#title			:GeonamesPreprocessor.py
#description		:The program extracts the location names, converts them to lowercase and removes the duplicates from the US Names file.
#author			:Natasha A Thomas
#date			:20140905
#usage			:python GeonamesPreprocessor.py <input-file>
#notes			:
#python_version		:2.7.6
#=============================================================================

import os
import sys

infile = open(str((sys.argv)[1]), "r")
outfile = open("Geonames2.txt", "w")
for line in infile:
    outfile.write((line.split('	')[2] + '\n').lower()) #extracts the asciiname column of the file and writes it to a new file
infile.close()
outfile.close()

seenLines = set() 
outfile = open("PreprocessedGeonames.txt", "w") 

#removing duplicate entries
for line in open("Geonames2.txt", "r"):
    if line not in seenLines: 
        outfile.write(line)
        seenLines.add(line)

os.remove("Geonames2.txt")
outfile.close()
