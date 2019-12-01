# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
import sys
import os

def intStringToList(sl):
    newList = [int(x) for x in sl.split()]
    newList.sort()
    return newList

def getMean(numList):
    return (sum(numList)/len(numList))

def getMedian(numList,listLength):
    if listLength % 2 == 1:
        return numList[int((listLength-1)/2)]
    else:
         return ((numList[int(listLength/2)-1] + numList[int(listLength/2)])/2)

def getMode(numList):
    max = 0 
    s = set(numList)
    numDict = {i : 0 for i in s}
    for x in range(len(numList)):
        if numList[x] in numDict:
            numDict[numList[x]] = numDict.get(numList[x]) + 1
        if numDict[numList[x]] > max:
            max = numDict[numList[x]]
    modes = []
    for y in numDict:
        if numDict[y] == max:
            modes.append(y)

    return min(modes)

# SD = (((x1-m)**2+(x2-m)**2+(x3-m)**2+(x4-m)**2+...(xN-m)**2))/N)**0.5
def getStandDiv(numList,listLength,listMean):
    sum = 0
    for x in range(len(numList)):
        sum += ((numList[x]-listMean)**2)
    
    return round(((sum/listLength)**0.5),1)

def printUpperLowerCI(standardDiv,mean,length):
    upper = str(round((mean + 1.96*(standardDiv/math.sqrt(length))),1))
    lower = str(round((mean - 1.96*(standardDiv/math.sqrt(length))),1))
    print(lower + " " + upper)

if __name__ == "__main__":
    length = int(input())
    inputString = input()
    numbers = intStringToList(inputString)

    mean = getMean(numbers)
    print(mean)
    print(getMedian(numbers,length))
    print(getMode(numbers))
    stanDiv = getStandDiv(numbers,length,mean)
    print(stanDiv)
    printUpperLowerCI(stanDiv,mean,length)