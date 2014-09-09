##
## Longest Alpha. String
## Problem Set 1 Question 3
##

## Finds the longest sub string of alphabetical
## letters and returns it.
def longAlphaString(s, debug = False):
    tmpListA = []
    tmpStr = ''

    for i in range(0, len(s)):
        if len(s)-1 > i and s[i] <= s[i+1]:
            tmpStr += s[i]
        else:
            tmpStr += s[i]
            tmpListB = []
            tmpListB.append(tmpStr)
            tmpListB.append(len(tmpStr))
            tmpListA.append(tmpListB)
            tmpStr = ''

    save = 0
    for item in tmpListA:
        if item[1] > save:
            save = item[1]
            tmpStr = item[0]

    if debug == True:
        print 'Longest substring in alphabetical order is:', tmpStr

    return tmpStr