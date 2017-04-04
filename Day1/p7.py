name = raw_input('what is your name? ')
ans = 'hello ' + name
print ans
hours = int(raw_input('how many hours did you work this week? '))
if hours < 40:
	b = 20
	c = str(b*hours)
	print 'your salary is 20 dollars per hour, your total salary is ' + c + '.'
else:
	d = 800
	e = hours - 40
	f = 60*e
	g = str(d+f)
	print 'your salary is 20 dollars per hour, and the salary of over-time work is the triple price, so your total salary is ' + g +'.'