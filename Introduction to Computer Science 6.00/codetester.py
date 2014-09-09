high = 100
low = 0

print 'Please think of a number between '+str(low)+' and '+str(high)+'!'

while 1:
    middle = (high + low) / 2
    print 'Is your secret number '+str(middle)+'?'
    user_input = str(raw_input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. "))
    
    if user_input == 'h':
        high = middle
    elif user_input == 'l':
        low = middle
    elif user_input == 'c':
        print 'Game over. Your secret number was:', middle
        break
    else:
        print 'Sorry, I did not understand your input.'
    