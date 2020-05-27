Last login: Thu May 28 00:58:32 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = [1,2,3]
>>> b = [4,5,6]
>>> a + b
[1, 2, 3, 4, 5, 6]
>>> a = [1,2,3]
>>> a *3
[1, 2, 3, 1, 2, 3, 1, 2, 3]
>>> a = [1, 2, 3]
>>> len(a)
3
>>> a = [1, 2, 3]
>>> a[2] + "hi"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str'
>>> str(a[2]) + "hi"
'3hi'
>>> a = [1, 2, 3]
>>> a[2] = 4
>>> a
[1, 2, 4]
>>> a = [1, 2, 3]
>>> del a[1]
>>> a
[1, 3]
>>> del a[0]
>>> a
[3]
>>> a = [1, 2, 3, 4]
>>> del a[2:]
>>> a
[1, 2]
>>> a = [1, 2, 3]
>>> a.append(4)
>>> a
[1, 2, 3, 4]
>>> a.append([5, 6])
>>> a
[1, 2, 3, 4, [5, 6]]
>>> a = [1, 4, 3, 2]
>>> a.sort()
>>> a
[1, 2, 3, 4]
>>> a = ['a', 'c', 'b']
>>> a.sort()
>>> a
['a', 'b', 'c']
>>> a = ['a', 'c', 'b']
>>> a.reverse()
>>> a
['b', 'c', 'a']
>>> a = [1, 2, 3]
>>> a.index(3)
2
>>> a.index(1)
0
>>> a.index(0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 0 is not in list
>>> a = [1, 2, 3]
>>> a.insert(0, 4)
>>> a
[4, 1, 2, 3]
>>> a.insert(3, 5)
>>> a
[4, 1, 2, 5, 3]
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2]
>>> a = [1, 2, 3, 1, 2, 3]
>>> a.remove(3)
>>> a
[1, 2, 1, 2, 3]
>>> a.remove(3)
>>> a = [1, 2, 3]
>>> a.pop()
3
>>> a
[1, 2]
>>> a = [1, 2, 3]
>>> a.pop(1)
2
>>> a
[1, 3]
>>> a = [1, 2, 3, 1]
>>> a.count(1)
2
>>> a = [1, 2, 3]
>>> a.extend([4, 5])
>>> a
[1, 2, 3, 4, 5]
>>> b = [6, 7]
>>> a.extend(b)
>>> a
[1, 2, 3, 4, 5, 6, 7]
>>> 

