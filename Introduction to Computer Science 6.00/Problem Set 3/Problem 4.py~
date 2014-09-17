def getAvailableLetters(lettersGuessed):
	import string
	'''
	lettersGuessed: list, what letters have been guessed so far
	returns: string, comprised of letters that represents what letters have not
	yet been guessed.
	'''

	tmpStr = ''

	alpha = string.ascii_lowercase
	lettersGuessed.sort()
	for i in alpha:
		if i not in lettersGuessed:
			tmpStr += i
	return tmpStr

lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
getAvailableLetters(lettersGuessed)
