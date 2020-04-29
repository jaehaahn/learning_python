(base) [root@ip-172-31-23-187 ec2-user]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> wor = "뱀파이어를 조심해!"
>>> word = "밤팽
KeyboardInterrupt
>>> word = "밤패아이
KeyboardInterrupt
>>> word = "뱀파이어를 조심해!"
>>> word[-1]
'!'
>>> word[-2]
'해'
>>> word[-2:]
'해!'
>>> word[:-2]
'뱀파이어를 조심'
>>> word[-0]
'뱀'
>>>
>>> u'잘가\u0020세상!'
'잘가 세상!'
>>> ㅓ
KeyboardInterrupt
>>> slayer = ["버피", "앤", "아스틴"]
>>> " ".join(slayer)
'버피 앤 아스틴'
>>> "-<>-".join(slayer)
'버피-<>-앤-<>-아스틴'
>>> "".join(slayer)
'버피앤아스틴'
>>>
>>> "".join(reversed(slayer))
'아스틴앤버피'
>>>
>>> name = "스칼렛"
>>> name.ljust(50, '_')
'스칼렛_______________________________________________'
>>> name.rjust(50, '-')
'-----------------------------------------------스칼렛'
>>>
>>> "{0} {1}".format("안녕,", "파이썬!")
'안녕, 파이썬!'
>>> "이름: {who}, 나이: {age}".format(who="제임스", age=17)
'이름: 제임스, 나이: 17'
>>> "이름: {who}, 나이(0)".format(12, who="ㅇㅇ이미지")
'이름: ㅇㅇ이미지, 나이(0)'
>>> "{} {} {}".format("파이썬", "자료구조", "알고리즘")
'파이썬 자료구조 알고리즘'
>>> import decimal
>>> "{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("99.9"))
"99.9 99.9 Decimal('99.9') Decimal('99.9')"
>>>
>>> hero = "버피"
>>> number = 999
>>> "{number}: {hero}".format(**locals())
'999: 버피'
>>>
>>> slayers = "로미오\n줄리엣"
>>> slayers.splitlines()
['로미오', '줄리엣']
>>>
