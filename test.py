'''
def encipher_fence(plaintext,numRails):
    ciphertext = ""
    r = []
    for x in range(0, numRails):
        r.append('')
        for y in range(x, len(plaintext)):
            if (y - x) % numRails == 0:
                r[x] = r[x] + plaintext[y]
    for z in range(len(r) - 1, -1, -1):
        ciphertext += r[z]
        
    return ciphertext
print(encipher_fence("python", -69))
        
            

def decipher_fence(ciphertext,numRails):
    remainder  = len(ciphertext) % numRails
    downLen = len(ciphertext) / numRails
    arr = []
    while remainder != 0:
        arr.append(downLen + 1)
        remainder -= 1
    for x in ciphertext:
        for y in range:

    return

def decode_text(ciphertext,wordfilename):
    decode_text(ciphertext,wordfilename) -> str
    attempts to decode ciphertext using railfence cipher
    wordfilename is a file with a list of valid words
'''


