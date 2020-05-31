Last login: Sun May 31 01:08:05 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root  283 May 31 01:14 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = True
>>> b = False
>>> type(a)
<class 'bool'>
>>> type(b)
<class 'bool'>
>>> 1 == 1
True
>>> 2> 1
True
>>> 2 < 1
False
>>> a = [1,2,3,4]
>>> while a:
...     print(a.pop())
... 
4
3
2
1
>>> if []:
...     print("참")
... else:
...     print("거짓")
... 
거짓
>>> if [1,2,3]:
...     print("참")
... else:
...     print("거짓")
... 
참
>>> bool('python')
True
>>> bool('')
False
>>> bool([1,2,3])
True
>>> bool([])
False
>>> bool(0)
False
>>> bool(3)
True
>>> a = 1
>>> b = "python"
>>> c = [1,2,3]
>>> a = [1,2,3]
>>> id(a)
140128185496992
>>> a = [1,2,3]
>>> b = a
>>> id(a)
140128315022064
>>> id(b)
140128315022064
>>> a is b
True
>>> a[1] = 4
>>> a
[1, 4, 3]
>>> b
[1, 4, 3]
>>> a = [1,2,3]
>>> b = a[:]
>>> a[1] = 4
>>> a
[1, 4, 3]
>>> b
[1, 2, 3]
>>> id(a)
140128185496992
>>> id(b)
140128315022544
>>> from copy import copy
>>> b = copy(a)
>>> b is a
False
>>> a, b = ('python', 'life')
>>> (a, b) = 'python', 'life'
>>> [a,b] = ['python', 'life']
>>> a = b = 'python'
>>> a = 3
>>> b = 5
>>> a, b = b, ba
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'ba' is not defined
>>> a, b = b, a
>>> a
5
>>> b
3
>>> 

