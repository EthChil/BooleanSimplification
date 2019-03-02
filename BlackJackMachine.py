# import random
#
# cards = 13
# deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
#
# def calcPossible(score):
#     max = 21 - score
#
#     possibleCards = 0
#
#     for i in deck:
#         if i <= max:
#             possibleCards += 1
#
#     if max >= 11:
#         possibleCards += 1
#
#     return float(possibleCards)
#
# while(True):
#     dealer = int(raw_input("dealer: "))
#     you = int(raw_input("you: "))
#
#     if dealer > you:
#         print("UR LOWER EXECUTE")
#     else:
#         print("DEALER: " + str((calcPossible(dealer) / 13.0)*100))
#         print("YOURS: " + str((calcPossible(you) / 13.0)*100))
#         if calcPossible(you) > calcPossible(dealer) and (calcPossible(you)/13)*100 < 100:
#             print("VERDICT EXECUTE IT")
#         else:
#             print("naw fam")
#
#
#
import copy

listInput = raw_input("Enter a list element seperated by a space ")
listunsorted = listInput.split()
sortedList = listunsorted.copy()
sortedList = sortedList.sort()

def is_sorted ():
    if listunsorted == sortedList:
        return True
    else:
        return False


print (is_sorted ())
