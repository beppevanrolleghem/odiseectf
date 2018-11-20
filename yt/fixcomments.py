import json


with open('comments-AKLrKMz-avE.json', 'r') as infile:
    j = json.load(infile)
with open('commets.txt', 'w') as outfile:
    for item in j:

        try:
            if (item["commentText"]):
                temp = item["commentText"]
                woordjes = temp.replace("\n", " ").replace("\r", " ").split(" ")
                for w in woordjes:
                    outfile.write(w+"\n")
        except KeyError:
                print("wss een comment reply")
