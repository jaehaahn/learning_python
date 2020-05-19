(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
>>> print(mod1.add(3, 4))
7
>>> print(mod1.sub(4, 2))
2
>>> from mod1 import add
>>> add(3, 4)
7
>>> from mod1 import add, sub
>>> sub(5, 1)
4
>>> from mod1 import *
>>> add(3, 4)
7
>>> exit
Use exit() or Ctrl-D (i.e. EOF) to exit
>>> exit()
(base) [root@ip-172-31-23-187 jtp_ch05]# vi mod1.py
(base) [root@ip-172-31-23-187 jtp_ch05]# python3 mod1.py
5
2
(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
5
2
>>> exit()
(base) [root@ip-172-31-23-187 jtp_ch05]# vi mod1.py
(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "/home/git/repo/learning_python/jtp_ch05/mod1.py", line 7, in <module>
    if __name == "__main__":
NameError: name '__name' is not defined
>>> exit()
(base) [root@ip-172-31-23-187 jtp_ch05]# vi mod1.py
(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod1
>>> exit()
(base) [root@ip-172-31-23-187 jtp_ch05]#



(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import mod2
>>> print(mod2.PI)
3.141592
>>> a = mod2.Math()
>>> print(a.solv(2))
12.566368
>>> print(mod2.add(mod2.PI, 4.4))
7.5415920000000005
>>> exit()

