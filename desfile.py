def desTextToType(file):
    global binaryCode
    binaryCode = ""
    lines= []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    file.close()
    for line in lines:
        for letter in line:
            letter = bin(ord(letter))
            letterWO = letter.replace("b", "")
            if len(letterWO) == 8:
                binaryCode += (letterWO)
            elif len(letterWO) != 8:
                while len(letterWO) != 8:
                    letterWO = "0" + letterWO
                binaryCode += (letterWO)
    return binaryCode
'''
Takes in the text from the file.
Converts each letter to binary with proper formatting (no B and length of 8).
Puts this all into one string called binaryCode
'''

def desTextToArray(file):
    global binaryArray
    binaryArray = []
    lines= []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    file.close()
    for line in lines:
        for letter in line:
            tempArray = []
            letter = bin(ord(letter))
            letterWO = letter.replace("b", "")
            if len(letterWO) == 8:
                tempArray.append(letterWO)
            elif len(letterWO) != 8:
                while len(letterWO) != 8:
                    letterWO = "0" + letterWO
                tempArray.append(letterWO)
            binaryArray.append(tempArray)
    return binaryArray
'''
Takes in the text from the file.
Converts each letter to binary with proper formatting (no B and length of 8).
Appends them all to the tempArray, which is appended to the binaryArray.
'''

def byteChecker(binaryCode, binaryArray):
    global checkWhich, arrayCounter, codeCounter, goodLength
    print("")
    goodLength = False
    codeCounter = 0
    arrayCounter = 0
    checkWhich = "array"
    if checkWhich == "array":
        for x in binaryArray:
            arrayCounter+=1
        if arrayCounter % 8 == 0:
            print("The array is 8 bytes long")
            checkWhich = "code"
            goodLength = True
            counter = 0
        elif arrayCounter % 8 != 0:
            print("The array is NOT 8 bytes long")
            checkWhich = "code"
            counter = 0
    if checkWhich == "code":
        for x in binaryCode:
            codeCounter+=1
        if len(binaryCode) % 64 == 0:
            print("The code is 8 bytes long")
            goodLength = True
        elif codeCounter % 64 != 0:
            print("The code is NOT 8 bytes long")
'''
Goes through the binaryArray first, and checks that it has a length of a multiple of 8 bytes. 
Goes through the binaryCode, then checks if that has a length of a multiple of 64 bits. 
If either have unsufficient lengths, goodLength is kept to false. 
If they have good lengths, goodLength is made to be true. 
'''

def lengthFixer(binaryCode, binaryArray, arrayCounter, codeCounter, goodLength):
    global paddedBinaryCode, paddedBinaryArray
    print("\nPADDING STARTUP")
    if goodLength == False:
        needToAdd = 0
        paddedBinaryCode = binaryCode
        paddedBinaryArray = binaryArray
        needToAdd = arrayCounter % 8
        needToAdd= 8 - needToAdd
        addThis = needToAdd
        addThis = bin(addThis)
        addThis = addThis.replace("b", "0")
        while len(addThis) != 8:
            addThis = "0" + addThis
        while needToAdd != 0:
            tempArray = []
            tempArray.append(addThis)
            paddedBinaryArray.append(tempArray)
            needToAdd -= 1


        needToAdd = codeCounter % 64
        needToAdd = (64 - needToAdd)//8
        addThis = needToAdd//8
        addThis = bin(addThis)
        addThis = addThis.replace("b", "0")
        while len(addThis) != 8:
            addThis = "0" + addThis
        while needToAdd != 0:
            paddedBinaryCode += addThis
            needToAdd -= 1
    elif goodLength == True:
        paddedBinaryCode = binaryCode
        paddedBinaryArray = binaryArray
    print(paddedBinaryArray)
    print(paddedBinaryCode)
    print("PADDING COMPLETE\n")
'''
Sets the paddedBinaryCode equal to the original code, and the paddedBinaryArray to the original as well.
Finds the amount of things it needs to add to the array first, then finds the binary code of that number with proper 
formatting. 
Then it appends the proper binary code to the array as an extra array(s) at the end until it's the proper length. 

Finds the amount of binary codes that it needs to add to the paddedBinaryCode. 
Finds the binary code of that, and fixes it to have the right formatting. 
Adds that to the paddedBinaryCode until it has no more things to add.
'''

