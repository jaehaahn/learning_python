Last login: Wed May 20 21:59:09 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# 
(base) [root@ip-172-31-23-187 learning_python]# 
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 4 root root  148 May 20 22:03 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = 123
>>> a = -178
>>> a = 0
>>> 
>>> a = 1.2
>>> a = -3.45
>>> 
>>> a = 4.2E10
>>> a = 4.24e-10
>>> 
>>> a = Oo177
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>

NameError: name 'Oo177' is not defined
>>> a = 0o177
>>> a = 0O177
>>> 
>>> a = 0x8ff
>>> a = 0xABC
>>> 
>>> a = 3
>>> b = 4
>>> a ** b
81
>>> 7 % 3
1
>>> 3 % 7
3
>>> 7/4
1.75
>>> 7 // 4
1
>>> food = 'Python\'s favourite food is perl'
>>> food
"Python's favourite food is perl"
>>> say = "\"Python is very easy.\" he says"
>>> say
'"Python is very easy." he says'
>>> multiline = "Life is too short\nYou need python"
>>> multiline
'Life is too short\nYou need python'
>>> multiline='''
... Life is too short
... You need python
... '''
>>> multiline
'\nLife is too short\nYou need python\n'
>>> print(multiline)

Life is too short
You need python

>>> head = "Python"
>>> tail = " is fun!"
>>> head + tail
'Python is fun!'
>>> a = "python"
>>> a * 2
'pythonpython'
>>> exit()
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 4 root root  148 May 20 22:03 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# cd jtp_ch05/
(base) [root@ip-172-31-23-187 jtp_ch05]# cd ..
(base) [root@ip-172-31-23-187 learning_python]# mkdir jtp_ch02
(base) [root@ip-172-31-23-187 learning_python]# cd jtp_ch02/
(base) [root@ip-172-31-23-187 jtp_ch02]# ll
total 0
(base) [root@ip-172-31-23-187 jtp_ch02]# vi multistring.py
(base) [root@ip-172-31-23-187 jtp_ch02]# python3 multistring.py 
==================================================
My Program
==================================================
(base) [root@ip-172-31-23-187 jtp_ch02]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "Life is too short, You need Python"
>>> a[3]
'e'
>>> a[0]
'L'
>>> a[12]
's'
>>> a[-1]
'n'
>>> a[-2]
'o'
>>> a[-5]
'y'
>>> b = a[0] + a[1] + a[2] + a[3]
>>> b
'Life'
>>> a[0:4]
'Life'
>>> a[0:1]
'L'
>>> a[0:3]
'Lif'
>>> a[0:]
'Life is too short, You need Python'
>>> a[19:-7]
'You need'
>>> a = "20010331Rainy"
>>> date = a[:8]
>>> weather = a[8:]
>>> date
'20010331'
>>> weather
'Rainy'
>>> a = "20010331Rainy"
>>> year = a[:4]
>>> day = a[4:8]
>>> weather = a[8:]
>>> year
'2001'
>>> day
'0331'
>>> weather
'Rainy'
>>> "I eat %d apples." % 3
'I eat 3 apples.'
>>> "I eat %s apples." % "five"
'I eat five apples.'
>>> number = 3
>>> "I eat %d apples." % number
'I eat 3 apples.'
>>> number = 10
>>> day = "three"
>>> "I ate %d apples. So I was sick for %s days." % (number, day)
'I ate 10 apples. So I was sick for three days.'
>>> 

