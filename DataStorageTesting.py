import re
import numpy as np


booleanStatement = raw_input("Enter Boolean Statement in the form of sum of products")


class Statement:
    nDiscreteVars = 0
    highestVar = 0
    container = np.array([])
    childerhoseLiuMap = np.array([])

    def __init__(self, rawString):

        #split and strip input
        rawString = rawString.replace(" ", "")
        terms = rawString.split("+")

        #temp arr
        regArr = []

        #determine discrete vars and the highest var
        for term in terms:
            for var in range(len(term)):
                if("'" not in term[var]):
                    #check to see if it's the biggest
                    if(ord(term[var])-64 > self.highestVar):
                        self.highestVar = ord(term[var]) - 64

                    #Calc nDiscreteVars
                    for i in range(ord(term[var])-64):
                        if(len(regArr) == i):
                            regArr.append(0)
                    if(regArr[ord(term[var]) - 65] == 0):
                        regArr[ord(term[var]) - 65] += 1

        #calc the quantity of discrete vars
        self.nDiscreteVars = sum(map(abs, regArr))

        #build numpy container
        self.container = np.array(np.zeros((len(terms), self.highestVar),np.int8))

        #populate numpy array
        for i in range(len(terms)):
            for q in range(len(terms[i])):
                if(terms[i][q] != "'"):
                    if (len(terms[i]) - 1 > q and terms[i][q + 1] == "'"):
                        if(self.container[i][ord(terms[i][q])-65] == 0):
                            self.container[i][ord(terms[i][q])-65] = -1;
                    else:
                        if (self.container[i][ord(terms[i][q])-65] == 0):
                            self.container[i][ord(terms[i][q])-65] = 1;

    def calculateGroupSize(self, varIn):
        return pow(2, self.nDiscreteVars - sum(map(abs, varIn)))

    def calculateOverlapNum(self, arr1, arr2):
        product = np.multiply(arr1, arr2)

        if(-1 in product):
            return 0
        else:
            return pow(2, self.nDiscreteVars - (sum(np.abs(np.subtract(np.abs(arr1), np.abs(arr2)))) + sum(product)))

    def printChilderhoseLiuMap(self):
        tempArr = np.array(np.zeros((self.nDiscreteVars, self.nDiscreteVars), np.int8))

        for term1Ptr in range(len(self.container)):
            for term2Ptr in range(len(self.container)):
                if (term2Ptr != term1Ptr):
                    tempArr[term1Ptr][term2Ptr] = self.calculateOverlapNum(self.container[term1Ptr], self.container[term2Ptr])

        print(tempArr)


    def generateChilderhoseLiuMap(self):
        self.childerhoseLiuMap = np.array(np.zeros((self.nDiscreteVars, self.nDiscreteVars), np.int8))

        for term1Ptr in range(len(self.container)):
            for term2Ptr in range(len(self.container)):
                if (term2Ptr != term1Ptr):
                    self.childerhoseLiuMap[term1Ptr][term2Ptr] = self.calculateOverlapNum(self.container[term1Ptr], self.container[term2Ptr])

        return self.childerhoseLiuMap

    #def generateTailQuotient(self):



#AB     [1,1,0]
#BC     [0,1,1]
#A'C    [-1,0,1]

[0, 1, 0]
[1, 0, 1]

[0, 0, 1]
[1, 1, 0]


stat = Statement(booleanStatement)
print(stat.generateChilderhoseLiuMap())
stat.printChilderhoseLiuMap()


'''
for term in terms:
    tempArr = []
    for var in range(len(term)):
        #if the var is complimented
        if (len(term) - 1 > var and term[var + 1] == "'"):
            for i in range(ord(term[var]) - 64):
                if (len(tempArr) == i):
                    tempArr.append(0)
            tempArr[ord(term[var]) - 65] = -1
        #if the var isn't complimented
        elif (ord(term[var]) - 65 > 0):
            for i in range(ord(term[var]) - 64):
                if (len(tempArr) == i):
                    tempArr.append(0)
            tempArr[ord(term[var]) - 65] = 1


    statement.append(tempArr)
print(statement)

npArr = np.array(statement, np.int8)
print(statement)


arr3 = np.array([1, 2, 3, 4])

arr3 = np.pad(arr3, (3, 3), 'constant')

print(arr3)

print(np.add(arr3[0], arr3[1]))

'''