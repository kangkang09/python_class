email = 'wky@163.com'
index = email.find('@')
username = email[0:index]
# print username
domain = email[index+1:]
print domain