#one more try
#Prime Number assignment
'''
From Canvas....
A prime number is a number that has only itself and 1 as a factor. 
This means that for each of the numbers from 2 to that number, 
the number cannot be divided without a remainder. 
For example, 9 is not a prime number because it can be divided by 3 without 
a remainder. But 7 is a prime number because it cannot be divided by 2, 3, 4, 5, 
or 6 without a remainder. Write an appliation that will that show a list of 
numbers and indicate whether or not they are prime.
The user will have to input the last number in the range, and you will print 
all of the numbers from 1 to that number. 
'''


#prompt for last prime number to check
last_check_prime = int(input("Enter last number in range to check for prime: "))

	#print(last_check_prime)


#Run this for loop for each number starting at 2, upto the last prime number inputed.
# This loop will run for each num that is to be checked if it a prime number, up to 
# the upper number inputed (last_check_prime) by the user.

for that_num in range(2, last_check_prime + 1):
	#Initail prime_flg is true, assue it is untile found out otherwise 
	prime_flg = True

	#For each that_num divide by 2 until that_num to find out if there is not 
	# a remainder, then it is not a prime and reset flag to not a prime.  
	for number in range(2, that_num):
		#print( "number: "+ str(number) +" "+ "that_num: " + str(that_num))
		if that_num%number==0:
		#if any any point, there is not a remainder, this is not a 
		#prime number because the loop is going up to but not including
		#that number
			prime_flg = False
			#print(prime_flg)

	if prime_flg == False:
		print("    "+str(that_num) + " Is NOT a prime number")
	else:
		print("    "+ str(that_num) + " Is a prime number")

	
	
	