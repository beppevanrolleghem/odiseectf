import test


allofem = test.makeWords()
with open("output.txt", "a") as outfile:
    for i in range(20):
        for combo in test.combinations(allofem, i):
            c = "".join(combo)
            if len(c) > 20 or len(c) < 8:
                continue
            else:
                #outfile.write(decrypt(text,c))
                temp = test.bo64.b64enconde(str.encode(hashlib.sha512(c).hexdigest()))
                if len(temp) == len(text):
                    if temp == text:
                        outfile.write("we may have got it: {} transformed turned into: {}".format(c, temp))
                    else:
                        outfile.write("i mean maybe... {} transformed turned into: {}".format(c, temp))
