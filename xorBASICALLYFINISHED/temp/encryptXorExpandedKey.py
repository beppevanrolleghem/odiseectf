import os
import sys

KEY_SIZE = 10


def expand_key(key, length):
    return int(length / len(key)) * key + key[0:(length % len(key))]


def xor(s1, s2):
    assert len(s1) == len(s2)
    return bytes([(a ^ b) for a, b in zip(s1, s2)])


def main():
    if len(sys.argv) <= 2:
        key = os.urandom(KEY_SIZE)
        print(type(key))
        filename = sys.argv[1]

        f = open(filename,'rb')
        data = f.read()
        f.close()
        #temp = bytes([0x47, 0x49, 0x46, 0x38, 0x39, 0x61, 0xc0, 0x03, 0x80, 0x02])
        #eerste 10 bytes van voorbeeld afbeelding
        #temp = bytes([0x49,0x47, 0x38, 0x46, 0x61, 0x39, 0x03, 0xc0, 0x02, 0x80])
        #en dan krijg je deze bytes list
        #solution = bytes([0x47, 0x3b, 0x57, 0x2b, 0x07, 0xd0, 0x29, 0xdb, 0x3b, 0x82])
        #dus blijkbaar was de eerste set van bytes verkerd van volgorde, dus dit is de key die we dan krijgen (met de tweede temp)
        #07a70ffe4f233ffbf9dd
        #solution = bytes([0xf7, 0xa3, 0x1b, 0x32, 0xb1, 0x56, 0x94, 0x38, 0x3c, 0x90])
        #solution = bytes.fromhex("07a70ffe4f233ffbf9dd")
        #4947 3846 6139 03c0 0280

        #key = bytes("49473846613903c00280")
        #key = bytes.fromhex("0123456789")
        #4947 3846 6139 03c0 0280
        key = bytes(b'\x49\x47\x38\x46\x61\x39\x03\xc0\x02\x80')
        #key = bytes([0x49, 0x47, 0x38, 0x46, 0x61, 0x39, 0x03, 0xc0, 0x02, 0x80])
        #key = bytes([0x6e, 0x66, 0x4e, 0x7b, 0x94, 0xae, 0xd2, 0x15, 0xb4, 0xec])
        key = bytes(b'\x29\x2f\x08\x43\xad\xcf\x12\x16\x34\xee')
        key = bytes.fromhex('3f8015fb17b7e9a48477')
        expanded_key = expand_key(key, len(data))
        data_encrypted = xor(expanded_key, data)

        print(data_encrypted)

        f = open(filename + ".enc", "wb")
        f.write(data_encrypted)
        f.close()

        print("File %s encrypted with key: %s" % (filename, key.hex()))
    else:
        print("Usage: %s <filename>" % (sys.argv[0]))

if __name__ == "__main__":
    main()
