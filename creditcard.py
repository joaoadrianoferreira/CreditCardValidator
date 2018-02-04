import sys
import os

os.system('clear') 
print "This software can be used to Validate Credit Card Number"
print "This validator use the Luhn Algorithm"

# Input of type of credit card
while True: 
	type_of_credit_card = raw_input('Select Option:\n1: American Express\n2: Master Card\n3: Visa\n')
	if type_of_credit_card == '1':
		lenght = 15
		break
	elif type_of_credit_card == '2':
		lenght = 16
		break
	elif type_of_credit_card == '3':
		lenght1 = 13
		lenght2 = 16
		break
	os.system('clear') 

# Input of credit card number 
while True:	
	number_of_credit_card = raw_input('Insert credit card number without spaces: ')
	if type_of_credit_card == '1' or type_of_credit_card == '2':
		if len (number_of_credit_card) == lenght:
			break
	elif type_of_credit_card == '3': 
		if len (number_of_credit_card) == lenght1 or len (number_of_credit_card) == lenght2:
			break 

# Reverse the credit card number and creates a list of digits 
inverse_number = number_of_credit_card[::-1]
lst_of_digits = [int(x) for x in inverse_number]

# From the rightmost digit, which is the check digit, and moving left, double the value of every second digits
x = 0
while x < len(lst_of_digits):
	if x % 2 != 0:
		lst_of_digits[x] = lst_of_digits[x] * 2
		if lst_of_digits[x] >= 10:
			str_num = str(lst_of_digits[x])
			y1 = str_num[0]
			y2 = str_num[1]
			y = int(y1) + int(y2)
			lst_of_digits[x] = y
	x += 1

# Sum all values from de lst_of_digits 
sum_value = 0
for num in lst_of_digits:
	sum_value += int(num)

# Validate credit card number s
if sum_value  % 10 == 0:
	print "Your Credid Card Number is Valid"
else: 
	print "Your Credid Card Number is Invalid"
print "Thanks for using this software"

# Terminate the program
sys.exit()