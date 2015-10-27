print ("Welcome to guess the number")

number = 10 

guess = int(raw_input("Enter a guess")); 

if guess < number:  
	print 'Nunmber too low'

elif guess > number:
	print 'Number too high'

else:
	print 'Correct'

