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

"""
    practice03
    实现计算求最大公约数和最小公倍数的函数
    author:liucong
    version:0.1
    date：2021-01-07
"""
def gcd(x, y):
    # 求最大公因数
    if x > y:
        x, y = y, x
    for res in (x, 0, -1):
        if x % res == 0 and y % res == 0:
            return res

def lcm(x, y):
    # 求最小公倍数
    return x * y // gcd(x, y)


"""
    practice04
    实现判断一个数是不是回文数的函数:12421, 对称数
    author:liucong
    version:0.1
    date：2021-01-07
"""
def is_palindrome(num):
    # 判断一个数是不是回文数
    temp = num
    total = 0
    while temp > 0:
        total = total * 10 + temp % 10
        temp //= 10
    return total == num

"""
    practice05
    实现判断一个数是不是素数的函数
    author:liucong
    version:0.1
    date：2021-01-07
"""
def is_prime(num):
    # 判断一个数是不是素数
    for factor in range(2, int(num ** 0.5) + 1):
        if num % factor == 0:
            return False
    return True if num != 1 else False

"""
    practice06
    写一个程序判断输入的正整数是不是回文素数
    author:liucong
    version:0.1
    date：2021-01-07
"""
if __name__ == '__main__':
    num = int(input('请输入正整数: '))
    if is_palindrome(num) and is_prime(num):
        print('%d是回文素数' % num)





