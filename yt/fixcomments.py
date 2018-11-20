import json


with open('comments-AKLrKMz-avE.json', 'r') as infile:
    j = json.load(infile)
with open('commets.txt', 'w') as outfile:
    for item in j:

        try:
            if (item["commentText"]):
                temp = item["commentText"]
                outfile.write(temp.replace("\n", " ").replace("\r", " ")+"\n")
        except KeyError:
                print("wss een comment reply")
