Last login: Thu May 28 16:21:42 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ 녀애 
-bash: 녀애: command not found
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# 1dhkdls
bash: 1dhkdls: command not found
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root  212 May 28 16:27 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
bash: dic: command not found
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> dic = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}>>> dic
{'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a = {1: 'hi'}
>>> a = { 'a': [1,2,3]}
>>> a = {1: 'a'}
>>> a[2] = 'b'
>>> a
{1: 'a', 2: 'b'}
>>> a['name'] = 'pey
  File "<stdin>", line 1
    a['name'] = 'pey
                   ^
SyntaxError: EOL while scanning string literal
>>> a['name'] = 'pey'
>>> a
{1: 'a', 2: 'b', 'name': 'pey'}
>>> a[3] = [1,2,3]
>>> a
{1: 'a', 2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>> del a[1]
>>> a
{2: 'b', 'name': 'pey', 3: [1, 2, 3]}
>>> grade = {'pey': 10, 'julliet': 99}
>>> grade['pey']
10
>>> grade['julliet']
99
>>> a = {1:'a', 2:'b'}
>>> a[1]
'a'
>>> a[2]
'b'
>>> a = {'a':1, 'b':2}
>>> a['a']
1
>>> a['b']
2
>>> dic
{'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> dic['name']
'pey'
>>> dic['phone']
'0119993323'
>>> dic['birth']
'1118'
>>> a = {1:'a', 1:'b'}
>>> a
{1: 'b'}
>>> a = {[1,2] : 'hi'}
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: unhashable type: 'list'
>>> a = {'name': 'pey', 'phone': '0119993323', 'birth': '1118'}
>>> a.keys()
dict_keys(['name', 'phone', 'birth'])
>>> for k in a.keys():
...     print(k)
... 
name
phone
birth
>>> list(a.keys())
['name', 'phone', 'birth']
>>> a.values()
dict_values(['pey', '0119993323', '1118'])
>>> a.values()
dict_values(['pey', '0119993323', '1118'])
>>> a.items()
dict_items([('name', 'pey'), ('phone', '0119993323'), ('birth', '1118')])
>>> a.clear()
>>> a
{}
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> a.get('name')
'pey'
>>> a.get('phone')
'0119993323'
>>> a = {'name':'pey', 'phone':'0119993323', 'birth': '1118'}
>>> print(a.get('nokey'))
None
>>> print(a['nokey'])
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
KeyError: 'nokey'
>>> a.get('foo', 'bar')
'bar'
>>> a = {'name':'pey', 'phone':'0119993323', 'birth':'1118'}
>>> 'name' in a
True
>>> 'email' in a
False
>>> exit()
(base) [root@ip-172-31-23-187 learning_python]# 

