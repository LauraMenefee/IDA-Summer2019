'''
Calculate Employee Payroll

Laura Menefee
Immersive Data Analytics - Summer 2019
7/26/2019


This program calculates employee pay. An employee pay is calculated by pay rate * hours worked.
Every hour worked, over 40 hours, is calculated with 1.5 * pay rate.

For each employee their name and calculated pay is printed.

Payroll information is inside a dictionary containing a dictionary.
1st key is the employee number and then value pair is a dictionary with
the needed employee information in in key value pairs.

'''
## Create employee payroll dictionary

payroll_dict = {
					'001': {'name': 'Mary', 'pay_rate':15.00,'hrs_wrked':40 },
					'002': {'name': 'John', 'pay_rate':22.00,'hrs_wrked':25 },
					'003': {'name': 'Bob', 'pay_rate':35.00,'hrs_wrked':4 },
					'004': {'name': 'Mel', 'pay_rate':43.00,'hrs_wrked':62 },
					'005': {'name': 'Jen', 'pay_rate':17.00,'hrs_wrked':33 },
					'006': {'name': 'Sue', 'pay_rate':29.00,'hrs_wrked':45 },
					'007': {'name': 'Ken', 'pay_rate':40.00,'hrs_wrked':36 },
					'008': {'name': 'Dave', 'pay_rate':20.00,'hrs_wrked':17 },
					'009': {'name': 'Beth', 'pay_rate':37.00,'hrs_wrked':37 },
					'010': {'name': 'Ray', 'pay_rate':16.50,'hrs_wrked':80 }
				}
							

#print(payroll_dict)							

#loop thru each employees info and set data in variables
for emp_no, emp_info in payroll_dict.items():

	# Get emp info in variables
	fname = emp_info['name']
	hourly_rate = float(emp_info['pay_rate'])
	hours_worked = float(emp_info['hrs_wrked'])

	# calc salary
	# If employee worked less than or equal to 40 hours calc salary and print
	if hours_worked <= 40:
		salary = ( hourly_rate * hours_worked )
		print(f"\t{fname} has earned ${salary} this week")
	else:
	# If employee worked overtime calc regular salary and overtime salary and print
		salary = (( hourly_rate * 40 ) + (( hourly_rate * 1.5) * ( hours_worked - 40)))
		print(f"\t{fname} has earned ${salary} this week, this includes overtime pay!")

	
print("\nNo more employee's to calculate pay for. ")



	




