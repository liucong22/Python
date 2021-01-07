"""
    practice01
    计算C(M,N) = M!/N!(M-N)!
    author:liucong
    wersion:0.1
    date：2021-01-07
"""
m = int(input('m = '))
n = int(input('n = '))
# 分别算m的阶乘，n的阶乘，（m-n）的阶乘
fm = 1
for i in range(1, m + 1):
    fm *= i
fn = 1
for j in range(1, n + 1):
    fn *= j
fm_n = 1
for k in range(1, m - n + 1):
    fm_n *= k
print("C(m,n) = %d" % (fm // fn // fm_n))

"""
    practice01
    计算C(M,N) = M!/N!(M-N)!
    author:liucong
    wersion:0.2
    date：2021-01-07
"""
# 自己封装函数
def fac(num):
    # 求阶乘
    res = 1
    for i in range(1, num + 1):
        res *= i
    return res

m = int(input('m = '))
n = int(input('n = '))
print("C(m,n) = %d" % (fac(m) // fac(n) // fac(m-n)))

"""
    practice01
    计算C(M,N) = M!/N!(M-N)!
    author:liucong
    wersion:0.3
    date：2021-01-07
"""
# 使用现有函数
import math
m = int(input('m = '))
n = int(input('n = '))
print("C(m,n) = %d" % (math.factorial(m) // math.factorial(n) // math.factorial(m-n)))

"""
    practice02
    python对函数参数的处理
    author:liucong
    version:0.1
    date：2021-01-07
"""
from random import randint
# 掷骰子
def roll_dice(n = 2):
    total = 0
    for _ in range(n):
        total += randint(1, 6)
    return total

# 三个数相加
def add(a = 0, b = 0, c = 0):
    return a + b + c

print(roll_dice())
print(roll_dice(3))
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 3, 3))
print(add(b = 100, c = 2, a = 5))

# 传参是由调用者决定的，如果是非必传参数，可以使用可变参数
# 在参数名前面的*表示args是一个可变参数
def add(*args):
    total = 0
    for val in args:
        total += val
    return total

# 在调用add函数时可以传入0个或多个参数
print(add())
print(add(1))
print(add(1, 2))
print(add(1, 2, 3))
print(add(1, 3, 5, 7, 9))



