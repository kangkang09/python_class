sum = 0
while(True):
	a = raw_input('enter your number ')
	if a == 'done':
		break
	if a[0] == '#':
		continue
	sum += int(a)
	print sum

