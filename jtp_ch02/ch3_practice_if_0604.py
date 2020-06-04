Last login: Thu Jun  4 21:55:03 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
17 package(s) needed for security, out of 34 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 16
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root 4096 Jun  2 16:04 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# cd jtp_ch02/
(base) [root@ip-172-31-23-187 jtp_ch02]# ll
total 44
-rw-r--r-- 1 root root 3879 May 21 23:22 ch2_practice_0520.py
-rw-r--r-- 1 root root 3123 May 22 23:07 ch2_practice_0522.py
-rw-r--r-- 1 root root  116 May 23 18:50 ch2_practice_0523.py
-rw-r--r-- 1 root root 2176 May 31 23:17 ch2_practice_bool_variable_0531.py
-rw-r--r-- 1 root root 3280 May 30 00:48 ch2_practice_dictionary_0529.py
-rw-r--r-- 1 root root  918 May 26 00:40 ch2_practice_list_0525.py
-rw-r--r-- 1 root root 2085 May 28 01:29 ch2_practice_list_0527.py
-rw-r--r-- 1 root root 2862 May 31 01:14 ch2_practice_set_0529.py
-rw-r--r-- 1 root root 1676 Jun  2 16:04 ch2_practice_test_0602.py
-rw-r--r-- 1 root root 2135 May 28 16:27 ch2_practice_tuple_0528.py
-rw-r--r-- 1 root root   54 May 21 23:14 multistring.py
(base) [root@ip-172-31-23-187 jtp_ch02]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> money = True
>>> if money:
...     print("택시를 타고 가라")
... else
  File "<stdin>", line 3
    else
       ^
SyntaxError: invalid syntax
>>> if money:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
... 
택시를 타고 가라
>>> x = 3
>>> y = 2
>>> x > y
True
>>> x < y
False
>>> x == y
False
>>> x != y
True
>>> money = 2000
>>> if money >= 3000:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
... 
걸어가라
>>> money = 2000
>>> card = True
>>> if money >=3000 or card:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
... 
택시를 타고 가라
>>> 1 in [1,2,3,4]
True
>>> 1 not in [1,2,3,4]
False
>>> 'a' in ('a', 'b', 'c')
True
>>> 'j' not in 'python'
True
>>> pocket = ['paper', 'cellphone', 'money']
>>> if 'money' in pocket:
...     print("택시를 타고 가라")
... else:
...     print("걸어가라")
... 
택시를 타고 가라
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money in pocket:
  File "<stdin>", line 1
    if 'money in pocket:
                       ^
SyntaxError: EOL while scanning string literal
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money in pocket:
  File "<stdin>", line 1
    if 'money in pocket:
                       ^
SyntaxError: EOL while scanning string literal
>>> pocket = ['paper', 'money', 'cellphone']
>>> if 'money' in pocket:
...     pass
... else:
...     print("카드를 ㄲㅓ내라")
... 
>>> pocket = ['paper', 'handphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고가라")
... else:
...     if card:
...         print("택시를 타고가라")
...     else:
...         print("걸어가라")
... 
택시를 타고가라
>>> pocket = ['paper', 'cellphone']
>>> card = True
>>> if 'money' in pocket:
...     print("택시를 타고가라")
... elif card:
...     print("택시를 타고라라")
... else:
...     print("걸어가라")
... 
택시를 타고라라
>>> if score >= 60:
...     message = "success"
... else:
...     message = "failure"
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'score' is not defined
>>> message = "success" if score >= 60 else "failure"
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'score' is not defined
>>> 

