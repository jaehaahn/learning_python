(base) [root@ip-172-31-23-187 chapter_02]# python3 
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> slayers = "Buffy and Faith"
>>> slayers.swapcase()
'bUFFY AND fAITH'
>>> 
>>> slayers = "Buffy and Faith"
>>> slayers.find("y")
4
>>> slayers.find("k")
-1
>>> slayers.index("k")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: substring not found
>>> slayers.index("y")
4
>>> 
>>> slayer = "Buffy is Buffy is Buffy"
>>> slayer.count("Buffy", 0, -1)
2
>>> slayer.count("Buffy")
3
>>> 
>>> slayer = "Buffy is Buffy is Buffy
  File "<stdin>", line 1
    slayer = "Buffy is Buffy is Buffy
                                    ^
SyntaxError: EOL while scanning string literal
>>> slayer = "Buffy is Buffy is Buffy"
>>> slayer.replace("Buffy", "who", 2)
'who is who is Buffy'
>>> 
>>> name = "프레드"
>>> f"그의 이름은 {name!r}입니다."
"그의 이름은 '프레드'입니다."
>>> f"그의 이름은 {repr(name)}입니다." # repr()은 !r과 같다.
"그의 이름은 '프레드'입니다."
>>> import decimal
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"결과: {value:{width}.{precision}}" # 중첩 필드 사용
'결과:      12.35'
>>> from datetime import datetime
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}" # 날ㅉㅏ 포맷 지정 지정가(specifier) 사용
'January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}" # 정수 포맷 지정자 사용 (16진수 표현)
'0x400