def keyEncryption(key):
    global subKeys
    print("KEY ENCRYPTION COMMENCING")
    binaryKey = []
    oGKey = []
    permutatedKey = []
    tempLeft = []
    tempRight = []
    subKeys= []
    orderPermutate = [57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44,
              36, 63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20,
              12, 4]
    orderEncrypt = [14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10, 23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2, 41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48, 44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32]
    shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
    for letter in key:
        letter = bin(ord(letter))
        letterWO = letter.replace("b", "")
        if len(letterWO) == 8:
            for x in letterWO:
                binaryKey.append(x)
        elif len(letterWO) != 8:
            while len(letterWO) != 8:
                letterWO = "0" + letterWO
            for x in letterWO:
                binaryKey.append(x)
    for index in orderPermutate:
        permutatedKey.append(binaryKey[index-1])
    oGKey = permutatedKey


    for numberOfShifts in shifts:
        subKey = []
        if numberOfShifts ==1:
            tempLeft = (oGKey[0:28])
            addToEnd = tempLeft.pop(0)
            tempLeft.append(addToEnd)
            tempRight = (oGKey[28:])
            addToEnd = tempRight.pop(0)
            tempRight.append(addToEnd)
            oGKey = []
        elif numberOfShifts ==2:
            tempLeft = (oGKey[0:28])
            addToEnd = tempLeft.pop(0)
            tempLeft.append(addToEnd)
            addToEnd = tempLeft.pop(0)
            tempLeft.append(addToEnd)
            tempRight = (oGKey[28:])
            addToEnd = tempRight.pop(0)
            tempRight.append(addToEnd)
            addToEnd = tempRight.pop(0)
            tempRight.append(addToEnd)
            oGKey = []
        for x in tempLeft:
            oGKey.append(x)
        for x in tempRight:
            oGKey.append(x)

        for index in orderEncrypt:
            subKey.append(oGKey[index - 1])

        subKeys.append(subKey)
        print(subKey)
    print("KEY ENCRYPTION DONE\n")
'''
Goes through the key inputted, converting it to binary with the proper formatting. It is all in one array with each 
byte as an element.
Runs through the amount of shifts (16 different ones).
For each shift, it splits the array, and does 1 or 2 shifts based on which turn it is.
Saves the shifted arrays, and adds it to one big array.
Takes the big array that can be modified, and permutates it. 
Saves the permutated key to the subKeys array. 
Runs through this again with the original keys that only go through shifts. 
'''

