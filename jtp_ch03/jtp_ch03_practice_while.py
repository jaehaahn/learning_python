Last login: Thu Jun  4 23:43:12 2020 from 220.72.142.105

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
(base) [root@ip-172-31-23-187 ec2-user]# cd /home/git/
(base) [root@ip-172-31-23-187 git]# ll
total 0
drwxr-xr-x 3 root root 29 Apr 22 15:32 repo
(base) [root@ip-172-31-23-187 git]# cd repo/learning_python/
(base) [root@ip-172-31-23-187 learning_python]# ll
total 16
drwxr-xr-x 2 root root 4096 Apr 28 10:33 chapter_01
drwxr-xr-x 2 root root 4096 May 11 10:33 chapter_02
drwxr-xr-x 2 root root   33 May 17 23:44 chapter_05
drwxr-xr-x 2 root root 4096 Jun  4 23:52 jtp_ch02
drwxr-xr-x 4 root root  148 May 22 19:15 jtp_ch05
-rw-r--r-- 1 root root 1014 Apr 22 15:33 README.md
(base) [root@ip-172-31-23-187 learning_python]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> treeHit = 0
>>> while treeHit < 10:
...     treeHit = treeHit +1
...     print("나무를 %d번ㅉㅣㄱ어어습니다." % treeHit)
...     if treeHit == 10:
...         print("나무 넘어갑니다.")
... 
나무를 1번ㅉㅣㄱ어어습니다.
나무를 2번ㅉㅣㄱ어어습니다.
나무를 3번ㅉㅣㄱ어어습니다.
나무를 4번ㅉㅣㄱ어어습니다.
나무를 5번ㅉㅣㄱ어어습니다.
나무를 6번ㅉㅣㄱ어어습니다.
나무를 7번ㅉㅣㄱ어어습니다.
나무를 8번ㅉㅣㄱ어어습니다.
나무를 9번ㅉㅣㄱ어어습니다.
나무를 10번ㅉㅣㄱ어어습니다.
나무 넘어갑니다.
>>> prompt = """
... 1. Add
... 2. Del
... 3. List
... 4. Quit
... 
... Enter number: """
>>> number = 0
>>> while number != 4:
...     print(prompt)
...     number = int(input())
... 

1. Add
2. Del
3. List
4. Quit

Enter number: 
1

1. Add
2. Del
3. List
4. Quit

Enter number: 
2

1. Add
2. Del
3. List
4. Quit

Enter number: 
3

1. Add
2. Del
3. List
4. Quit

Enter number: 
4
>>> coffee = 10
>>> money = 300
>>> while money:
... print("돈을 받아아으니 커피를 줍니다.")
  File "<stdin>", line 2
    print("돈을 받아아으니 커피를 줍니다.")
        ^
IndentationError: expected an indented block
>>> coffee = 10
>>> money = 300
>>> while money:
...     print("돈을 받아아으니 커피를 줍니다.")
...     coffee = coffee -1
...     print("남은 커피의 양은 %d개입니다." % coffee)
...     if coffee == 0:
...         print("커피가 다 ㄸㅓㄹ어져져습니다. 판매를 중지합니다.")
...         break
... 
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 9개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 8개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 7개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 6개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 5개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 4개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 3개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 2개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 1개입니다.
돈을 받아아으니 커피를 줍니다.
남은 커피의 양은 0개입니다.
커피가 다 ㄸㅓㄹ어져져습니다. 판매를 중지합니다.
>>> exit()
(base) [root@ip-172-31-23-187 learning_python]# 

