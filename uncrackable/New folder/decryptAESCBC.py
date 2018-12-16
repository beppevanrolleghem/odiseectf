#!python3
import sys
import os
import getpass
from Cryptodome.Cipher import AES
from Cryptodome.Hash import MD5, SHA256 
from itertools import product
 

for group in list(product('azertyuiop', repeat = 6)):
        global passw
        passw = ''.join(group)
        print(passw + '\n')

        # generates key based on password
        def generatekey():
        
            return bytes.fromhex('084b8b05fae51beed25806aacf738fea')
            #return bytes.fromhex('1aa4e2c69d19ef436f0058168823c2b8')
  

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

            key = generatekey()
            decipher = AES.new(key, AES.MODE_CBC)
            decryptedcontent = decipher.decrypt(encryptedContent)

            ivlength = 16
            # remove iv and padding
            decryptedcontent = decryptedcontent[ivlength:-decryptedcontent[-1]]

            # check Integrity and retain cleartext
            if checkintegrity(decryptedcontent):
                cleartext = decryptedcontent[0:-64]
                # write to file
                outputfile = open(outputfilename, 'wb')
                outputfile.write(cleartext)
                outputfile.close()
            else:
                cleartext = 'Integrity check error'.encode()

            # useful only for decrypted text files
            # print(cleartext)

            


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
