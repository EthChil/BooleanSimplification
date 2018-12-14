import re
import numpy as np

alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U",
            "V", "W", "X", "Y", "Z"]

booleanStatement = raw_input("Enter Boolean Statement in the form of sum of products")

booleanStatement = booleanStatement.replace(" ", "")
terms = booleanStatement.split("+")

statement = []

for term in terms:
    tempArr = []
    for var in range(len(term)):
        if (len(term) - 1 > var and term[var + 1] == "'"):
            for i in range(alphabet.index(term[var]) + 1):
                if (len(tempArr) == i):
                    tempArr.append(0)
            tempArr[alphabet.index(term[var])] = -1
        elif (alphabet.count(term[var]) > 0):
            for i in range(alphabet.index(term[var]) + 1):
                if (len(tempArr) == i):
                    tempArr.append(0)
            tempArr[alphabet.index(term[var])] = 1

    statement.append(tempArr)

print(statement)




def multiplyArrays(arr1, arr2):
    return [arr1 * arr2 for arr1, arr2 in zip(arr1, arr2)]

def generateChilderhoseLiuTable(input):
    CLTable = []

    for x in input:
        tempArr = []
        for y in input:
            if(x == y):
                tempArr.append(0)
            else:
                n = multiplyArrays(x, y)
                if(-1 in n):
                    tempArr.append(0)
                else:
                    print("")






