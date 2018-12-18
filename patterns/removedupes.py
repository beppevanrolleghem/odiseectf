import sys, os

if len(sys.argv) < 2:
    print("usage python removedupes.py FILE")
    sys.exit()
lines = []
f = sys.argv[1]
with open(f, 'r') as infile:
   lines = infile.readlines()



outlines = []
for l in lines:
    if l not in outlines:
        outlines.append(l) 


with open(f+".dupless", "w") as outfile:
    outfile.writelines(outlines)
 
