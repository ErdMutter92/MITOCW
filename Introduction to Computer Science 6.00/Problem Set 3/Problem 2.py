def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''

    foundLetterCount = 0

    for i in secretWord:
        if i in lettersGuessed:
            foundLetterCount += 1
            
    if len(secretWord) == foundLetterCount:
        return True
    else:
        return False

print isWordGuessed('coconut', ['z', 'x', 'q', 'c', 'o', 'c', 'o', 'n', 'u', 't'])
