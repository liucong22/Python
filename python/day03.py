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
    百钱百鸡：公鸡5元一只，母鸡3元一只，小鸡1元三只，用100块钱买一百只鸡，问公鸡、母鸡、小鸡各有多少只？
    author：liucong
    date：2021-01-06
"""
# 100元买5元一只的鸡20只；3元一只的鸡33只；1元3只的鸡300只
for x in range(20):
    for y in range(33):
        z = 100 - x - y
        if x * 5 + y * 3 + z / 3 == 100:
            print("公鸡%d只，母鸡%d只，小鸡%d只" % (x, y, z))

"""
    practice04
    CRAPS赌博游戏:
    玩家第一次摇骰子如果摇出了7点或11点，玩家胜；
    玩家第一次如果摇出2点、3点或12点，庄家胜；
    其他点数玩家继续摇骰子，如果玩家摇出了7点，庄家胜；
    如果玩家摇出了第一次摇的点数，玩家胜；
    其他点数，玩家继续摇骰子，直到分出胜负。
    author：liucong
    date：2021-01-06
"""
from random import randint

money = int(input("请输入资产："))
while money > 0:
    print("你的总资产为%d" % money)
    needs_go_on = False
    while True:
        debt = int(input("请下注："))
        if 0 < debt <= money:
            break
    # randint(a,b) [a, b]；range(a,b) [a, b)
    first = randint(1, 6) + randint(1, 6)
    print('玩家摇出了%d点' % first)
    if first == 7 or first == 11:
        print("玩家胜！")
        money += debt
    elif first == 2 or first == 3 or first == 12:
        print("庄家胜！")
        money -= debt
    else:
        needs_go_on = True
    while needs_go_on:
        needs_go_on = False
        current = randint(1, 6) + randint(1, 6)
        print('玩家摇出了%d点' % current)
        if current == 7:
            print("庄家胜！")
            money -= debt 
        elif current == first:
            print("玩家胜！")
            money += debt
        else:
            needs_go_on = True
print("你破产了，游戏结束")

"""
    practice05
    生成斐波那契数列的前20个数：
    斐波那契数列的特点是数列的前两个数都是1，从第三个数开始，每个数都是它前面两个数的和，形如：1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, ...
    author：liucong
    date：2021-01-07
"""

"""
    practice06
    找出10000以内的完美数：
    它的所有的真因子（即除了自身以外的因子）的和（即因子函数）恰好等于它本身；例如：6（$6=1+2+3$）和28（$28=1+2+4+7+14$）就是完美数
    author：liucong
    date：2021-01-07
"""

"""
    practice07
    输出100以内所有的素数：
    素数指的是只能被1和自身整除的正整数（不包括1）
    author：liucong
    date：2021-01-07
"""










