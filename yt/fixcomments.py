import json


with open('comments-AKLrKMz-avE.json', 'r') as infile:
    j = json.load(infile)

for item in j:
    try:
        if (item["commentText"]):
            temp = item["commentText"]
            print(temp.replace("\n", " ").replace("\r", " "))
    except KeyError:
            print("wss een comment reply")
