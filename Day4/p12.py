fhand = open('romeo.txt')
counts = dict()
fout = open('juliet.txt','w')
result = ' '
for line in fhand:
	line = line.rstrip()
	words = line.split(' ')
	for word in words:
		word = word.lower()
		if word not in counts:
			counts[word] = 1
		else:
			counts[word] += 1
for key in counts:
	line = key + ':  ' + str(counts[key]) + '\n'
	result += line
fout.write(result)
fout.close()
	# print key,counts[key]
