(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> t1 = 1234, '안녕!'
>>> t1[0]
1234
>>> t1
(1234, '안녕!')
>>> t2 = t1, (1,2,3,4,5) #중첩됨(nested)
>>> t2
((1234, '안녕!'), (1, 2, 3, 4, 5))
>>> 
>>> empty = ()
>>> t1 = '안녕', # ㄸㅗ는 ('안녕',)
>>> len(empty)
0
>>> len(t1)
1
>>> t1
('안녕',)
>>> t2 = ('안녕')
>>> t2
'안녕'
>>> 
>>> t = 1,5,7,8,9,4,1,4
>>> t.count(4)
2
>>> t.count(1)
2
>>> t.count(7)
1
>>> 
>>> x, *y = (1,2,3,4)
>>> x
1
>>> y
[2, 3, 4]
>>> *x, y = (1,2,3,4)
>>> x
[1, 2, 3]
>>> y
4
>>> 
>>> import collections
>>> Person = collections.namedtuple('Person', 'name age gender')
>>> p = Person('아스틴', 30, '남자')
>>> p
Person(name='아스틴', age=30, gender='남자')
>>> p[0]
'아스틴'
>>> p.name
'아스틴'
>>> p.age = 20 # 에러: 일반 튜플과 마찬가지로 불변형이다.
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: can't set attribute
>>>
