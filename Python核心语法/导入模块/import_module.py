#-------------------------------------------模块--------------------------------------------
"""
    1. 导入模块(所有功能):
    语法: import 模块名 --> 调用方式: 模块名.功能名 / 别名.功能名
    语法: import 模块名 as 别名 --> 调用方式: 别名.功能名
    语法: from 模块名 import *  --> * 是通配符

    2. 导入模块中的功能(某一个或者多个功能):
    语法: from 模块名 import 功能名 -->  调用方式: 功能名
    语法: from 模块名 import 功能名 as 别名(功能名的别名) -->  调用方式: 别名
"""
# 1. 导入模块(所有功能)
# 规范: 导入的模块一般在 Python 文件的开头

# 生成 100 个随机数

# 语法: import 模块名 --> 调用方式: 模块名.功能名 / 别名.功能名
# import random
# for i in range(100): # 循环 100 次
#
#     print(random.randint(1,100)) # randint: 生成一个 int 类型的随机数
#                                       # a: star, b: end (包含star也包含end)
#
#
# 语法: import 模块名 as 别名 --> 调用方式: 别名.功能名
# import random as rd
# for i in range(100):
#     print(rd.randint(1, 100))


# 2. 导入模块中的功能(某一个或者多个功能)
# 语法: from 模块名 import 功能名 -->  调用方式: 功能名
# from random import randint
# for i in range(100):
#     print(randint(1, 100))

# 语法: from 模块名 import 功能名 as 别名(功能名的别名) -->  调用方式: 别名
# from random import randint as rint
# for i in range(100):
#     print(rint(1, 100))

# 3. 导入模块中的所有功能
# 语法: from 模块名 import *  --> * 是通配符
# 调用方式: 需要调用的具体功能名
from random import *
for i in range(100):
    print(randint(1, 100))