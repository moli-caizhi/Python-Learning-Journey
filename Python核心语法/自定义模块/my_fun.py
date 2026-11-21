# __all__ 指定的是 from ... import * 导入的是哪些功能(规范: 文件开头写)
__all__ = ['log_separator1',  'log_separator3', "PI", "NAME"]


# 常量(不会发生变化的数据; 常量的名称全部大写)
PI = 3.14159
NAME = "茉莉 * 彩脂"

# 字符串乘以一个整数, 表示把这个字符串重复 N 次
def log_separator1():
    print("-" * 30) # " - "重复输出 30 次

def log_separator2():
    print("+" * 30)

def log_separator3():
    print("#" * 30)

def log_separator4():
    print("*" * 30)

# 测试函数

# 1. __name__: Python中的内置变量, 表示当前模块的名字;
# 2. 直接运行当前模块, __name__的值为"__main__";
# 3. 当该模块被导入时,运行导入模块的文件, __name__的值就是导入的模块名;

# print(__name__)

# 4. 运行当前文件, 则会执行如下代码; 如果被当作模块导入,运行导入模块的文件, 如下代码不执行
if __name__ == '__main__': # 快捷方式: 输入 main 回车
    log_separator1()



