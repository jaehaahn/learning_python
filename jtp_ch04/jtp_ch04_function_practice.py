Authenticating with public key "Imported-Openssh-Key: C:\Users\ucand\Downloads\jaeha_2.pem"
     ┌────────────────────────────────────────────────────────────────────┐
     │                        • MobaXterm 11.1 •                          │
     │            (SSH client, X-server and networking tools)             │
     │                                                                    │
     │ ➤ SSH session to ec2-user@54.180.85.186                            │
     │   • SSH compression : ✔                                            │
     │   • SSH-browser     : ✔                                            │
     │   • X11-forwarding  : ✘  (disabled or not supported by server)     │
     │   • DISPLAY         : 192.168.0.105:0.0                            │
     │                                                                    │
     │ ➤ For more info, ctrl+click on help or visit our website           │
     └────────────────────────────────────────────────────────────────────┘

Last login: Mon Jun  8 08:32:53 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
17 package(s) needed for security, out of 34 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# ll
total 534096
-rw-rw-r-- 1 ec2-user ec2-user 546910666 Apr 21 15:31 Anaconda3-2020.02-Linux-x86_64.sh
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22)
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> def add(a, b)
  File "<stdin>", line 1
    def add(a, b)
                ^
SyntaxError: invalid syntax
>>> def add(a, b):
...     return a + b
...
>>> a = 3
>>> b = 4
>>> c = add(a, b)
>>> print(c)
7
>>> def add(a, b):
...     result = a + b
...     return result
...
>>> a = add(3, 4)
>>> print(a)
7
>>> def say():
...     return 'Hi"
  File "<stdin>", line 2
    return 'Hi"
              ^
SyntaxError: EOL while scanning string literal
>>> def say():
...     return 'Hi'
...
>>> a = say()
>>> print(a)
Hi
>>> def add(a, b):
...     print(%d, %d의 합은 %d입니다." % (a, b, a+b))
  File "<stdin>", line 2
    print(%d, %d의 합은 %d입니다." % (a, b, a+b))
          ^
SyntaxError: invalid syntax
>>> def add(a, b):
...     print("%d, %d의 합은 %d입니다." % (a, b, a+b))
...
>>> a = add(3, 4)
3, 4의 합은 7입니다.
>>> a = add(3, 4)
3, 4의 합은 7입니다.
>>> print(a)
None
>>> def (say):
  File "<stdin>", line 1
    def (say):
        ^
SyntaxError: invalid syntax
>>> def say():
...     print('Hi')
...
>>> say()
Hi
>>> def add(a, b):
...     return a+b
...
>>> result = add(a=3, b=7)
>>> print(result)
10
>>> result = add(b=5, a=3)
>>> print(result)
8
>>> def add_many(*args):
...     result = 0
...     for i in args:
...         result = result + i
...     return result
...
>>> result = add_many(1,2,3)
>>> print(result)
6
>>> result = add_many(1,2,3,4,5,6,7,8,9,10)
>>> print(result)
55
>>> def add_mul(choice, *args):
...     if choice == "add":
...         result = 0
...         for i in args:
...             result = result + i
...     elif choice == "mul":
...         result = 1
...         for i in args:
...             result = result * i
...     return result
...
>>> result = add_mul('add', 1,2,3,4,5)
>>> print(result)
15
>>> result = add_mul('mul', 1,2,3,4,5)
>>> print(result)
120
>>> def print_kwargs(**kwargs):
...     print(kwargs)
...
>>> print_kwargs(a=1)
{'a': 1}
>>> {'a': 1}
{'a': 1}
>>> print_kwargs(name='foo', age=3)
{'name': 'foo', 'age': 3}
>>> def add_and_mul(a, b):
...     return a+b, a*b
...
>>> result = add_and_mul(3,4)
>>> result
(7, 12)
>>> def add_and_mul(a,b):
...     return a+b
...     return a*b
...
>>> result = add_and_mul(2,3)
>>> print(result)
5
>>> def add_and_mul(a,b):
...     return a+b
...
>>> def say_nick(nick):
...     if nick == "바보":
...         return
...     print("나의 별명은 %s입니다." % nick)
...
>>> say_nick('야호')
나의 별명은 야호입니다.
>>> say_nick('바보')
>>> exit()
(base) [root@ip-172-31-23-187 learning_python]#

