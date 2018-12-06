#A'C + BC' + A'B = A'C + BC'  NEED TO ADD CC'
#AB + AC + B'C = AB + B'C NEED TO ADD BB'


# BB' + AB + B'C + AC
# B (B' + A) C +
# AC + BB' + AB + B'C

#New Data Structure
#
#
#
#

import re

potentialVarList = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

LS = input("enter left side no spaces")
RS = input("enter right side no spaces")

terms = LS.split("+")
varList = []

stepList = []
lastStep = LS

#given a letter add the steps necessary to add that ghost term
def addVar(letter):
    global lastStep
    stepList.append(lastStep + " + 0        RULE ")
    stepList.append(lastStep + " + " + letter + letter + "\'" + "       RULE")
    lastStep = lastStep + "+" + letter + letter + "\'"

#factor variables fully and show steps
#Input is in the form of a term list
def factor(stuff2factor):
    factorableVars = generateVarList(stuff2factor)

    rootVar = factorableVars[0]
    factorTerms = []

    for i in stuff2factor:
        if(rootVar in i):
            factorTerms.append(i)

    outputHalf = "(" + rootVar + "+"
    outputHalf2 = "("

    for i in factorableVars:
        for q in factorTerms:
            if(i in q and i != rootVar):
                outputHalf2 = outputHalf2+i+"+"


    outputHalf2 = re.sub(".$", ")", outputHalf2)

    for i in factorableVars:
        if(i not in outputHalf2 and i != rootVar):
            outputHalf = outputHalf + i + ")"

    stepList.append(outputHalf + outputHalf2 + "       RULE: DIST")

    return outputHalf + outputHalf2




#generates variables in a given term list
def generateVarList(stuff2GetVarsFrom):
    varList = []

    for i in stuff2GetVarsFrom:
        tempVar = ""

        for q in i:
            if (q in potentialVarList):
                if (tempVar != ""):
                    if (tempVar not in varList):
                        varList.append(tempVar)
                tempVar = q

            if ("\'" in q):
                tempVar = tempVar + "\'"
                if (tempVar not in varList):
                    varList.append(tempVar)

        if (tempVar not in varList):
            varList.append(tempVar)

    return varList

def generateCounterGhost(ghostLetter, variables):
    output = "("

#Isolate the variables
varList = generateVarList(terms)

#Determine variable that needs to be added
varToAdd = ""
numberOfVar = 0

tempL = "".join(varList)

for i in potentialVarList:
    if(tempL.count(i) > numberOfVar):
        numberOfVar = varList.count(i)
        varToAdd = i

#add that variable
addVar(varToAdd)
terms.append(varToAdd + varToAdd + "\'")
ghostLetter = varToAdd

varList = generateVarList([re.sub('[+)(]', "", factor(terms))])



#print the steps
for i in stepList:
    print(i)
