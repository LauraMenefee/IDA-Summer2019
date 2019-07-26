'''
Simple Eliza Program
Imersion Data Analytics - Summer 2019
Laura Menefee

Assignment from Canvas....
You will be creating an interactive chat-bot type program. Eliza is a therapist program 
that interacts with the user. Your program will need to evaluate what the user asks and 
turn the user's input into a question that sounds like the therapist really cares.

Your first task is to develop a program with a running loop. If the user types in "I am feeling great" 
or enter "Q", the program will stop running. Your program should print out the last input (as an output)
 every time before accepting new input. Make sure you are accommodating for NO case-sensitivity. 
 (Q is the same as q)

''' 

prompt = "Good Day.  What is your problem? "
prompt += "Enter your respone here or Q to quit: "
	
answer = ''	
	
while answer.lower() != 'q':
	answer = input(prompt)
	print(answer)
	prompt = "Enter your respone here or Q to quit: "
	