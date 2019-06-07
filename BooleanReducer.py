import time
import numpy as np
import itertools

#TODO: compare speed difference of map(abs, arr) vs np.abs(arr)
#TODO: look into the int8 stuff for numpy array
#TODO: print the total overlaps at every step and the TQs
#TODO: render truth tables
#TODO: New class to generate all boolean expressions

class generateExpressions:
    container = np.array([])

    def __init__(self, varCount):
        self.truthTable = []
        self.curExp = []
        self.varCount = varCount


    def genTruthTable(self):
        self.truthTable = list(itertools.product([False, True], repeat=self.varCount))

    def solve(self):
        for i in range(pow(2, pow(2, self.varCount))):
            print("gang")
            #generate current expression


    def simplifySet(self):
        print("ba")


booleanStatement = input("Enter Boolean Statement in the form of sum of products")

#A'B'D'E'F'+A'B'CD'E'+A'CD'E'F+A'BCD'F+A'BD'EF+A'BC'D'E+BC'D'EF'


class Statement:
    nDiscreteVars = 0
    highestVar = 0
    container = np.array([])
    childerhoseLiuMap = np.array([])
    tags = []
    raw = ""

    verbose = False
    trivial = False

    def __init__(self, rawString, modifiers, discreteVars):

        if("-t" in modifiers):
            self.trivial = True
        if("-v" in modifiers):
            self.verbose = True

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
                    #
                    # #Calc nDiscreteVars
                    # for i in range(ord(term[var])-64):
                    #     if(len(regArr) == i):
                    #         regArr.append(0)
                    # if(regArr[ord(term[var]) - 65] == 0):
                    #     regArr[ord(term[var]) - 65] += 1

        # #calc the quantity of discrete vars
        # self.nDiscreteVars = sum(map(abs, regArr))
        self.nDiscreteVars = discreteVars

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

        #do a trivial solve to merge simple groupings (Optional)
        if(self.trivial):
            self.trivialSolve()

    #calculate the quantity of 1s that make up a given term (2^discrete variables - )
    def calculateGroupSize(self, varIn):
        return pow(2, self.nDiscreteVars - sum(map(abs, varIn)))


    def calculateOverlapNum(self, arr1, arr2):
        product = np.multiply(arr1, arr2)

        if(-1 in product):
            return 0
        else:
            sub = np.abs(np.subtract(arr1, arr2))

            output = self.nDiscreteVars - (sum(sub) + sum(product))
            return pow(2, output)


    def printChilderhoseLiuMap(self):
        terms = "a"
        for i in self.tags:
            if(terms == "a"):
                terms = i
            else:
                terms = terms + "+" + i
        print("ChilderhoseLiu Mapping of " + terms)
        print("".ljust(10), end ="")
        for i in self.tags:
            print(i.ljust(10), end ="")

        print("")


        for term1Ptr in range(len(self.container)):
            print(self.tags[term1Ptr].ljust(10), end ="")
            for term2Ptr in range(len(self.container)):
                if (term2Ptr != term1Ptr):
                    print(str(self.calculateOverlapNum(self.container[term1Ptr], self.container[term2Ptr])).ljust(10), end ="")
                else:
                    print("X".ljust(10), end ="")

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

    def findGhost(self, TQ, BL):
        ghostNum = 1000
        tailNum = -1000
        ghost = 0
        tail = 0

        for i in range(len(TQ)):
            if(i not in BL):
                if TQ[i] < ghostNum:
                    ghostNum = TQ[i]
                    ghost = i
                if TQ[i] > tailNum:
                    tailNum = TQ[i]
                    tail = i

        if (abs(self.childerhoseLiuMap[tail][ghost]) + abs(self.childerhoseLiuMap[ghost][tail]) == 2):
            return ghost
        else:
            if(TQ[ghost] <= 0):
                BL.append(tail)
                return self.findGhost(TQ, BL)
            else:
                BL.append(ghost)
                return self.findGhost(TQ, BL)

    def removeGhostTerm(self):
        TQ = []
        BL = []

        self.childerhoseLiuMap = self.generateChilderhoseLiuMap()

        for row in range(len(self.childerhoseLiuMap)):
            TQ.append(self.generateTailQuotient(self.childerhoseLiuMap[row], self.container[row]))

        #if all of the TQs are above 0 then exit
        endCond = True
        for q in TQ:
            if(q <= 0):
                endCond = False

        if(endCond):
            return

        #remove term, it isn't a ghost or tail
        for q in range(len(TQ)):
            if(TQ[q] == self.calculateGroupSize(self.container[q])):
                BL.append(q)

        #end condition all TQs are equal
        if(len(BL) > 0):
            firstNum = 0
            started = False
            doExit = True

            for i in range(len(TQ)):
                if(i not in BL):
                    if(started == False):
                        firstNum = TQ[i]
                        started = True
                    elif(firstNum != TQ[i]):
                        doExit = False
            if(doExit):
                return
        else:
            if(TQ.count(TQ[0]) == len(TQ)):
                return

        ghost = self.findGhost(TQ, BL)

        self.childerhoseLiuMap = np.delete(self.childerhoseLiuMap, ghost, axis=0)
        self.childerhoseLiuMap = np.delete(self.childerhoseLiuMap, ghost, axis=1)
        del self.tags[ghost]
        self.container = np.delete(self.container, ghost, axis=0)

        if(self.verbose):
            self.printChilderhoseLiuMap()

        self.removeGhostTerm()

    def trivialSolve(self):
        set = self.container

        for term1 in range(len(set)):
            for term2 in range(term1, len(set)):
                if(not np.array_equal(set[term1], set[term2])):
                    if(sum(np.subtract(np.abs(set[term1]), np.abs(set[term2]))) == 0):
                        if(1 not in np.abs(np.add(set[term1], set[term2])) and sum(np.abs(np.add(set[term1], set[term2]))) + 2 == sum(np.abs(set[term1]))*2):
                            print("Merging " + self.tags[term1] + " and " + self.tags[term2], end ="")
                            self.container[term1] = np.divide(np.add(set[term1], set[term2]), 2)
                            self.container = np.delete(self.container, term2, axis=0)
                            del self.tags[term2]
                            self.tags[term1] = self.genTermText(self.container[term1])
                            print("into " + self.tags[term1])

                if(term1 != term2 and np.array_equal(set[term1], set[term2])):
                    print("Removed duplicate " + self.tags[term1])
                    self.container = np.delete(self.container, term2, axis=0)
                    del self.tags[term2]



    def genTermText(self, term):
        output = ""

        for i in range(len(term)):
            if(term[i] != 0):
                output = output + chr(65 + i)
            if(term[i] == -1):
                output = output + "'"

        return output






