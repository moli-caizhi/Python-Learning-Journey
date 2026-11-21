#--------------------------------------字面量--------------------------------------------
# 字面量的写法
print(100) # 整数类型(int)
print(3.14) # 浮点数/小数(float)

print(True)
print(False) # 布尔(bool),首字母必须大写

print("Hello Python") # 字符串(str),必须使用引号引起来

print(None) # 空值(NoneType)

# 布尔类型本质也是整数类型（True -- 1, False -- 0）
print(True + 1) # 2
print(False - 1) # -1


# ----------------------------------------变量----------------------------------------
# 变量的定义
num = 100

#-----------------------------------------案例----------------------------------------
# B 站课程播放量
# 课程基础播放量为：20.7 万
# 每月新增播放量为：50 万
# 请输出未来两个月每个月的播放总量？

base = 20.7
incr = 50
print("未来第一个月的播放总量:",base + incr) # Ctrl + D 快速复制一行
print("未来第二个月的播放总量:",base + incr + incr)

# 一次定义多个变量
base,incr = 20.7,50
print("未来第一个月的播放总量:",base + incr) # Ctrl + D 快速复制一行
print("未来第二个月的播放总量:",base + incr + incr)

# 变量值的交换, 交换 a 和 b
a = 10
b = 20
c = a # c = 10
a = b # a = 20
b = c # b = 10
print("a的值为: ", a, "b的值为: ", b)

#-------------------------------------------常见的的数据类型-----------------------------
# type() 获取指定字面量或变量的数据类型
print(type("hello"))
print(type("10"))
print(type("3.14"))
print(type("True"))
print(type("False"))
print(type("None"))

num = 10
print(type(num))

# isinstance(数据,类型) --> 判定数据类型是否为指定类型,如果是:True,否则:False
print(isinstance(num,int))
print(isinstance(num,float))
print(isinstance(num,bool))
