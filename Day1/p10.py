import random
# for i in range(10):
# 	print random.random()
ans = random.randint(1,100)
count = 0
money = 100
while(True):
	if money < 10:
		print 'you lose! '
		break
	a = int(raw_input('enter your answer '))
	if a > int(ans):
		print 'too big '
		count += 1
		money -= 10
	elif a < int(ans):
		print 'too small'
		count += 1
		money -= 10
	else:
		count += 1
		money += 100
		print 'you win! you spent ' + str(count) + ' times. your money is ' + str(money) + ' .'
		break
	