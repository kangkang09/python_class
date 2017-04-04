name = raw_input('what is your name? ')
ans = 'hello ' + name
print ans
age = int(raw_input('how old are you? '))
if age < 18:
	print 'sorry, you can come here when you grow up.'
else:
	a = int(raw_input('our price is 5 for each, how many do you want? '))
	b = 5
	c = str(a*b)
	print 'you need to pay ' + c + ' dollars.'