s = 'hello'
t = list(s)
# print t
t.append('a')
# print t
t2 = ['w','a']
# t.append(t2)
t += t2
popped_val = t.pop(1)
print popped_val
print t
del t[0]
print t