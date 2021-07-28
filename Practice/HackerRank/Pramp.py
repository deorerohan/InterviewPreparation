def isLoveLetterReproducible(L, M):
    charMap = []
    charCount = 0

    for i in range(len(L)):
        charCode = int(L[i])
        if charMap[charCode] == 0:
            charCount += 1
        charMap[charCode] += 1

    for i in range(len(M)):
        charCode = int(M[i])
        if charMap[charCode] > 0:
            charMap[charCode] -= 1
            if charMap[charCode] == 0:
                charCount -= 1
        if charCount == 0:
            return True

    return False
