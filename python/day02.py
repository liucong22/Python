"""
    practice01
    1-100间的偶数求和
    author：liucong
    date：2021-01-05
"""
# 1-100间的偶数是从2开始，步长为2，递增到100，range(2, 101, 2)
sum = 0
for i in range(2, 101, 2):
    sum += i
print(sum)

for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)


"""
    practice02
    猜数字小游戏：计算机出一个1到100之间的随机数，玩家输入自己猜的数字，计算机给出对应的提示信息（大一点、小一点或猜对了），如果玩家猜中了数字，计算机提示用户一共猜了多少次，游戏结束，否则游戏继续。
    author：liucong
    date：2021-01-05
"""
import random
res = random.randint(1, 100)
cnt = 0
while True:
    # 每次进入循环，次数+=1
    cnt += 1
    # 玩家输入数字
    num = int(input("请输入整数："))
    if num > res:
        print("小一点")
    elif num < res:
        print("大一点")
    else:
        print("猜对了")
        break
print("共猜了%d次" % cnt)


"""
    practice03
    九九乘法表
    author：liucong
    date：2021-01-05
"""
for i in range(1, 10):
    for j in range(1, i + 1):
        print("%d * %d = %d" % (i, j, i * j), end = '\t')
    print()

"""
    practice04
    输入一个正数，判断是不是素数：素数指的是只能被1和自身整除的大于1的整数
    author：liucong
    date：2021-01-05
"""
num = 0
while True:
    # 输入一个正数，判断输入
    is_prime = True
    num = int(input("请输入一个正数:"))
    if num <= 0:
        print("请重新输入！")
        continue
    # 循环判断，其是否能被非1，非自身的数整除
    for i in range(2, num + 1):
        if num % i == 0:
            is_prime = False
            break
        else:
            break
    break

# 输出结果
if is_prime and num != 1:
    print("%d是素数" % num)
else:
    print("%d不是素数" % num)

"""
    practice05
    输入两个正整数，计算它们的最大公约数和最小公倍数：最大公约数是两个数的公共因子中最大的那个数，最小公倍数则是能够同时被两个数整除的最小的那个数
    author：liucong
    date：2021-01-05
"""
# 输入两个正整数
x = int(input("x = "))
y = int(input("y = "))
# 比较两个数的大小, 若x > y, 则交换 x, y 的值
if x > y:
    x , y = y , x
for i in range(x, 0, -1):
    if x % i == 0 and y % i == 0:
        print("%d和%d的最大公因数是%d" % (x, y, i))
        print("%d和%d的最小公倍数是%d" % (x, y, x * y // i))
        break

"""
    practice06
    打印三角形图案
    author：liucong
    date：2021-01-05
"""
row = int(input("row = "))
for i in range(row):
    for j in range(i + 1):
        print("*", end = ' ')
    print()

for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end = ' ')
        else:
            print('*', end = ' ')
    print()

for i in range(row):
    for j in range(row - i - 1):
        print(' ', end = ' ')
    for j in range(2 * i + 1):
        print('*', end = ' ')
    print()




