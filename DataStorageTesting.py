import re

alphabet = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

booleanStatement = input("Enter Boolean Statement in the form of sum of products")

booleanStatement = booleanStatement.replace(" ", "")
terms = booleanStatement.split("+")

statement = []

for term in terms:
    tempArr = []
    for var in range(len(term)):
        if(len(term)-1 > var and term[var+1] == "'"):
            for i in range(alphabet.index(term[var])):
                if(tempArr[i] == None):
                    tempArr.append(0)
            tempArr[alphabet.index(term[var])] = -1
        elif(alphabet.count(term[var]) > 0):
            for i in range(alphabet.index(term[var])+1):
                if(len(tempArr) == i):
                    tempArr.append(0)
            tempArr[alphabet.index(term[var])] = 1

    statement.append(tempArr)

print(statement)