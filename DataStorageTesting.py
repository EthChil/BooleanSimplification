import re
import numpy as np


booleanStatement = raw_input("Enter Boolean Statement in the form of sum of products")


class Statement:
    nDiscreteVars = 0
    highestVar = 0
    container = np.array([])
    childerhoseLiuMap = np.array([])
    tags = []
    raw = ""

    def __init__(self, rawString):

        #split and strip input
        rawString = rawString.replace(" ", "")
        terms = rawString.split("+")
        self.tags = terms
        self.raw = rawString

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
            return pow(2, self.nDiscreteVars - (sum(np.abs(np.subtract(arr1, arr2))) + sum(product)))

    def printChilderhoseLiuMap(self):
        print("ChilderhoseLiu Mapping of " + self.raw)
        print("").ljust(10),
        for i in self.tags:
            print(i).ljust(10),
        print("")


        for term1Ptr in range(len(self.container)):
            print(self.tags[term1Ptr]).ljust(10),
            for term2Ptr in range(len(self.container)):
                if (term2Ptr != term1Ptr):
                    print(str(self.calculateOverlapNum(self.container[term1Ptr], self.container[term2Ptr]))).ljust(10),
                else:
                    print("X").ljust(10),
            print("")


    def generateChilderhoseLiuMap(self):
        self.childerhoseLiuMap = np.array(np.zeros((len(self.container), len(self.container)), np.int8))

        for term1Ptr in range(len(self.container)):
            for term2Ptr in range(len(self.container)):
                if (term2Ptr != term1Ptr):
                    self.childerhoseLiuMap[term1Ptr][term2Ptr] = self.calculateOverlapNum(self.container[term1Ptr], self.container[term2Ptr])

        return self.childerhoseLiuMap

    def generateTailQuotient(self, row, term):
        return self.calculateGroupSize(term) - sum(row)

    def removeGhostTerm(self):

        ghostNotFound = True;
        ghostNum = 1000
        tailNum = -1000
        ghost = 0
        tail = 0

        while(ghostNotFound):

            for row in self.childerhoseLiuMap:
                tempOut = self.generateTailQuotient(row, self.container[index(row)])
                if()

            tail = self.generateTailQuotient()
            ghost

            print(tail)
            print(ghost)

            if(2 in np.add(np.abs(self.childerhoseLiuMap[tail]), np.abs(self.childerhoseLiuMap[ghost]))):
                ghostNotFound = False

        print(tail)
        print(ghost)



#MAIN PROGRAM

#AB     [1,1,0]
#BC     [0,1,1]
#A'C    [-1,0,1]
#A'B' + C'D'A' + C'D'B + C'AB + DAB

stat = Statement(booleanStatement)
stat.printChilderhoseLiuMap()
stat.generateChilderhoseLiuMap()
stat.removeGhostTerm()

