a = 'hello'
b = 'hello'
print a is b
c = [1,2,3]
d = [1,2,3]
print c is d
e = c
c.pop()
print e
b = b[0:2]
print a is b