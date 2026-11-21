#-----------------------------------------案例----------------------------------------
# 要求输入两个数 x 与 y, 分别输出 x + y 的结果和 x - y 的结果
x = float(input("请输入x: "))
y = float(input("请输入y: "))
print(f"x + y =", x + y)
print(f"x - y =", x - y)

#-----------------------------------------练习----------------------------------------
# 1. 计算输入的三个整数的平均数
num1 = int(input("请输入第一个整数:"))
num2 = int(input("请输入第二个整数:"))
num3 = int(input("请输入第三个整数:"))
avg = (num1 + num2 + num3) / 3
print("三个整数的平均数为",avg)

# 2. 要求输入梯形的上底、下底、高，然后计算梯形的面积
top = float(input("请输入梯形的上底:"))
bottom = float(input("请输入梯形的下底:"))
h = float(input("请输入梯形的高:"))
area = (top + bottom) * h / 2
print(f"梯形的面积为{area}")

# 3. 要求输入圆的半径，然后计算圆的周长和面积（周长：2πr，面积：πr²）
import math
radius = float(input("请输入半径:"))
c = 2 * radius * math.pi
area = radius ** 2 * math.pi
print(f"圆的周长为:{c}\n圆的面积为:{area}")

# 4. 身体质量指数 BMI 的计算（BMI = 体重 (kg) / 身高 (m)²）
# 步骤:
#   1. 输入体重（单位 kg）
#   2. 输入身高（单位 m）
#   3. 计算身体质量指数 BMI 并输出
weight = float(input("请输入体重(kg):"))
height = float(input("请输入身高(m):"))
BMI = weight / height ** 2
print(f"BMI:{BMI}")

#-----------------------------------------赋值运算符---------------------------------------
# a,b,c的值分别赋值给c,a,b
a = 100
b = 200
c = 300
d = c # d = 300
c = b # c = 200
b = a # b = 100
a = d # a = 300
print(a,b,c)

# 第二个方法
a = 100
b = 200
c = 300
a,b,c = c,a,b #一行完成交换
print(a,b,c)


