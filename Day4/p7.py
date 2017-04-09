fhand = open('data.txt','r')
emails =[]
result_string = ''
fout = open('output.txt','w')
for line in fhand:
	if line.startswith('From:'):
		line = line.rstrip()
		array = line.split('From: ')
		email = array[1]
		if email not in emails:
			emails.append(email)
for email in emails:
	# print email
	line = email + '\n'
	result_string += line
fout.write(result_string)
fout.close()
