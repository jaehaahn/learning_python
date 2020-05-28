Last login: Thu May 28 01:08:49 2020 from 220.72.142.105

       __|  __|_  )
       _|  (     /   Amazon Linux 2 AMI
      ___|\___|___|

https://aws.amazon.com/amazon-linux-2/
14 package(s) needed for security, out of 27 available
Run "sudo yum update" to apply all updates.
[ec2-user@ip-172-31-23-187 ~]$ sudo su
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 12
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root  178 May 28 01:29 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# cd jtp_ch02
(base) [root@ip-172-31-23-187 jtp_ch02]# ll
total 24
-rw-r--r-- 1 root root 3879 May 21 23:22 ch2_practice_0520.py
-rw-r--r-- 1 root root 3123 May 22 23:07 ch2_practice_0522.py
-rw-r--r-- 1 root root  116 May 23 18:50 ch2_practice_0523.py
-rw-r--r-- 1 root root  918 May 26 00:40 ch2_practice_list_0525.py
-rw-r--r-- 1 root root 2085 May 28 01:29 ch2_practice_list_0527.py
-rw-r--r-- 1 root root   54 May 21 23:14 multistring.py
(base) [root@ip-172-31-23-187 jtp_ch02]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> t1 = ()
>>> t2 = (1,)
>>> t3 = (1, 2, 3)
>>> t4 = 1, 2, 3
>>> t5 = ('a', 'b', ('ab', 'cd'))
>>> t1 = (1, 2, 'a', 'b')
>>> del t1[0]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object doesn't support item deletion
>>> t1[0] = 'c'
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'tuple' object does not support item assignment
>>> t1 = (1, 2, 'a', 'b')
>>> t1[0]
1
>>> t1[3]
'b'
>>> t1[1:]
(2, 'a', 'b')
>>> t2 = (3, 4)
>>> t1 + t2
(1, 2, 'a', 'b', 3, 4)
>>> t2 = (3, 4)
>>> t2 * 3
(3, 4, 3, 4, 3, 4)
>>> t1 = (1, 2, 'a', 'b')
>>> len(t1)
4
>>> exit()
(base) [root@ip-172-31-23-187 jtp_ch02]# 

