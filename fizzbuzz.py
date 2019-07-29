"""
Immersive Data Analytics
Laura Menefee

Fizz Buzz assignment

From Canvas....
Write a program that prints the numbers from 1 to 100.
For multiples of 3 print “Fizz” instead of the number.
For the multiples of five print “Buzz”.
For numbers which are multiples of both 3 and 5 print “FizzBuzz”.

"""



for number in range(1, 101):

	if number%3 == 0 and number%5 == 0:
		print("FizzBuzz")
		
	elif number%3 == 0:
		print("Fizz")
		
	elif number%5 == 0:
		print("Buzz")
		
	else:
		print(number)
		
	

