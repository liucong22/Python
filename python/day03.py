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

"""
    practice02
    正整数的反转：1234，4321
    author：liucong
    date：2021-01-06
"""
num = int(input("num = "))
# 将正整数进行反转，1234反转=1*1 + 2*10 + 3*100 + 4*1000;个位，个位+10位
res = 0
while num > 0:
    res = res * 10 + num % 10
    num = num // 10
print(res)

"""
    practice03
    白钱白鸡：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
    author：liucong
    date：2021-01-06
"""
# 100元买5元一只的鸡20只；3元一只的鸡33只；1元3只的鸡300只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print("公鸡%d只，母鸡%d只，小鸡%d只" % (x, y, z))









