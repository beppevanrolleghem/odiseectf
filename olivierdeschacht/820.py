temp = []
with open("olivier.txt", "r") as infile:
   temp = infile.readlines()

with open("olivier820.txt", "w") as outfile:
    for t in temp:
        if len(t) < 8 and len(t) > 20:
            continue
        outfile.write(t+"\n")
