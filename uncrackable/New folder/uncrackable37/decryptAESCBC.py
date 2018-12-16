import sys
import os
import getpass

from Crypto.Cipher import AES
# from Crypto.Random import get_random_bytes, random
# from Crypto.Util import Padding
from Crypto.Hash import MD5, SHA256


# generates key based on password
def generatekey():
    password = getpass.getpass('Password for decryption: ')

    h = MD5.new()
    h.update(''.join(password))

    return h.digest()


# calculates and return hash for message
def calculatehash(message):
    h = SHA256.new()
    h.update(message)
    # use hexdigest to prevent problems with control characters
    # e.g. \r in charcter 5, appends 4, then overwrites beginning of message with rest of digest
    return h.hexdigest()


# check integrity and return cleartext or error message
def checkintegrity(decryptedcontent):
    return calculatehash(decryptedcontent[0:-64]) == decryptedcontent[-64:]


# encrypts content in AES CBC mode
def decrypt_AES_CBC(inputfilename, encryptedContent):
    # create encrypted filename, keep extension
    outputfilename = inputfilename[0:inputfilename.find('.', len(inputfilename) - 5)] + '_decrypted' + inputfilename[
                                                                                                       inputfilename.find(
                                                                                                           '.'):len(
                                                                                                           inputfilename)]

    key = generatekey()
    decipher = AES.new(key, AES.MODE_CBC)
    decryptedcontent = decipher.decrypt(encryptedContent)

    ivlength = 16
    # remove iv and padding
    decryptedcontent = decryptedcontent[ivlength:-ord(decryptedcontent[-1])]

    # check Integrity and retain cleartext
    if checkintegrity(decryptedcontent):
        cleartext = decryptedcontent[0:-64]
    else:
        cleartext = 'Integrity check error'

    # useful only for decrypted text files
    # print(cleartext)

    # write to file
    outputfile = open(outputfilename, 'wb')
    outputfile.write(cleartext)
    outputfile.close()


for i in sys.argv[1:]:

    inputfilename = i

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
