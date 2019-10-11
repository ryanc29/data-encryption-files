def simpleDecimalToBinary(file):
    lines = []
    binaryCodes =[]
    line = file.readline()
    while line:
        lines.append(line)
        line = file.readline()
    file.close()
    for x in lines:
        for letter in x:
            binaryCodes.append(bin(ord(letter)))
    file = open("binaryTextCyphered.txt", "w")
    for x in binaryCodes:
        file.write(x + "\n")
    file.close()
'''
Takes in the file binaryText.txt as a parameter.
Reads the file, appends the characters to the lines array.
Goes through the lines, goes through each letter in the line. 
It appends the binary code of the character code of the letter to the binaryCodes array.
Opens the binaryTextCiphered.txt file.
Writes all the binaryCodes elements to the binaryTextCiphered.txt file.
'''

def simpleBinarytoDecimal(file):
    lines = []
    line = file.readline()
    while line:
        lines.append(line.strip())
        line = file.readline()
    file.close()
    file = open("binaryTextDecyphered.txt", "w")
    for code in lines:
        file.write(chr(int(code, 2)))
    file.close()
'''
Takes in the binaryTextCiphered.txt file as a parameter. 
Reads the file, appending the codes without the \n to the lines array.
Opens the binaryTextDecyphered.txt file.
Goes through the codes in the lines array.
Writes the code of the integer that is equal to the binary code from the array. I have the , so it knows it is in binary.
'''



file = open("binaryText.txt", "r")
simpleDecimalToBinary(file)
file = open("binaryTextCyphered.txt", "r")
simpleBinarytoDecimal(file)
#bin(ord(ascii))
#str(chr(int(binary, 2)))
'''
Opens the binaryText.txt file. 
Runs the simpleDecimalToBinary function.
Opens the binaryTextCyphered.txt file
Runs the simpleBinarytoDecimal function
'''

