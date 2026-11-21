# 捕获异常
# 语法:
# try:
#     可能出现异常的业务代码1
#     可能出现异常的业务代码2
#     ...
# except 异常类型 as 变量名:
#     出现异常的预案
# finally:
#     不管是否出现异常, 都会执行的代码

# try:
#     print("=============================")
#     print(my_name)
#     print( 1 / 0 )
#     print("ABC".hello)
#     print("=============================")
# # except NameError as e: # 捕获特定的异常
# #     print("程序运行出错了, 请联系管理员. 异常信息: ", e)
#
# # 捕获所有类型的异常, 只能捕获一个, 捕获完异常, 后续代码将不执行, 如果后续有异常, 是不会捕获的
# except Exception as e:
#     print("程序运行出错了, 请联系管理员. 异常信息: ", e)
#
# finally: # 无论程序是否正常运行, finally 代码块中的代码都会执行
#     print("释放资源")

#----------------------------------------异常的传递-----------------------------------------
# 异常的传递 --> 在主程序中处理更合适
def fun1():
    print("fun1 ... running ...")
    fun2()

def fun2():
    print("fun2 ... running ...")
    fun3()

def fun3():
    print("fun3 ... running ...")
    print(my_color)

if __name__ == '__main__':
    try:
        fun1()
    except Exception as e:
        print("程序运行出错了，请联系管理员，错误信息：", e)


