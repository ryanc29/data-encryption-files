def stringShift(originalString, shiftValue):
    endString=""
    for x in originalString:
        characterCode= ord(x)
        if characterCode != 32 and characterCode != 10:
            characterCode+=shiftValue
        endString+=str(chr(characterCode))
    return endString
'''
This function takes a string and a shift value as a parameter. 
It then gets the character code for each letter, and adds the shift value to the code then returns the shifted string.
'''
def stringDecrypt(endString):
    decryptedString=""
    for x in endString:
        characterCode = ord(x)
        if characterCode != 32 and characterCode != 10:
            characterCode -= shiftValue
        decryptedString += str(chr(characterCode))
    return decryptedString
'''
This takes in the encrypted string from the prior function as a parameter. 
It goes through the string, finds the character code, then subtracts it and adds the letter to the decrypted string. 
'''
#////////////////////////////////////////////////////////////////////////////////////////////

def fileShift(originalFile, shiftValue):
    lines=[]
    endLines=[]
    line = originalFile.readline()
    while line:
        lines.append(line)
        line= originalFile.readline()
    originalFile.close()
    encryptedFile= open("encryptedtextfile.txt", "w")
    for x in lines:
        endString=""
        for letter in x:
            characterCode = ord(letter)
            if characterCode!=32 and characterCode!=10:
                characterCode += shiftValue
            endString += str(chr(characterCode))
        endLines.append(endString)
    while len(endLines) != 0:
        encryptedFile.write(endLines.pop(0))
    encryptedFile.close()
'''
This takes the file ciphertextfile and a shift value as paraemeters. 
It gets all the lines of the original file, runs through it, and adds the shift value to all characters but spaces and \n's
It then writes these shifted letters to the encryptedtexifile.
'''

def fileDecrypt(encryptedFile):
    lines=[]
    line = encryptedFile.readline()
    endLines=[]
    while line:
        lines.append(line)
        line = encryptedFile.readline()
    encryptedFile.close()
    decryptedFile= open("decryptedfile.txt", "w")
    for x in lines:
        endString=""
        for letter in x:
            characterCode = ord(letter)
            if characterCode!=32 and characterCode!=10:
                characterCode -= shiftValue
            endString += str(chr(characterCode))
        endLines.append(endString)
    while len(endLines) != 0:
        decryptedFile.write(endLines.pop(0))
'''
This takes in the encryptedtextfile as a parameter, and reads through the lines and adds them to an array.
It then goes through each letter in the array, and subtracts the shift value.
Then it writes the decrypted text to the decryptedtextfile.
'''

#///////////////////////////////////////////////////////////////////////////////////////

def railEncryptString(originalString, rows):
    fullStringArray=[]
    thisRow=0
    fullStringString=""
    while thisRow<rows:
        fullStringArray.append([])
        thisRow+=1
    thisRow=1
    for letter in originalString:
        if thisRow!=rows:
            fullStringArray[(thisRow-1)].extend(letter)
            thisRow+=1
        elif thisRow==rows:
            fullStringArray[(thisRow - 1)].extend(letter)
            thisRow=1
    for mini in fullStringArray:
        for letter in mini:
            fullStringString+=letter
    print(fullStringString)
    return fullStringArray
'''
This takes a string and a number of rows as input.
It makes small arrays within a 2D array for the total lines that the user wants for the cypher.
It then runs through the string, and the arrays. So if the user wanted 2 rows, it would alternate putting letters
into the first and second arrays until the end of the word. EX: 2 rows, "Hello". Would be |Hlo|el|
'''

def railDecryptString(fullStringArray):
    decryptedArray=[]
    decryptedString=""
    thisRow = 1
    lettersAdded=0
    totalLetters=0
    for mini in fullStringArray:
        for letter in mini:
            totalLetters+=1
    while lettersAdded<totalLetters:
        if thisRow!=rows:
            decryptedArray.extend(fullStringArray[thisRow-1].pop(0))
            thisRow+=1
            lettersAdded+=1
        elif thisRow==rows:
            decryptedArray.extend(fullStringArray[thisRow-1].pop(0))
            thisRow=1
            lettersAdded+=1
    for x in decryptedArray:
        decryptedString+=x
    return decryptedString
