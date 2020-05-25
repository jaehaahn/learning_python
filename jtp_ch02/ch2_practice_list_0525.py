(base) [root@ip-172-31-23-187 jtp_ch02]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> odd = [1, 3, 5, 7, 9]
>>> a = [1, 2, 3]
>>> a
[1, 2, 3]
>>> a[0]
1
>>> a[0] + a[2]
4
>>> a[-1]
3
>>> a = [1, 2, 3, ['a', 'b', 'c']
... ]
>>> a = [1, 2, 3, ['a', 'b', 'c']]
>>> a[0]
1
>>> a[-1]
['a', 'b', 'c']
>>> a[3]
['a', 'b', 'c']
>>> a[-1][0]
'a'
>>> a[-1][1]
'b'
>>> a = [1, 2, ['a', 'b', ['Life', 'is']]]
>>> a[2][2][0]
'Life'
>>> a = [1, 2, 3, 4, 5]
>>> a[0:2]
[1, 2]
>>> a = "12345"
>>> a[0:2]
'12'
>>> a = [1, 2, 3, 4, 5]
>>> b = a[:2]
>>> c = a[2:]
>>> v
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'v' is not defined
>>> b
[1, 2]
>>> c
[3, 4, 5]
>>> a = [1, 2, 3, ['a', 'b', 'c'], 4, 5]
>>> a[2:5]
[3, ['a', 'b', 'c'], 4]
>>> a[3][:2]
['a', 'b']
>>> 

