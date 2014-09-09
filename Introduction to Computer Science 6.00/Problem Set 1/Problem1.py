##
##  Count the Vowels
##  Problem Set 1 Question 1
##

## Counts the number of vowels (excluding y) in a given
## String. Returns Int.
def countVowels(s, debug = False):
    count = 0
    for i in s:
        if i in 'aeiou':
            count += 1

    if debug == True:
        print 'Number of vowels:', count
    
    return count
