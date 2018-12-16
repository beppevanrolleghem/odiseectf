import json


with open('comments-AKLrKMz-avE.json', 'r', encoding="utf8") as infile:
    j = json.load(infile)
with open('commets.txt', 'w') as outfile:
    for item in j:

<<<<<<< HEAD
        try:
            if (item["commentText"]):
                temp = item["commentText"]
                woordjes = temp.replace("\n", " ").replace("\r", " ").split(" ")
                for w in woordjes:
                    outfile.write(w+"\n")
        except KeyError:
                print("wss een comment reply")
=======

for item in j:
	try:
		with open('lijst.txt','a') as outfile:
			if (item["commentText"]):
				temp = item["commentText"]
				outfile.write(temp+"\n")
	except KeyError:
		print("wss een comment reply")
>>>>>>> ce4144fab82340b3c9d5adb48ba585ec7c72cb9a
