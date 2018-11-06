import sys
import os
import getpass
import itertools
from Crypto.Cipher import AES
from Crypto.Hash import MD5, SHA256


# generates key based on password
def generatekey(pw):
    password = pw   # getpass.getpass('Password for decryption: ')
    #print(password)
    h = MD5.new()
    h.update(password.encode())
    #h.update(password)
    return h.digest()

def generatePass():
    temp = []
    alpha = ["a", "z", "e", "r", "t", "y", "u", "i", "o", "p"]
    for i in itertools.product(alpha, repeat=6):
        temp.append(generatekey("".join(i)))
    return temp

# calculates and return hash for message
def calculatehash(message):
    h = SHA256.new()
    h.update(message)
    # use hexdigest to prevent problems with control characters
    # e.g. \r in charcter 5, appends 4, then overwrites beginning of message with rest of digest
    return h.hexdigest()


# check integrity and return cleartext or error message
def checkintegrity(decryptedcontent):
    return calculatehash(decryptedcontent[0:-64]).encode() == decryptedcontent[-64:]


# encrypts content in AES CBC mode
def decrypt_AES_CBC(inputfilename, encryptedContent):
    # create encrypted filename, keep extension
    outputfilename = inputfilename[0:inputfilename.find('.', len(inputfilename) - 5)] \
                     + '_decrypted' + inputfilename[inputfilename.find('.'):len(inputfilename)]

    i = 0
    keys = generatePass()
    print(len(keys))
    for key in keys:
        decipher = AES.new(key, AES.MODE_CBC)
        decryptedcontent = decipher.decrypt(encryptedContent)
        ivlength = 16
        # remove iv and padding
        decryptedcontent = decryptedcontent[ivlength:-decryptedcontent[-1]]
        # check Integrity and retain cleartext
        if checkintegrity(decryptedcontent):
            cleartext = decryptedcontent[0:-64]
            outputfile = open(outputfilename, 'wb')
            outputfile.write(cleartext)
            outputfile.close
            outputfilename = outputfilename+"EXTRA"
        else:
            cleartext = 'Integrity check error'.encode()
            print("error:{}".format(i))
            i = i+1
    print("done?")

    return

#
#
#    key = generatekey()
#    decipher = AES.new(key, AES.MODE_CBC)
#    decryptedcontent = decipher.decrypt(encryptedContent)
#
#    ivlength = 16
#    # remove iv and padding
#    decryptedcontent = decryptedcontent[ivlength:-decryptedcontent[-1]]
#
#    # check Integrity and retain cleartext
#    if checkintegrity(decryptedcontent):
#        cleartext = decryptedcontent[0:-64]
#    else:
#        cleartext = 'Integrity check error'.encode()
#
#    # useful only for decrypted text files
#    # print(cleartext)
#
#    # write to file
#    outputfile = open(outputfilename, 'wb')
#    outputfile.write(cleartext)
#    outputfile.close()


for i in sys.argv[1:]:

    inputfilename = i

    print('decrypting ' + inputfilename)

    try:
        inputfile = open(inputfilename, 'rb')
    except IOError:
        print("File " + inputfilename + " not found, working directory: " + os.getcwd())
        continue
    else:
        # if file opened, read content into variable
        content = inputfile.read()
        inputfile.close()

    # apply symmetric encryption
    decrypt_AES_CBC(inputfilename, content)
    # encrypt_AES_ECB(inputfilename,content)
