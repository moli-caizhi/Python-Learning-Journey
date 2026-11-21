# i = 0
# while i < 10:
#     print("人生苦短,我用Python")
#     i+=1
# else:
#     print("循环正常结束")

#计算1-100之间所有偶数的累加之和
# total = 0
# i = 1
# while i <= 100:
#     if i % 2 == 0 :
#         total += i
#     i += 1
# print(f"1-100之间所有偶数的累加之和{total}")

#需求：根据输入的用户名密码执行登录操作，具体要求如下：
# 正确的用户名和密码为 admin/666888 、zhangsan/123456、taoge/888666
# 输入用户名和密码进行登录，直到登录成功，程序结束运行；如果登录失败，则继续输入用户名和密码进行登录
# 输入的用户名和密码不能为空！
# 登录成功：输出 "登录成功，进入 B 站首页～"
# 登录失败：输出 "用户名或密码错误，请重新输入！"
# while True:
#
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空! 请重新输入!")
#         continue #结束当前循环,直接进入下一轮循环
#
#     if username == "admin" and password == "666888":
#         print("登录成功,欢迎进入B站首页~")
#         break #跳出循环
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功,欢迎进入B站首页~")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功,欢迎进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误,请重新输入!")


#需求：用户名密码登录，正确的用户名和密码为 admin/666888 、zhangsan/123456、taoge/888666，
# # 5 次登录机会，输入错误五次，不允许再操作了。
# i = 1
# while i <= 5:
#
#     username = input("请输入用户名: ")
#     password = input("请输入密码: ")
#
#     if username == "" or password == "":
#         print("输入的用户名和密码不能为空! 请重新输入!")
#         i += 1
#         continue #结束当前循环,直接进入下一轮循环
#
#     if username == "admin" and password == "666888":
#         print("登录成功,欢迎进入B站首页~")
#         break #跳出循环
#     elif username == "zhangsan" and password == "123456":
#         print("登录成功,欢迎进入B站首页~")
#         break
#     elif username == "taoge" and password == "888666":
#         print("登录成功,欢迎进入B站首页~")
#         break
#     else:
#         print("用户名或密码错误,请重新输入!")
#     i += 1
#
# else:
#     print("输入错误五次,不允许再操作了")


#猜数字游戏
# 系统随机生成一个随机数
# 用户根据提示猜数字，并将所猜的数字输入系统
# 如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
# 如果猜对，系统自动退出，游戏结束

# import random
# num_random = random.randint(1,100)
# while True:
#     number = int(input("请输入你猜的数字: "))
#     if number > num_random:
#         print("你输入的数字大了")
#     elif number < num_random:
#         print("你输入的数字小了")
#     else:
#         print("恭喜你猜对了!真棒~")
#         break






