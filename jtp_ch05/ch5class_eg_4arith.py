(base) [root@ip-172-31-23-187 jtp_ch05]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> a = FourCal()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FourCal' is not defined
>>> a.setdata(4, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'a' is not defined
>>> a = FourCal()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FourCal' is not defined
>>> a=FourCal()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'FourCal' is not defined
>>> class FourCal:
...     pass
... 
>>> a = FourCal()
>>> type(a)
<class '__main__.FourCal'>
>>> a.setdata(4, 2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FourCal' object has no attribute 'setdata'
>>> 
>>> class FourCal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
... 
>>> def setdata(self, first, second):
...     self.first = first
...     self.second = second
... 
>>> self.first = 4
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'self' is not defined
>>> def setdata(self, first, second):
...     self.first = first
...     self.second = second
... self.first = 4
  File "<stdin>", line 4
    self.first = 4
       ^
SyntaxError: invalid syntax
>>> a = FourCal()
>>> a.setdata(4, 2)
>>> print(a.first)
4
>>> print(a.second)
2
>>> a = FourCal()
>>> b = FourCal()
>>> a.setdata(4, 2)
>>> print(a.first)
4
>>> b.setdata(4, 2)
>>> print(b.first)
4
>>> print(a.first)
4
>>> a = FourCal()
>>> b = FourCal()
>>> a.setdata(4, 2)
>>> b.setdata(3, 7)
>>> id(a.first)
93905312932704
>>> id(b.first)
93905312932672
>>> a = FourCal()
>>> a.setdata(4, 2)
>>> print(a.add())
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
AttributeError: 'FourCal' object has no attribute 'add'
>>> class FourCal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...     def add(self):
...         result = self.first + self.second)
  File "<stdin>", line 6
    result = self.first + self.second)
                                     ^
SyntaxError: invalid syntax
>>>  class FourCal:
  File "<stdin>", line 1
    class FourCal:
    ^
IndentationError: unexpected indent
>>> Class FourCal:
  File "<stdin>", line 1
    Class FourCal:
                ^
SyntaxError: invalid syntax
>>> class Fourcal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...     def add(self):
...         result = self.first + self.second
...         return result
... 
>>> a = Fourcal()
>>> a.setdata(4,2)
>>> print(a.add())
6
>>> class FourCal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...     def add(self):
...         result = self.first + self.second
...         return result
...     def mul(self):
...         result = self.first * self.second
...     def sub(self):
...         result = self.first - self.second
...     
KeyboardInterrupt
>>> class FourCal:
...     def setdata(self, first, second):
...         self.first = first
...         self.second = second
...     def add(self):
...         result = self.first + self.second
...         return result
...     def mul(self):
...         result = self.first * self.second
...         return result
...     def sub(self):
...         result = self.first - self.second
...         return result
...     def div(self):
...         result = self.first / self.second
...         return result
... 
>>> a = FourCal()
>>> b = FourCal()
>>> a.setdata(4, 2)
>>> b.setdata(3, 8)
>>> a.add()
6
>>> a.mul()
8
>>> a.div()
2.0
>>> b.add()
11
>>> b.mul()
24
>>> b.sub()
-5
>>> b.div()
0.375
>>>  
