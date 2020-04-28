(djangoenv) (base) [root@ip-172-31-23-187 ~]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import copy
>>> my0bj = "다른 어떤 객체"
>>> new0bj = copy.copy(my0bj)
>>> new0bj2 = copy.deepcopy(my0bj)
>>> print new0bj
  File "<stdin>", line 1
    print new0bj
               ^
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(new0bj)?
>>> print(new0bj)
다른 어떤 객체
>>> print(new0bj2)
다른 어떤 객체
>>>
