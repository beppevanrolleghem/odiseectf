import hashlib


def hash(txt):
    return hashlib.sha512(str.encode(txt)).hexdigest()


lines = []
with open("output.txt", "r") as infile:
   lines = infile.readlines()

hashedlines = []
for l in lines:
    hashedlines.append(hash(l))

with open("outputHashed.txt", "w") as outfile:
    for l in hashedlines:
        outfile.write(l+"\n")
