(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> q = [2, 3]
>>> p = [1, q, 4]
>>> p[1].append("버피")
>>> p
[1, [2, 3, '버피'], 4]
>>> q
[2, 3, '버피']
>>> p
[1, [2, 3, '버피'], 4]
>>> p[0].append("1번")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
>>> p[2].append("1번")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'int' object has no attribute 'append'
>>> 
>>> people = ["버피", "페이스"]
>>> people.append("자일스")
>>> people
['버피', '페이스', '자일스']
>>> people[len(people):] = ["잰더"]
>>> people
['버피', '페이스', '자일스', '잰더']
>>> 
>>> people = ["버피", "페이스"]
>>> people.extend("자일스")
>>> people
['버피', '페이스', '자', '일', '스']
>>> ['버피', '페이스', '자', '일', '스']
['버피', '페이스', '자', '일', '스']
>>> people += "윌로"
>>> people
['버피', '페이스', '자', '일', '스', '윌', '로']
>>> people[len(people):] = "아스틴"
>>> people
['버피', '페이스', '자', '일', '스', '윌', '로', '아', '스', '틴']
>>> 
>>> people = ["버피", "페이스"]
>>> people.insert(1, "잰더")
>>> people
['버피', '잰더', '페이스']
>>> 
>>> people = ["버피", "페이스"]
>>> people.remove("버피")
>>> people
['페이스']
>>> people.remove("버피")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
>>> 
>>> people = ["버피", "페이스", "아스틴"]
>>> people.pop(1)
'페이스'
>>> people
['버피', '아스틴']
>>> people.pop()
'아스틴'
>>> people
['버피']
>>> 
>>> a = [-1, 4, 5, 7, 10]
>>> del a[0]
>>> a
[4, 5, 7, 10]
>>> del a[2:3]
>>> a
[4, 5, 10]
>>> del a
>>> a
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> 
>>> people = ["버피", "페이스"]
>>> people.index("버피")
0
>>> 
>>> people = ["버피", "페이스", "버피"]
>>> people.count("버피")
2
>>> 
>>> people = ["잰더", "페이스", "버피"]
>>> people.sort()
>>> people
['버피', '잰더', '페이스']
>>> people.sort(reverse=true)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'true' is not defined
>>> people.sort(reverse=True)
>>> people
['페이스', '잰더', '버피']
>>> 
>>> imprt time
  File "<stdin>", line 1
    imprt time
             ^
SyntaxError: invalid syntax
>>> import time
>>> timestamp = [
...     "2018-12-12 01:17:31",
...     "2018-12-12 02:17:28",
...     "2018-12-12 06:39:26",
...     "2018-11-25 07:30:35",
...     "2018-11-25 11:32:33",
...     "2018-11-25 12:35:48"
... ]
>>> def time_format(t):
...     return time.strptime(t, '%Y-%m-%d %H:%M:%S')[0:6]
... 
>>> timestamp.sort(key=time_format, reverse=True) #날ㅉㅏ를 최신순으로 정렬
>>> timestamp.sort(key=time_format, reverse=True)
>>> timestamp.sort)key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S')[0:6], reverse=True)
  File "<stdin>", line 1
    timestamp.sort)key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S')[0:6], reverse=True)
                  ^
SyntaxError: invalid syntax
>>> timestamp.sort(key=lambda x: time.strptime(x, '%Y-%m-%d %H:%M:%S')[0:6], reverse=True)
>>> exit()
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import time
>>> timestamp = [
...      "2018-12-12 01:17:31",
...      "2018-12-12 02:17:28",
...      "2018-12-12 06:39:26"
... ]
>>> def time_format(t):
...     return time.strptime(t, '%Y-%m-%d %H:%M:%S')[0:6]
... 
>>> timestamp.sort(key=time_format, reverse=True)
>>> 
>>> people = ["잰더", "페이스", "버피"]
>>> people.reverse()
>>> people
['버피', '페이스', '잰더']
>>> people[::-1]
['잰더', '페이스', '버피']
>>> 
>>> first, *rest = [1,2,3,4,5]
>>> first
1
>>> rest
[2, 3, 4, 5]
>>> def example_args(a,b,c):
...     return a*b*c # 여기에서 * 연산자는 곱셈이다.
... L = [2,3,4]
  File "<stdin>", line 3
    L = [2,3,4]
    ^
SyntaxError: invalid syntax
>>> example_args(*L) # 리스트 언패킹
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'example_args' is not defined
>>> example_args(*L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'example_args' is not defined
>>> def example_args(a, b, c):
...     return a * b * c
... 
>>> L = [2, 3, 4]
>>> example_args(*L)
24
>>> example_args(2, *L[1:])
24
>>> 
>>> 
