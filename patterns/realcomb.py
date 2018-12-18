#it just actually combines files by appending the lines of one to another

import sys, os

if len(sys.argv) < 2:
    print("usage python blabal.py file1 ....")
    sys.exit()



files = []
for i,x in enumerate(sys.argv):
    if i > 0:
        files.append(x)


lines = []
title = ""

for f in files:
    title = title+f 

    with open(f, "r") as infile:
       lines.extend(infile.readlines())


for i,l in enumerate(lines):
    if " " in l:
        temp = l
        lines.pop(i)
        temp.split(" ")
        lines.extend(temp) 

with open(title, "w") as outfile:
    outfile.writelines(lines)




 
