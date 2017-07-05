#!/usr/bin/env python3

import os
import sys
import string
import subprocess

file = open("documentation.md", 'r', encoding='utf8')


file_pirit2f = open("documentation_pirit2f.md", 'w', encoding='utf8')

file_fm16 = open("documentation_fm16.md", 'w', encoding='utf8')

lines = []
with open("documentation.md", 'r', encoding="utf8") as file:
    pirit2fOnly = False
    fm16Only = False
    for line in file:
        if line.find("<<<<<< Pirit2f start >>>>>>") != -1:
            pirit2fOnly = True
            fm16Only = False
            continue

        if line.find("<<<<<< Pirit2F end >>>>>>") != -1:
            pirit2fOnly = False
            continue

        if line.find("<<<<<< FM16 start >>>>>>") != -1:
            fm16Only = True
            pirit2fOnly = False
            continue

        if line.find("<<<<<< FM16 end >>>>>>") != -1:
            fm16Only = False
            continue

        if fm16Only == False:
            file_pirit2f.write(line)
        if pirit2fOnly == False:
            file_fm16.write(line)

file_pirit2f.close()
file_fm16.close()

proc = subprocess.Popen("python backdoc.py -t FM16 -s documentation_fm16.md > output/documentation_fm16.html", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()

proc = subprocess.Popen("python backdoc.py -t Pirit2F -s documentation_pirit2f.md > output/documentation_pirit2f.html", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()

proc = subprocess.Popen("python backdoc.py -t ProtocolDescription -s protocol_description.md > output/protocol_description.html", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()

proc = subprocess.Popen("rm documentation_pirit2f.md", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()

proc = subprocess.Popen("rm documentation_fm16.md", shell=True, stdout=subprocess.PIPE)
out = proc.stdout.readlines()

print("Done")