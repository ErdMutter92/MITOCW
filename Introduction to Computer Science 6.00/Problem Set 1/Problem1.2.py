##
##  Count the 'bob's
##  Problem Set 1 Question 2
##

## Counts the accurences of the string 'bob'
## within a given string.
def countBob(s, debug = False):
    count = 0
    for char in range(0, len(s)):
        ## Makes sure there are enough chars remaing to
        ## conduct the test.
        if (len(s) - i) >= 3:
            if s[char] == 'b':
                if s[char] == 'b':
                    if s[char] == 'b':
                        count += 1

    if debug == True:
        print 'Number of times bob occurs is:', count
    
    return count