#MAIN PROGRAM

#AB     [1,1,0]
#BC     [0,1,1]
#A'C    [-1,0,1]
#A'B' + C'D'A' + C'D'B + C'AB + AC'D + B'C'D = A'B' + C'D'B + AC'D
#AB + BC + A'C

#A'B'C+A'CE+A'CDE+BD'+ABC'+ABCE+ABDE+ACDE
#D'B + A'B'C + ABC' + A'CE + CDE + EABC + ABDE (merged no trivial)
#D'B + A'B'C + ABC' + A'CE + ACDE + EABC + ABDE + A'CDE

if(input("b for bool, g to gen truth table") == "g"):
    exp = generateExpressions(3)
    exp.genTruthTable()
    exp.solve()

else:
    booleanStatement = input("Enter Boolean Statement in the form of sum of products")
    discVar = input("Input Number of Discrete Variables")

    stat = Statement(booleanStatement, "-verbose -trivial", discVar)
    stat.printChilderhoseLiuMap()

    stat.trivialSolve()

    stamp = time.time()

    stat.removeGhostTerm()
    stat.printChilderhoseLiuMap()

    timeTook = (time.time() - stamp)*1000000000

    print("NS = " + str(timeTook))

    #0.25 ns per cycle
    print("At 3ghz that is " + str((round(timeTook/0.25))) + " Processor Cycles")
    print(str(round(timeTook/0.25)))
