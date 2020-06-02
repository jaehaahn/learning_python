Last login: Tue Jun  2 01:06:31 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = "a:b:c:d"
>>> b = a.replace(":
  File "<stdin>", line 1
    b = a.replace(":
                   ^
SyntaxError: EOL while scanning string literal
>>> b = a.replace(":", "#")
>>> b
'a#b#c#d'
>>> a = [1,3,5,4,3]
>>> a.sort()
>>> a.reverse()
>>> a
[5, 4, 3, 3, 1]
>>> a = ['Life', 'is', 'too', 'short']
>>> result = " ".join(a)
>>> result
'Life is too short'
>>> a = (1,2,3)
>>> a = a + (4)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate tuple (not "int") to tuple
>>> a = a + (4,)
>>> a
(1, 2, 3, 4)
>>> a = (1,2,3)
>>> id(a)
140129557378944
>>> a = a + (4,)
>>> id(a)
140129427848560
>>> a[[1]] = 'python'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> a = {'A':90, 'B':80, 'C':70)
  File "<stdin>", line 1
    a = {'A':90, 'B':80, 'C':70)
                               ^
SyntaxError: invalid syntax
>>> a = {'A':90, 'B':80, 'C':70}
>>> result = a.pop('B')
>>> a
{'A': 90, 'C': 70}
>>> result
80
>>> a = [1,1,1,2,2,3,3,3,4,4,5]
>>> aSet = set(a)
>>> b = list(aSet)
>>> print(b)
[1, 2, 3, 4, 5]
>>> 

