"""
>>> 1000
1000
>>> 100000
100000
>>> 1_000_000
1000000
>>> num = 42
>>> print(num)
42
>>> num + 1
43
>>> print(num + 1)
43
>>> num += 1
>>> num
43
>>> nnum = num + 1
>>> num
43
>>> num = num + 1
>>> num
44
>>> type(num)
<class 'int'>
>>> num
44
>>> num.__add__(6)
50

"""

#  Conversão de int para float
num = 5
print(num)
print(type(num))

res = float(num) # Conversão

print(num)
print(type(res))