'''
This takes the array of the rows as a parameter.,
It runs through the mini arrays and counts the total number of letters.
Then, it knows which row it is on, and has a while loop to make sure all letters are added. 
It adds each letter, looping through arrays as long as it is not the end of the arrays.
Once it reaches the end of the arrays, it resets to the first one.
Adds all these in order to a string, and returns it. 
'''

#/////////////////////////////////////////////////////////////////////////////////////////////

def railCipherFile(rows, file):
    thisRow=1
    encryptedArray=[]
    arrayCount=0
    lines = []
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    file.close()
    while arrayCount<rows:
        encryptedArray.append([])
        arrayCount+=1
    for line in lines:
        for letter in line:
            if thisRow!=rows:
                encryptedArray[(thisRow-1)].extend(letter)
                thisRow+=1
            elif thisRow==rows:
                encryptedArray[(thisRow - 1)].extend(letter)
                thisRow=1
    file = open("encryptedtextfile.txt", "w")
    for mini in encryptedArray:
        for letter in mini:
            file.write(letter + "\n")
        file.write("ROW\n")
    file.close()
'''
Takes in a ciphertextfile and an amount of rows as a parameter. 
Runs through the file putting it into arrays by line.
Makes mini arrays within a 2D array for each desired line. 
Then runs through the letters of each line, putting them into the mini arrays (running through those too).
Makes sure that it does not go beyond the amount of mini arrays.
Then writes each letter to encryptedtextfile.
'''
def railCipherFileDecrypt(file):
    encryptedArray = []
    line = file.readline()
    temp = []
    while line:
        if line.strip() == "ROW":
            encryptedArray.append(temp)
            temp = []
        elif line.strip() != "ROW":
            temp.append(line.strip())
        line = file.readline()
    file.close()
    decryptedArray = []
    thisRow = 1
    lettersAdded = 0
    totalLetters = 0
    for mini in encryptedArray:
        for letter in mini:
            totalLetters += 1
    while lettersAdded < totalLetters:
        if thisRow != rows:
            decryptedArray.extend(encryptedArray[thisRow - 1].pop(0))
            thisRow += 1
            lettersAdded += 1
        elif thisRow == rows:
            decryptedArray.extend(encryptedArray[thisRow - 1].pop(0))
            thisRow = 1
            lettersAdded += 1
    file = open("decryptedfile.txt", "w")
    for letter in decryptedArray:
        file.write(letter)
    file.close()
'''
This takes the encryptedarray and decryptedtextfile as parameters.
It runs through the encryptedarray with mini arrays in it.
Counts the number of total letters.
Then it runs through the mini arrays, adding them to the decryptedarray in order.
It resets to the beginning array when it reaches the end. 
Lastly, it runs through the decryptedarray and wrties it to the decryptedfile.
'''
#//////////////////////////////////////////////////////////////////////////////////////////////////

def polybiusStringCipher(string):
    codeArray=[]
    tempArray=[]
    codeString=""
    for letter in string:
        if ord(letter)>=65 and ord(letter)<=70:
            tempArray.append(1)
            tempArray.append((ord(letter)-65)+1)
            codeArray.append(tempArray)
        elif ord(letter)>=71 and ord(letter)<=76:
            tempArray.append(2)
            tempArray.append((ord(letter) - 71) + 1)
            codeArray.append(tempArray)
        elif ord(letter) >= 77 and ord(letter) <= 82:
            tempArray.append(3)
            tempArray.append((ord(letter) - 77) + 1)
            codeArray.append(tempArray)
        elif ord(letter)>=83 and ord(letter)<=88:
            tempArray.append(4)
            tempArray.append((ord(letter) - 83) + 1)
            codeArray.append(tempArray)
        elif ord(letter)>=89 and ord(letter)<=90:
            tempArray.append(5)
            tempArray.append((ord(letter) - 89) + 1)
            codeArray.append(tempArray)
        elif ord(letter)>=48 and ord(letter)<=51:
            tempArray.append(5)
            tempArray.append((ord(letter) - 48) + 3)
            codeArray.append(tempArray)
        elif ord(letter)>=52 and ord(letter)<=57:
            tempArray.append(6)
            tempArray.append((ord(letter) - 52) + 1)
            codeArray.append(tempArray)
        tempArray = []
    for mini in codeArray:
        for x in mini:
            codeString+=str(x)
        codeString+=" "
    print(codeString)
    return codeArray
