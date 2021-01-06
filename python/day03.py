"""
    practice01
    寻找水仙花数：一个3位数，该数字每个位上数字的立方之和正好等于它本身，例如：$1^3 + 5^3+ 3^3=153$。
    author：liucong
    date：2021-01-06
"""

# 判断一个数是不是水仙花数，拿出这个数字的每个位，用立方和相加
for num in range(100, 1000):
    low = num % 10
    mid = num // 10 % 10
    high = num // 100
    if num == low ** 3 + mid ** 3 + high ** 3:
        print(num)





