def reverse_string(s):
	return s[::-1]
# print reverse_string(s)
def reverse_string2(s):
	length = len(s)
	if length < 1:
		return ''
	i = length -1
	result = ''
	while i >= 0:
		result += s[i]
		i -= 1
	return result
while(True):
	s = raw_input('enter your word ')
	if s == 'done':
		break
	else:
		print reverse_string2(s)

