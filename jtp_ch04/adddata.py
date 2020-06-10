f = open("새파일.txt", 'a')
for i in range(11, 20):
    data = "%d번버내 줄입니다. \n" % i
    f.write(data)
f.close()


