"""
    practice01
    将华氏温度转化成摄氏温度
    华氏温度到摄氏温度的转换公式为：$C=(F - 32) \div 1.8$
    author：liucong
    date：2021-01-04
"""
# 输入华氏温度 
F = float(input("F = "))
# 根据公式计算摄氏温度
C = (F - 32) / 1.8
# 输出摄氏温度
print("C = %f" % C)


"""
    practice02
    输入圆的半径计算计算周长和面积
    author：liucong
    date：2021-01-04
"""
import math
# 输入圆的半径
r = float(input('r = '))
# 根据公式计算圆的周长和面积
C = 2 * math.pi * r
S = math.pi * (r ** 2)
# 输出圆的周长和面积
print("C = %f" % C)
print("S = %f" % S)

"""
    practice03
    输入年份判断是不是闰年
    author：liucong
    date：2021-01-04
"""
# 输入年份
year = int(input("year = "))
# 判断是否为闰年：
#   普通年能被4整除且不能被100整除的为闰年
#   世纪年能被400整除的是闰年
res = ''
if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    res = '是闰年'
else:
    res = '不是闰年'
# 输出结果
print(res)


"""
    practice04
    分段函数求值:
		    3x - 5	(x > 1)
    f(x) =	x + 2	(-1 <= x <= 1)
		    5x + 3	(x < -1)
    author：liucong
    date：2021-01-04
"""
x = float(input('x = '))
if x > 1:
    fx = 3 * x -5
elif x >= -1:
    fx = x + 2
else:
    fx = 5 * x + 3
print(fx)


"""
    practice05
    百分制成绩转换为等级制成绩:
    要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；
    70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
    author：liucong
    date：2021-01-04
"""
score = float(input('score = '))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')

"""
liucong01
"""
