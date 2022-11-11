# Program to find a number is odd or even
a  = int(input())
if a % 2 == 0:
	print('Even')
else:
	print('Odd')

#Program to find add or sub operator
b  = input()
if b  == '+':
	print('Add')
elif b == '-':
	print('Subtract')
else:
	print('Not sure')


#Program to find if a number is divisible by 2 and 3
a = int(input())

if a % 2 == 0 and a % 3 == 0:
	print('Yes')
else:
	print('No')


#Program to find if a number is divisible by 2 or 3
a = int(input())

if a % 2 == 0 or a % 3 == 0:
	print('Yes')
else:
	print('No')
