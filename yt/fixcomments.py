import json


with open('comments-AKLrKMz-avE.json', 'r', encoding="utf8") as infile:
    j = json.load(infile)


for item in j:
	try:
		with open('lijst.txt','a') as outfile:
			if (item["commentText"]):
				temp = item["commentText"]
				outfile.write(temp+"\n")
	except KeyError:
		print("wss een comment reply")