'''
Takes in a string of only capitals and numbers as a parameter.
Runs through the string, and checks which row it is in based on being between certain character values.
Adds the row code number to the temparray, then finds the distance to the start of the row, and adds 1 to match with the
table.
Adds the column code to the temparray.
Adds the temparray to the codearray.
Then runs through the codearray, adding each code to a string along with a space, and returns that.  
'''
def polybiusStringDecrypt(codeArray):
    fullLetterArray=[]
    fullLetterString=""
    for mini in codeArray:
        if mini[0]==1:
            letter= chr(65+ (mini[1]-1))
        elif mini[0]==2:
            letter= chr(71 + (mini[1]-1))
        elif mini[0]==3:
            letter= chr(77 + (mini[1]-1))
        elif mini[0]==4:
            letter= chr(83 + (mini[1]-1))
        elif mini[0]==5 and mini[1]<3:
            letter= chr(89 + (mini[1]-1))
        elif mini[0]==5 and mini[1]>=3:
            letter= chr(48 + (mini[1]-3))
        elif mini[0]==6:
            letter= chr(52 + (mini[1]-1))
        fullLetterArray.append(letter)
    for x in fullLetterArray:
        fullLetterString+=x
    return fullLetterString
'''
Takes in the codearray as a parameter.
Runs through the codearray, finding the character at the 0th index, or the row. 
Then, it takes the column number, subtracts 1 so it matches up again, and then adds the character code of the first letter
of the row. 
Then it converts it to a letter based on this algorithm, and adds it to the fullletterarray.
Then it runs through the fulllletterarray and adds these letters to a string, and returns that. 
'''

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

def polybiusFileEncrypt(file):
    codeArray=[]
    tempArray=[]
    lines=[]
    line = file.readline()
    while line:
        lines.append(line)
        line=file.readline()
    file.close()
    for mini in lines:
        for letter in mini:
            if ord(letter) >= 65 and ord(letter) <= 70:
                tempArray.append(1)
                tempArray.append((ord(letter) - 65) + 1)
                codeArray.append(tempArray)
            elif ord(letter) >= 71 and ord(letter) <= 76:
                tempArray.append(2)
                tempArray.append((ord(letter) - 71) + 1)
                codeArray.append(tempArray)
            elif ord(letter) >= 77 and ord(letter) <= 82:
                tempArray.append(3)
                tempArray.append((ord(letter) - 77) + 1)
                codeArray.append(tempArray)
            elif ord(letter) >= 83 and ord(letter) <= 88:
                tempArray.append(4)
                tempArray.append((ord(letter) - 83) + 1)
                codeArray.append(tempArray)
            elif ord(letter) >= 89 and ord(letter) <= 90:
                tempArray.append(5)
                tempArray.append((ord(letter) - 89) + 1)
                codeArray.append(tempArray)
            elif ord(letter) >= 48 and ord(letter) <= 51:
                tempArray.append(5)
                tempArray.append((ord(letter) - 48) + 3)
                codeArray.append(tempArray)
            elif ord(letter) >= 52 and ord(letter) <= 57:
                tempArray.append(6)
                tempArray.append((ord(letter) - 52) + 1)
                codeArray.append(tempArray)
            else:
                tempArray.append(letter)
                codeArray.append(tempArray)
            tempArray = []
    file = open("encryptedtextfile.txt", "w")
    counter = 0
    for mini in codeArray:
        for code in mini:
            if code != " " and code != "\n":
                if counter != 1:
                    file.write(str(code))
                    counter += 1
                elif counter == 1:
                    file.write(str(code) + "\n")
                    counter = 0
            elif code == " ":
                file.write("SPACE" + "\n")
            elif code == "\n":
                file.write("BACKSLASHN" + "\n")
        file.write("NEW\n")
    file.close()
