def getGuessedWord(secretWord, lettersGuessed):
	'''
	secretWord: string, the word the user is guessing
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters and underscores that represents
	what letters in secretWord have been guessed so far.
	'''
	tmpStr = ''
	for i in secretWord:
		if i in lettersGuessed:
			tmpStr += str(i)
		else:
			tmpStr += '_ '

	return tmpStr

secretWord = 'apple'
lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
print getGuessedWord(secretWord, lettersGuessed)

