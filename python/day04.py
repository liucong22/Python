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