'''
Takes in the polybiuscyphertext as a parameter as it is only capitals. 
Makes an array for the lines of the file.
Runs through the array, appending the row of the letter based on the character code to the temparray.
Again, it finds the distance to the letter beginning the row, adds 1 so it matches up, then adds it to the temparray.
After that, it adds the temparray to the codearray.
If the letter is a space of a \n it just adds that.
Writes each code to encryptedtextfile.
'''
def polybiusFileDecrypt(file):
    codeArray = []
    line = file.readline()
    while line:
        if line.strip() != "NEW":
            if line.strip() == "BACKSLASHN":
                codeArray.append(["\n"])
            elif line.strip() == "SPACE":
                codeArray.append([" "])
            else:
                temp = []
                line = line.strip()
                for x in line:
                    temp.append(int(x))
                codeArray.append(temp)
        line = file.readline()
    fullLetterArray=[]
    for mini in codeArray:
        if mini[0]==1:
            letter= chr(65+ (mini[1]-1))
        elif mini[0]==2:
            letter= chr(71 + (mini[1]-1))
        elif mini[0]==3:
            letter= chr(77 + (mini[1]-1))
        elif mini[0]==4:
            letter= chr(83 + (mini[1]-1))
        elif mini[0]==5 and mini[1]<3:
            letter= chr(89 + (mini[1]-1))
        elif mini[0]==5 and mini[1]>=3:
            letter= chr(48 + (mini[1]-3))
        elif mini[0]==6:
            letter= chr(52 + (mini[1]-1))
        elif mini[0]=="\n":
            letter="\n"
        elif mini[0]==" ":
            letter=" "
        fullLetterArray.append(letter)
    file = open("decryptedfile.txt", "w")
    for x in fullLetterArray:
        file.write(x)
    file.close()
'''
Takes in the codearray and the decryptedtextfile as parameters.
Runs through the codearray, finding each letter for the code value based on their row. It then adds the code of the starting
letter of each row to the column number and finds the letter to that code. 
Has exceptions for \n and spaces.
It then writes the letter to the fullletterarray.
The writes each letter to the file.
'''
#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

def substitutionStringEncrypt(string):
    global alphabetArray, codeArray
    index=0
    encryptedStringArray=[]
    encryptedString=""
    alphabetArray=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                   "R", "S", "T", "U", "V", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
                   "h", "i", "j", "k", "l", "m", "n","o", "p", "q",
                   "r", "s", "t", "u", "v", "x", "y", "z", " ", ".", "?", ",", "!", "'", "\n"]
    codeArray=["z", "y", "x","w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h",
                    "g", "f", "e", "d", "?", "c", "b", "a", " ", "A", ".", "B", ",", "C", "'", "D", "E", "!", "F", "G", "H", "I",
                    "J", "K", "L", "M", "N", "O", "P", "Q",
                    "R", "S", "T", "U", "V", "X", "Y", "Z", "\n"]
    for letter in string:
        while letter!=alphabetArray[index]:
            index+=1
        encryptedStringArray.append(codeArray[index])
        index=0
    for x in encryptedStringArray:
        encryptedString+=x
    print(encryptedString)
    return encryptedStringArray

def substitutionStringDecrypt(encryptedStringArray):
    index=0
    decryptedStringArray=[]
    decryptedString=""
    for letter in encryptedStringArray:
        while letter!=codeArray[index]:
            index+=1
        decryptedStringArray.append(alphabetArray[index])
        decryptedString+=alphabetArray[index]
        index=0
    return decryptedString

#/////////////////////////////////////////////////////////////////////////////////////////////////////////////

