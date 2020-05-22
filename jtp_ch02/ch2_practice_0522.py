Last login: Fri May 22 19:17:09 2020 from 175.223.11.150

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
1(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root   56 May 21 23:22 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# cd jtp_ch02
(base) [root@ip-172-31-23-187 jtp_ch02]# ll
total 8
-rw-r--r-- 1 root root 3879 May 21 23:22 ch2_practice_0520.py
-rw-r--r-- 1 root root   54 May 21 23:14 multistring.py
(base) [root@ip-172-31-23-187 jtp_ch02]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> "I ate (0) apples. So I was sick for (day) days.".format(10, day=3)
'I ate (0) apples. So I was sick for (day) days.'
>>> "I ate {0} apples. So I was sick for {day} days.".format(10, day=3)
'I ate 10 apples. So I was sick for 3 days.'
>>> "{0:<10}".format("hi")
'hi        '
>>> "{0:>10}".format("hi")
'        hi'
>>> "{0:^10}".format("hi")
'    hi    '
>>> "{0:=^10}".format("hi")
'====hi===='
>>> "{0:!<10}".format("hi")
'hi!!!!!!!!'
>>> y = 3.42134234
>>> "{0:0.4f}".format(y)
'3.4213'
>>> "{0:10.4f}".format(y)
'    3.4213'
>>> "{{ and }}".format()
'{ and }'
>>> name = '홍길동'
>>> age = 30
>>> f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
'나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> age = 30
>>> f'나는 내년이면 {age+1}살이 된다.'
'나는 내년이면 31살이 된다.'
>>> d = {'name':'홍길동', 'age':30}
>>> f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.''나의 이름은 홍길동입니다. 나이는 30입니다.'
>>> f'{"hi":<10'
  File "<stdin>", line 1
SyntaxError: f-string: expecting '}'
>>> f'{"hi":<10}'
'hi        '
>>> f'{"hi":>10}'
'        hi'
>>> f'{"hi":^10}'
'    hi    '
>>> f'{"hi":=^10}'
'====hi===='
>>> f'{"hi":!<10}'
'hi!!!!!!!!'
>>> y = 3.23123234
>>> f'{y:0.4f}'
'3.2312'
>>> f'{y:10.4f}'
'    3.2312'
>>> f'{{ and }}'
'{ and }'
>>> a = "hobby"
>>> a.count('b')
2
>>> a = "Python is the best choice"
>>> a.find('b')
14
>>> a.find('k')
-1
>>> a = "Life is too short"
>>> a.index('t')
8
>>> a.index('k')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> ",".join('abcd')
'a,b,c,d'
>>> 

