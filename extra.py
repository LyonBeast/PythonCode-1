
def decipher_fence(ciphertext,numRails):
    lengthOfStr = len(ciphertext)
    arr = ['']*lengthOfStr
    counter = 0
    while (counter < lengthOfStr):
        for x in range(numRails-1, -1, -1):
            for y in range(x,lengthOfStr,numRails):
                arr[y] = ciphertext[counter]
                counter += 1
    for x in arr    
    return arr 


teststr = "ejodinchmbglafkp"
print(decipher_fence(teststr,5)) #expect "abcdefghijklmnop"