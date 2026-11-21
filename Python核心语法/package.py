# 1.导入包中模块的所有功能

#   语法: import 包名.模块名 --> 调用方式: 包名.模块名.功能名
# import utils.my_line
#
# utils.my_line.log_separator1()
# utils.my_line.log_separator2()

#   语法: from 包名 import 模块名 --> 调用方式: 模块名.功能名
# from utils import my_line
#
# my_line.log_separator1()
# my_line.log_separator2()

# 2. 导入包中所有模块的功能(如果要所有模块的功能 __all__ = [], [] 中要写所有模块, 否则只导入你所写的模块)
# 注意: 如果要通过 from utils import * 导入包下所有模块, 需要 __init__.py 文件中添加 __all__ = ["模块名"]
#   语法: from 包名 import * --> 调用方式: 模块名.功能名
# from utils import *
#
# my_line.log_separator1()
# my_line.log_separator2()
# print(my_var.PI)
# print(my_var.NAME)

#   语法: from 包名.模块 import * --> 调用方式: 功能名
# from utils.my_line import *
#
# log_separator2()
# log_separator3()

# 3. 导入包中模块的具体功能
# 语法: from 包名.模块 import 所要导入的功能 --> 调用方式: 功能名
# 相对路径: 从当前文件所在目录开始查找
# from utils.my_line import log_separator1, log_separator2
#
# log_separator1()
# log_separator2()

# 注意: package.py 要和 包在同一目录下, 否则报错, (我的不管放在哪个文件夹都没报错, 不知道为什么)
# 如果报错, 解决方法一:
# 绝对路径: 从项目的根目录下开始查找
# from Python核心语法.utils.my_line import log_separator1, log_separator2
#
# log_separator1()
# log_separator2()