def stringEncrypt(paddedBinaryCode):
    print("STRING ENCRYPTION COMMENCE")
    newBinaryCode= []
    order = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    expandRightOrder = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    rowsColumns = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

                   [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

                   [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

                   [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

                   [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

                    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

                   [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

                    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    sPermutate = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    finalPermutate = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    for index in order:
        newBinaryCode.append(paddedBinaryCode[index-1])


    for sub in subKeys:
        oGCode = newBinaryCode

        tempLeft = (oGCode[0:32])
        tempRight = (oGCode[32:])

        index = 0
        rowsColumnsBlock = 0
        sixArray = []
        counter = 0
        splitArray = []
        sixArray = []
        xORKey =[]
        expandedRight = []
        newRightWOPermutate = []
        newRightWithPermutate = []

        for index in expandRightOrder:
            expandedRight.append(tempRight[index - 1])

        index = 0
        for element in sub:
            if element == '0' and expandedRight[index] == '0':
                xORKey.append('0')
            elif element == '0' and expandedRight[index] == '1':
                xORKey.append('1')
            elif element == '1' and expandedRight[index] == '0':
                xORKey.append('1')
            elif element == '1' and expandedRight[index] == '1':
                xORKey.append('0')
            index += 1

        for element in xORKey:
            if counter != 6:
                sixArray.append(element)
                counter += 1
            if counter == 6:
                splitArray.append(sixArray)
                counter = 0
                sixArray = []

        for mini in splitArray:
            row = mini[0] + mini[5]
            row = int(row, 2)

            column = mini[1] + mini[2] + mini[3] + mini[4]
            column = int(column, 2)


            tableCode = rowsColumns[rowsColumnsBlock][row][column]
            tableCode = bin(tableCode)
            tableCode = tableCode.replace("b", "")
            if len(tableCode) <4:
                while len(tableCode)<4:
                    tableCode = "0" + tableCode
            elif len(tableCode) ==5:
                tableCode = tableCode[1:]
            rowsColumnsBlock+=1

            for x in tableCode:
                newRightWOPermutate.append(x)

        for index in sPermutate:
            newRightWithPermutate.append(newRightWOPermutate[index-1])


        leftnminus = tempLeft
        rightnminus = tempRight
        newLeft = rightnminus
        newRight = []

        index = 0
        for element in leftnminus:
            if element == '0' and newRightWithPermutate[index] == '0':
                newRight.append('0')
            elif element == '0' and newRightWithPermutate[index] == '1':
                newRight.append('1')
            elif element == '1' and newRightWithPermutate[index] == '0':
                newRight.append('1')
            elif element == '1' and newRightWithPermutate[index] == '1':
                newRight.append('0')
            index += 1
        newBinaryCode = []
        for x in newLeft:
            newBinaryCode.append(x)
        for x in newRight:
            newBinaryCode.append(x)

    reversedBinaryCode = []
    for x in newBinaryCode[32:]:
        reversedBinaryCode.append(x)
    for x in newBinaryCode[:32]:
        reversedBinaryCode.append(x)

    finalCode = []
    for index in finalPermutate:
        finalCode.append(reversedBinaryCode[index - 1])

    hexFinal = []
    counter = 0
    tempHex = ""
    for x in finalCode:
        if counter != 8:
            tempHex += x
            counter += 1
        if counter == 8:
            tempHex = int(tempHex, 2)
            hexFinal.append(hex(tempHex))
            tempHex = ""
            counter = 0
    print(hexFinal)
    firstHex = False
    if needsAppend == False:
        file = open("midput.txt", "w")
        for x in hexFinal:
            file.write(str(x) + "\n")
        file.close()
        file = open("showmidput.txt", "w")
        for x in hexFinal:
            if firstHex == False:
                firstHex = True
            elif firstHex == True:
                x = x[2:]
            file.write(str(x))
    elif needsAppend == True:
        file = open("midput.txt", "w")
        for x in hexFinal:
            file.write(str(x) + "\n")
        file.close()
        if writtenFrequency == 0:
            file = open("showmidput.txt", "w")
            for x in hexFinal:
                if firstHex == False:
                    firstHex = True
                elif firstHex == True:
                    x = x[2:]
                file.write(str(x))
            file.close()
        elif writtenFrequency > 0:
            file = open("showmidput.txt", "a")
            for x in hexFinal:
                x.replace("0x", "")
            file.write(str(x))
            file.close()
    print("STRING ENCRYPTION DONE\n")
'''
For each 8 bytes in the code of the message.
It permutates it originally. 
Goes through all the subkeys. 
Splits the code into a right and left.
Expands the right using a special permutation.
Goes through an XOR between the expanded right and the subkey.
Splits that XOR array into 6 byte blocks.
Runs through the block arrays.
It takes the first and last element of the 6 byte blocks, finds the binary code of that.
Takes the middle four element of the 6 byte block, finds the binary code of that.
Finds the element at the row and column of the right block array from the big array of block arrays.
Converts that number element to binary, appends it to the newRightWOPermutate.
Permutates the newRightWOPermutate to newRightWithPermutate.
Puts the original right array to the left, and does an XOR function between that and the new right.
Appends the old right (left) and XORd right to the array newBinaryCode.
Reverses the right and left of the newBinaryCode to reversedBinaryCode.
Permutates that a final time. 
Converts that to hex for every 8 elements in the code. 
Writes and appends (after the first loop) the hex codes with proper formatting (only one 0x beginning it) to the 
showmidput.txt.
Writes the hex codes in full to the midput.txt file so it can be read and decrypted.
'''

def readHex(file):
    print("CONVERTING TO HEX")
    global hexToBinary
    lines = []
    hexToBinary = []
    line = file.readline()
    while line:
        lines.append(line.strip())
        line = file.readline()

    for x in lines:
        tempAdd = int(x, 0)
        tempAdd = bin(tempAdd)
        tempAdd = tempAdd[2:]
        if len(tempAdd) < 8:
            while len(tempAdd) != 8:
                tempAdd = "0" + tempAdd
        hexToBinary.append(tempAdd)
    temp = hexToBinary
    hexToBinary = []
    for x in temp:
        for element in x:
            hexToBinary.append(element)

    print(hexToBinary)
    print("CONVERTED TO HEX AND WRITTEN\n")
'''
Reads from the midput.txt file for every 8 byte strand encrypted from the paddedBinaryCode.
Converts those hex codes to binary, and adds them to the hexToBinary array.
'''

def reverseKeys(subKeys):
    global reversedKeys
    print("REVERSING KEYS")
    reversedKeys = []
    index = 15
    while len(reversedKeys) != 16:
        reversedKeys.append(subKeys[index])
        print(subKeys[index])
        index -= 1
    print("KEYS REVERSED\n")
'''
Reverses all the subkeys. 
16 goes to 1, etc. 
'''

def stringDecrypt(hexToBinary, reversedKeys):
    print("STRING DECRYPTION COMMENCE\n")
    newBinaryCode= []
    order = [58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4, 62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8, 57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3, 61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7]
    expandRightOrder = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    rowsColumns = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
                   [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
                   [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
                   [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

                   [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
                    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
                    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
                    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

                   [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
                    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
                    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
                    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

                   [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
                    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
                    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
                    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

                   [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
                    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
                    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
                    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

                    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
                    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
                    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
                    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

                   [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
                    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
                    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
                    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

                    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
                    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
                    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
                    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]
    sPermutate = [16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10, 2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25]
    finalPermutate = [40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31, 38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29, 36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27, 34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25]

    for index in order:
        newBinaryCode.append(hexToBinary[index-1])


    for sub in reversedKeys:
        oGCode = newBinaryCode

        tempLeft = (oGCode[0:32])
        tempRight = (oGCode[32:])

        index = 0
        rowsColumnsBlock = 0
        sixArray = []
        counter = 0
        splitArray = []
        sixArray = []
        xORKey =[]
        expandedRight = []
        newRightWOPermutate = []
        newRightWithPermutate = []

        for index in expandRightOrder:
            expandedRight.append(tempRight[index - 1])

        index = 0
        for element in sub:
            if element == '0' and expandedRight[index] == '0':
                xORKey.append('0')
            elif element == '0' and expandedRight[index] == '1':
                xORKey.append('1')
            elif element == '1' and expandedRight[index] == '0':
                xORKey.append('1')
            elif element == '1' and expandedRight[index] == '1':
                xORKey.append('0')
            index += 1

        for element in xORKey:
            if counter != 6:
                sixArray.append(element)
                counter += 1
            if counter == 6:
                splitArray.append(sixArray)
                counter = 0
                sixArray = []

        for mini in splitArray:
            row = mini[0] + mini[5]
            row = int(row, 2)

            column = mini[1] + mini[2] + mini[3] + mini[4]
            column = int(column, 2)


            tableCode = rowsColumns[rowsColumnsBlock][row][column]
            tableCode = bin(tableCode)
            tableCode = tableCode.replace("b", "")
            if len(tableCode) <4:
                while len(tableCode)<4:
                    tableCode = "0" + tableCode
            elif len(tableCode) ==5:
                tableCode = tableCode[1:]
            rowsColumnsBlock+=1

            for x in tableCode:
                newRightWOPermutate.append(x)

        for index in sPermutate:
            newRightWithPermutate.append(newRightWOPermutate[index-1])


        leftnminus = tempLeft
        rightnminus = tempRight
        newLeft = rightnminus
        newRight = []

        index = 0
        for element in leftnminus:
            if element == '0' and newRightWithPermutate[index] == '0':
                newRight.append('0')
            elif element == '0' and newRightWithPermutate[index] == '1':
                newRight.append('1')
            elif element == '1' and newRightWithPermutate[index] == '0':
                newRight.append('1')
            elif element == '1' and newRightWithPermutate[index] == '1':
                newRight.append('0')
            index += 1
        newBinaryCode = []
        for x in newLeft:
            newBinaryCode.append(x)
        for x in newRight:
            newBinaryCode.append(x)

    reversedBinaryCode = []
    for x in newBinaryCode[32:]:
        reversedBinaryCode.append(x)
    for x in newBinaryCode[:32]:
        reversedBinaryCode.append(x)
    finalCode = []
    for index in finalPermutate:
        finalCode.append(reversedBinaryCode[index - 1])

    finalTranslated = []
    temp = ""
    counter = 0
    for x in finalCode:
        if counter != 8:
            temp += x
            counter += 1
        if counter == 8:
            temp = chr(int(temp, 2))
            finalTranslated.append(temp)
            counter = 0
            temp = ""
    if needsAppend == False:
        file = open("output.txt", "w")
        for x in finalTranslated:
            if x != (len(binaryCode) % 64) // 4:
                file.write(x)
        file.close()
    elif needsAppend == True:
        if writtenFrequency == 0:
            file = open("output.txt", "w")
            for x in finalTranslated:
                if x != (len(binaryCode) % 64) // 4:
                    file.write(x)
            file.close()
        elif writtenFrequency > 0:
            file = open("output.txt", "a")
            for x in finalTranslated:
                if x != (len(binaryCode) % 64) //4:
                    file.write(x)
            file.close()
    print("STRING DECRYPTION DONE\n")
'''
For each 8 byte block taken from the encrypted hex codes.
It permutates it originally. 
Goes through all the reversed subkeys. 
Splits the code into a right and left.
Expands the right using a special permutation.
Goes through an XOR between the expanded right and the subkey.
Splits that XOR array into 6 byte blocks.
Runs through the block arrays.
It takes the first and last element of the 6 byte blocks, finds the binary code of that.
Takes the middle four element of the 6 byte block, finds the binary code of that.
Finds the element at the row and column of the right block array from the big array of block arrays.
Converts that number element to binary, appends it to the newRightWOPermutate.
Permutates the newRightWOPermutate to newRightWithPermutate.
Puts the original right array to the left, and does an XOR function between that and the new right.
Appends the old right (left) and XORd right to the array newBinaryCode.
Reverses the right and left of the newBinaryCode to reversedBinaryCode.
Permutates that a final time. 
Converts that to text for each 8 byte hex block.
Writes and appends the converted to text without the excess padding numbers to the output.txt file.
'''

writtenFrequency = 0
file = open("input.txt", "r")
print(desTextToType(file))
file = open("input.txt", "r")
print(desTextToArray(file))
byteChecker(binaryCode, binaryArray)
lengthFixer(binaryCode, binaryArray, arrayCounter, codeCounter, goodLength)
key = ""
while key == "":
    key = str(input("Enter a key with a length of 8:\n>"))
    if len(key) == 8:
        key = key
    elif len(key) != 8:
        key = ""
        print("INCORRECT LENGTH")
keyEncryption(key)
reverseKeys(subKeys)
if len(paddedBinaryCode) == 64:
    needsAppend = False
    stringEncrypt(paddedBinaryCode)
    file = open("midput.txt", "r")
    readHex(file)
    stringDecrypt(hexToBinary, reversedKeys)
elif len(paddedBinaryCode) > 64:
    needsAppend = True
    temp = paddedBinaryCode
    paddedBinaryCode = ""
    counter = 0
    print(temp)
    for x in temp:
        if counter != 64:
            paddedBinaryCode += x
            counter +=1
        if counter == 64:
            print(paddedBinaryCode)
            stringEncrypt(paddedBinaryCode)
            file = open("midput.txt", "r")
            readHex(file)
            stringDecrypt(hexToBinary, reversedKeys)
            paddedBinaryCode = ""
            counter = 0
            writtenFrequency += 1
'''
Sets writtenFrequency to 0 in order for it to know when to append or write to a file.
Runs the functions that convert the message to an array and a code. 
Runs the byte checker and the padding functions. 
Asks for an 8 byte key until the user inputs an acceptible one.
Encrypts and reverses the subkeys. 
If the paddedBinaryCode is only 64 bits long, then it runs the encryption and decryption functions once as normal.
If the paddedBinaryCode is more than 64 bits long, it runs it for each 64 bit string of the main one.
Appends the elements of the temp array to the paddedBinaryCode until it has 64 bits, so it can run as normal.
Runs the encryption and decryption functions as normal, along with the readHex function.
Resets the paddedBinaryCode.
Adds 1 to the writtenFrequency so that it knows to append the next time. 
'''