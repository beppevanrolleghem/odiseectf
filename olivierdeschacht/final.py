import hashlib
import base64 as bo64
from itertools import combinations
dic = ["ollie", "olivier", "deschacht", "2014"]


with open("deschacht25.txt", "r") as infile:
    text = infile.read()


alts = {"a":"@",
        "e":"3",
        "o":"0",
        "s":"5",
        "g":"9",
        "i":"!"}

adders = ["!", "*"]

#yea, that shit works like that? isn't that mad?
def reverse(word):
    return word[::-1]


#set to -1 if you want to do all the chars
def altWord(word, l=-1):
    t = 0
    s = ""
    for letter in word:
        if letter in alts and t < l:
            s+=alts[letter]
        else:
            s+=letter
        t = t+1
    return s

def chopWord(word):
    s = ""
    l = []
    for c in word:
       s+=c
       l.append(s)
    return l


def addStartAndEnds(l):
    t = []
    for i in l:
        for a in adders:
            t.append(i+a)
            t.append(a+i)
    return t

def makeWords():
    words = dic.copy()
    for d in dic:
        for i in range(len(d)):
            words.append(altWord(d, i))

    temp2 = []
    for w in words:
        if len(w) > 1:
            temp2.append(reverse(w))
    words.extend(temp2)
    temp3 = addStartAndEnds(words)
    words.extend(temp3)
    return set(words)

#def decrypt(t, p):
#    aes = AES.new(p, AES.MODE_CBC, "")
#    return aes.decrypt(t)
temp = makeWords()
combos = []
for i in range(int(20/len(max(temp, key=len)))):
    for c in combinations(temp, i):
        w = "".join(c)
        if len(w) > 20 or len(w) < 8:
            continue
        else:
            combos.append(w)

with open("output.txt", "a") as outfile:
    for c in combos:
        outfile.write("{}\n".format(c))
