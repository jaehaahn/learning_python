(base) [root@ip-172-31-23-187 ec2-user]# python3
Python 3.7.6 (default, Jan  8 2020, 19:59:22) 
[GCC 7.3.0] :: Anaconda, Inc. on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> blist = [1, 2, 3, 255]
>>> the_bytes = bytes(blist)
>>> the_bytes
b'\x01\x02\x03\xff'
>>> 
>>> the_byte_array = bytearray(blist)
>>> the_byte_array
bytearray(b'\x01\x02\x03\xff')
>>> the_bytes[1] = 127
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: 'bytes' object does not support item assignment
>>> 
>>> the_bytes_array[1] = 127
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'the_bytes_array' is not defined
>>> the_byte_array[1] = 127
>>> the_byte_array
bytearray(b'\x01\x7f\x03\xff')
>>> 
>>> x = 4
>>> 1 << x
16
>>> 
>>> x = 8
>>> x & (x-1)
0
>>> 
>>> x = 6
>>> x & (x-1)
4
>>> exit()

