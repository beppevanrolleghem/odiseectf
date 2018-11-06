import os
import sys

KEY_SIZE = 10

def xor(s1, s2):
    assert len(s1) == len(s2)
    return bytes([(a ^ b) for a, b in zip(s1, s2)])

def expand_key(key, length):
    return int(length / len(key)) * key + key[0:(length % len(key))]



def main():
    if len(sys.argv) <= 2:
        key = os.urandom(KEY_SIZE)

        filename = sys.argv[1]

        f = open(filename,'rb')
        data = f.read()
        f.close()

        expanded_key = expand_key("0123456789", len(data))
        data_encrypted = xor(expanded_key, data)

        print(data_encrypted)

        f = open(filename + ".enc", "wb")
        f.write(data_encrypted)
        f.close()

        print("File %s encrypted with key: %s" % (filename, key.hex()))
    else:
        print("Usage: %s <filename>" % (sys.argv[0]))



'''

16^10 mogelijkheden, nie plezant dus, mss zoeken naar een andere manier da we iets kunnen vinden.

wat doet de expand key eigenlijk? dat soort dingen

'''

def decrypt():

    filename = "voorbeeld.gif.enc"
    with open("test.txt", "w") as outfile:
        for i in range(0,16**10):
            #print(bin(i).encode('ascii'))
            #print(bin(i).format('0<16'))
            #print(bin(i).format(16))
            #dus hier pak je de binaire versie van je iterator, en zet je die om naar een string, dit zal dus bv voor 1 0b1 geven, daarna wil je natuurlijk dat alle andere nullen erbij staan, anders krijg je geen 10 byte lange string, dus je haalt de 0b eraf en daarna gebruik je format en de string tussen de {} om de plaats links van onze input te vullen met 0
            temp = '{:0>80}'.format(str(bin(i))[2:]).encode('ascii')
            outfile.write(str(temp))
            #print(temp)
            #print(os.urandom(KEY_SIZE))
            if i > 10:
                break
    data = open(filename,'rb').read()
    print(expand_key("0123456789", len(data)))
    return True
















if __name__ == "__main__":
#    main()
    decrypt()


