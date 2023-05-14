import time

def rk_algorithm(patternStr, searchStr, charCount, maxPrime):
    h = 1
    patternHash = 0
    stringHash = 0
    patternLength = len(patternStr)
    stringLength = len(searchStr)
    for i in range(patternLength - 1):
        h = (h * charCount) % maxPrime #basic hash function with modulo

    print("HASH: ", h)

    for i in range(patternLength):
        #x=t[i]b^(M-1)+t[i+1]b^(M-2)+...+t[i+M-1]
        patternHash = (patternHash * charCount + ord(patternStr[i])) % maxPrime #calculate hash value for pattern
        stringHash = (stringHash * charCount + ord(searchStr[i])) % maxPrime #calculate hash value for text

    print("PATTERN HASH: ", patternHash)
    print("STRING HASH: ", stringHash)

    for i in range(stringLength - patternLength): #find pattern in text
        if patternHash == stringHash: #if hash values are equal
            for j in range(patternLength):
                if searchStr[i + j] != patternStr[j]: #compare char by char
                    break #chars in pattern don't match

            j += 1
            if j == patternLength:
                print("PATTERN AT INDEX: ", str(i)) #all char are found, strings are equal

        if i < (stringLength - patternLength):
            #x'=(x-t[i]b^(M-1))+t[i+M]
            stringHash = (charCount*(stringHash - ord(searchStr[i])*h) + ord(searchStr[i+patternLength])) % maxPrime #calculate new text hash value
        if stringHash < 0:
            stringHash = stringHash + maxPrime
            if stringHash < 0:
                stringHash = stringHash + charCount

patternStr = "ABCDE"
searchStr = "HFIRYWGCHIKRIEOEQWEABCDERTYU"
# patternLength = len(patternStr)
# stringLength = len(searchStr)
# patternHash = 0
# stringHash = 0
#h = 1
charCount = 64
maxPrime = 999999

start = time.perf_counter()
rk_algorithm(patternStr, searchStr, charCount, maxPrime)
stop = time.perf_counter() - start
print(str(round(stop,4)) + " seconds")