def myfunction(n):
	if int(n) >= 90:
		print 'A'
	elif 80 <= int(n):
		print 'B'
	elif 70 <= int(n):
		print 'C'
	elif 60 <= int(n):
		print 'D'
	else:
		print 'F'

a = 50
b = 75
c = 95
array = [a,b,c]
for num in array:
	myfunction(num)