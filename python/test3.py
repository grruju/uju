f = open('test.txt', 'r')
body = "Life is too short you need java"
print(body)
f.close()

body = body.replace("java","python")

f = open('test.txt','w')
f.write(body)
print(body)
f.close()