def substitutionFileEncrypt(file):
    global alphabetArray, codeArray
    index=0
    encryptedStringArray=[]
    alphabetArray=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q",
                   "R", "S", "T", "U", "V", "X", "Y", "Z", "a", "b", "c", "d", "e", "f", "g",
                   "h", "i", "j", "k", "l", "m", "n","o", "p", "q",
                   "r", "s", "t", "u", "v", "x", "y", "z", " ", ".", "?", ",", "!", "'", "\n"]
    codeArray=["z", "y", "x","w", "v", "u", "t", "s", "r", "q", "p", "o", "n", "m", "l", "k", "j", "i", "h",
                    "g", "f", "e", "d", "?", "c", "b", "a", " ", "A", ".", "B", ",", "C", "'", "D", "E", "!", "F", "G", "H", "I",
                    "J", "K", "L", "M", "N", "O", "P", "Q",
                    "R", "S", "T", "U", "V", "X", "Y", "Z", "\n"]
    lines=[]
    line= file.readline()
    while line:
        lines.append(line)
        line= file.readline()
    file.close()
    for line in lines:
        for letter in line:
            while letter!=alphabetArray[index]:
                index+=1
            encryptedStringArray.append(codeArray[index])
            index=0
    file = open("encryptedtextfile.txt", "w")
    print(encryptedStringArray)
    for x in encryptedStringArray:
        file.write(str(x) + "\n")



def substitutionFileDecrypt(file):
    index=0
    encryptedStringArray = []
    line = file.readline()
    while line:
        encryptedStringArray.append(line.strip())
        line = file.readline()
    file = open("decryptedfile.txt", "w")
    for letter in encryptedStringArray:
        while letter!=codeArray[index]:
            index+=1
        file.write(alphabetArray[index])
        index=0
    file.close()



#/////////////////////////////////////////////////////////////////////////////////////////////////////////////
method = ""
while method != "STOP":
    method= str(input("Enter which method to cipher and decipher you would like to use. Enter STOP to stop.\n>"))
    if method.lower() == "string shift":
        originalString = str(input("Enter a string: "))
        shiftValue = int(input("Enter a shift value: "))
        endString = stringShift(originalString, shiftValue)
        print(endString)
        decryptedString = stringDecrypt(endString)
        print(decryptedString)
    elif method.lower() == "file shift":
        shiftValue = int(input("Enter a shift value: "))
        originalFile = open("ciphertextfile.txt", "r")
        fileShift(originalFile, shiftValue)
        encryptedFile = open("encryptedtextfile.txt", "r")
        fileDecrypt(encryptedFile)
    elif method.lower() == "rail cipher string":
        originalString = str(input("Enter a string to be encrypted: "))
        rows = int(input("Enter a number of rows for the rail cipher: "))
        fullStringArray = railEncryptString(originalString, rows)
        decryptedString = railDecryptString(fullStringArray)
        print(decryptedString)
    elif method.lower() == "rail cipher file":
        rows = int(input("Enter a number of rows for the rail cipher: "))
        file = open("ciphertextfile.txt", "r")
        railCipherFile(rows, file)
        file = open("encryptedtextfile.txt", "r")
        railCipherFileDecrypt(file)
    elif method.lower() =="polybius string cipher":
        string = str(input("Enter a string (only capitals or numbers): "))
        codeArray = polybiusStringCipher(string)
        fullLetterString = polybiusStringDecrypt(codeArray)
        print(fullLetterString)
    elif method.lower() == "polybius file cipher":
        file = open("polybiuscyphertext.txt", "r")
        polybiusFileEncrypt(file)
        file = open("encryptedtextfile.txt", "r")
        polybiusFileDecrypt(file)
    elif method.lower() == "substitution string cipher":
        string = str(input("Enter a string: "))
        encryptedStringArray = substitutionStringEncrypt(string)
        decryptedString = substitutionStringDecrypt(encryptedStringArray)
        print(decryptedString)
    elif method.lower() == "substitution file cipher":
        file = open("ciphertextfile.txt", "r")
        substitutionFileEncrypt(file)
        file = open("encryptedtextfile.txt", "r")
        substitutionFileDecrypt(file)