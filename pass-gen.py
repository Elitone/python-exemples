import random, string

upper = string.ascii_uppercase
lower = string.ascii_lowercase
digits = string.digits
lis = [upper, lower, digits]

def rlistchoice(lis):
	# Random selection of list
	for n in range(len(lis)):
		return random.choice(lis)

def addspecial(lis):
	# Add special char to lis
	special = "{(&§!)}[]?$€£^<>"
	lis.append(special)

def newpassword(lis):
	# Create new password
	print('Remember: Strong password must be more then 6 char\n')
	lenght = int(input('Chois the lenght: '))
	aspecial = input('Add special char? [y-n]: ')

	if aspecial == 'y' or aspecial == 'Y':
		addspecial(lis)
		print('[*] Special char selected')
	else:
		print('[!] Special char not selected')

	# Generate new password
	password = ''
	for i in range(lenght):
		password += random.choice(rlistchoice(lis))
	print('\npassword = ' + password)

if __name__ == '__main__':
	newpassword(lis)