(base) Jaes-MacBook:~ jaehaahn$ python3
Python 3.7.6 (default, Jan  8 2020, 13:42:34)
[Clang 4.0.1 (tags/RELEASE_401/final)] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> first, *rest = [1,2,3,4,5]
>>> first
1
>>> rest
[2, 3, 4, 5]
>>>
>>> def example_args(a, b, c):
...     return a * b * c # 여기에서 * 연산자는 곱셈이다.
... L = [2, 3, 4]
  File "<stdin>", line 3
    L = [2, 3, 4]
    ^
SyntaxError: invalid syntax
>>> L = [2,3,4]
>>> example_args(*L) # 리스트 언패킹
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'example_args' is not defined
>>> example_args(*L)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'example_args' is not defined
>>> example_args(2, *L[1:])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'example_args' is not defined
>>> def example_args(a,b,c):
...     return a*b*c
...
>>> L = [2,3,4]
>>> example_args(*L)
24
>>> example_args(2, *L[1:])
24
>>>
>>> a = [y for y in range(1900, 1940) if y%4 == 0]
>>> a
[1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]
>>> b = [2**i for i in range(13)]
>>> b
[1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
>>> c = [x for x in a if x%2==0]
>>> c
[1900, 1904, 1908, 1912, 1916, 1920, 1924, 1928, 1932, 1936]
>>> d = [str(round(355/113.0,i)) for i in range(1,6)]
>>> d
['3.1', '3.14', '3.142', '3.1416', '3.14159']
>>> words = 'Buffy is awesome and a vampire slayer' .split()
>>> e = [[w.upper(), w.lower(), len(w)] for w in words]
>>> for i in e:
...     print(i)
...
['BUFFY', 'buffy', 5]
['IS', 'is', 2]
['AWESOME', 'awesome', 7]
['AND', 'and', 3]
['A', 'a', 1]
['VAMPIRE', 'vampire', 7]
['SLAYER', 'slayer', 6]
>>>
>>> result = []
>>> for x in range(10):
...     for y in range(5):
...          if x * y > 10:
...             result.append((x, y))
...
>>> for x in range(5):
...     for y in range(5):
...         if x != y:
...             for y != z:
  File "<stdin>", line 4
    for y != z:
           ^
SyntaxError: invalid syntax
>>>
