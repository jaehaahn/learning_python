f = open('test.txt', 'r')
body = f.read()
f.close

body = body.replace('python', 'java')

f = open('test.txt', 'w')
f.write(body)
f.close()
