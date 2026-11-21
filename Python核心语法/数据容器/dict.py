# 字典
# 定义字典
dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
print(dict1)
print(type(dict1))

# # key 不能重复(如果重复,后面的值会覆盖前面的值)
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688, "王林":400, "王林":80}
# print(dict1)
# print(type(dict1))

# key必须得是不可变类型(str, int, float, tuple)
dict2= {0:670, 1.3:608, (1,2):580, "韩立":688}
print(dict2)

# dict2 = {"王林":670, "李慕婉":608, "徐立国":580, ["A","B"]:688} # 不是不可变类型会报错
# print(dict2)

# 访问: 通过key获取value
print(dict1["李慕婉"])

# key不可修改, value可以修改
dict1["李慕婉"] = 688
print(dict1)


#--------------------------------常用操作----------------------------------
# dict1 = {"王林":670, "李慕婉":608, "徐立国":580, "韩立":688}
#
# # 添加 -- key不存在就是添加
# dict1["茉莉"] = 500
# print(dict1)
# #
# # 删除 -- key存在就是删除
# dict1["茉莉"] = 520
# print(dict1)
#
# # 查询
# print(dict1["茉莉"]) # 根据key获取value, 如果key不存在将会报错
# print(dict1.get("茉莉")) # 根据key获取value, 如果key不存在将会返回空值
#
# print(dict1.keys()) # 获取所有的key
# print(dict1.values()) # 获取所有的value
# print(dict1.items()) #获取所有的键值对 key:value
#
# # 删除
# score = dict1.pop("徐立国")
# print(score)
# print(dict1)
#
# del dict1["韩立"]
# print(dict1)
#
# print()
#
# # 遍历
# # 1.
# for k in dict1.keys():
#     print(f"{k}: {dict1[k]}")
#
# # 2.
# for item in dict1.items(): # dict_items([('王林', 670), ('李慕婉', 608), ('徐立国', 580), ('韩立', 688), ('茉莉', 520)])
#     print(f"{item[0]}: {item[1]}")  # item相当于一个元组
#                                     # 王林: 670
#                                     # 李慕婉: 608
#                                     # 茉莉: 520
#     # print(item) # ('王林', 670)
#                   # ('李慕婉', 608)
#                   # ('茉莉', 520)
#
#
# # 3.
# for k,v in dict1.items(): # 元组的解包
#     print(f"{k}: {v}")


#----------------------------------案例-----------------------------------
# # 开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。系统使用字典结构存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# # 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# # 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# # 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# # 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# # 5. 退出购物车
#
# shopping_cart = {"Meta80": {"price": 6999, "num": 2}, "鼠标": {"price": 199, "num": 3}}
#
# shopping_cart = {}
# # 1.制作菜单
# print("欢迎使用购物车系统~")
# menu = """
# ########### 购物车系统 ###########
# #         1. 添加购物车          #
# #         2. 修改购物车          #
# #         3. 删除购物车          #
# #         4. 查询购物车          #
# #         5. 退出购物车          #
# ################################
# """
# # 2.需要执行的操作
# while True:
#     print(menu)
#     choice = input("请输入你要执行的操作: ")
#     match choice:
#     # 1. 添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
#         case "1":
#             goods_name = input("请输入要添加的商品名称: ")
#             if goods_name in  shopping_cart:
#                 print("该商品已存在, 请重新选择~")
#                 continue
#
#             goods_price = float(input("请输入要添加的商品价格: "))
#             goods_num = int(input("请输入要添加的商品数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品选择完毕~")
#     # 2. 修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
#         case "2":
#             goods_name = input("请输入要修改的商品名称: ")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在, 请重新选择~")
#                 continue
#
#             goods_price = float(input("请输入要修改的商品价格: "))
#             goods_num = int(input("请输入要修改的商品数量: "))
#             shopping_cart[goods_name] = {"price": goods_price, "num": goods_num}
#             print("商品修改完毕~")
#     # 3. 删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
#         case "3":
#             goods_name = input("请输入要删除的商品名称: ")
#             if goods_name not in shopping_cart:
#                 print("该商品不存在, 请重新选择~")
#                 continue
#
#             del shopping_cart[goods_name]
#             print("商品删除完毕~")
#     # 4. 查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
#         case "4":
#             for goods_name in shopping_cart.keys():
#                 goods_info = shopping_cart[goods_name]
#                 print(f"商品名称: {goods_name}, 商品价格：{goods_info['price']}，商品数量：{goods_info['num']}")
#     # 5. 退出购物车
#         case "5":
#             print("Bye~")
#             break
#     # 其他操作
#         case _:
#             print("操作不支持哦,请重新输入~")


#-------------------------------------------练习-------------------------------------------
# # 开发一个教务管理系统，在该系统中可以维护和管理学员的成绩信息，具体需求如下：
# # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
# # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
# # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
# # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
# # 5. 列出所有学生：遍历所有学生信息并输出。
# # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
# # 7. 退出系统。
#
# # 结构: student_info = {"name":{"chinese":chinese_score, "math":math_score, "english":english_Score }}
# # 这个结构不行, 万一有重名的就不行了
#
# student_info = []
#
# # 制作菜单
# menu = """
# # # # # # # # # # # # # # # # # # # # # # # # # 【菜单】 # # # # # # # # # # # # # # # # # # # # # # #
# # 1. 添加学生信息  2. 修改学生信息  3. 删除学生信息  4. 查询学生信息  5.列出所有学生  6.统计班级成绩  7.退出系统 #
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# """
# while True:
#     print(menu)
#     choice = input("请输入您要选择的操作(1-7): ")
#     match choice:
# # 1. 添加学生信息：根据提示录入学生姓名、语文、数学、英语成绩，录入完成保存到系统中。
#         case "1":
#             name = input("请输入要添加学生的姓名: ")
#             chinese_score = float(input("请输入该学生要添加的语文成绩: "))
#             math_score = float(input("请输入该学生要添加的数学成绩: "))
#             english_score = float(input("请输入该学生要添加的英语成绩: "))
#
#             student = {
#                 "name": name,
#                 "chinese": chinese_score,
#                 "math": math_score,
#                 "english": english_score,
#             }
#             student_info.append(student)
#             print(student_info)
#             print("学生信息添加完毕~")
# # 2. 修改学生信息：要求输入要修改的学生姓名，然后再提示输入语文、数学、英语成绩，输入完成后修改学员信息。
#         case "2":
#             name = input("请输入要修改学生的姓名: ")
#             found = False
#             for stu in student_info:
#                 if stu["name"] == name:
#                     stu["chinese"] = float(input("请输入该学生要修改的语文成绩: "))
#                     stu["math"] = float(input("请输入该学生要修改的数学成绩: "))
#                     stu["english"] = float(input("请输入该学生要修改的英语成绩: "))
#                     print("学生信息修改完毕~")
#                     found = True
#                     break
#             if not found:
#                 print("查无此人哦~")
#
# # 3. 删除学生信息：要求输入要删除的学生姓名，根据姓名删除学生信息。
#         case "3":
#             name = input("请输入要删除学生的姓名: ")
#             found = False
#             for stu in student_info:
#                 if stu["name"] == name:
#                     student_info.remove(stu)
#                     print("学生信息删除完毕~")
#                     found = True
#                     break
#
#                 if not found:
#                     print("查无此人哦~")
# # 4. 查询学生信息：要求输入要查询的学生姓名，根据姓名查询学生信息并输出。
#         case "4":
#             name = input("请输入要查询学生的姓名: ")
#             found = False
#             for stu in student_info:
#                 if stu["name"] == name:
#                     print(f"姓名: {stu['name']}, 语文成绩: {stu['chinese']}, 数学成绩: {stu['math']}, 英语成绩: {stu['english']}")
#                     print("学生信息查询完毕~")
#                     found = True
#                     break
#
#                 if not found:
#                     print("查无此人哦~")
# # 5. 列出所有学生：遍历所有学生信息并输出。
#         case "5":
#             if not student_info:
#                 print("系统里没有该学生信息哦~")
#             else:
#                 for stu in student_info:
#                     print(f"姓名: {stu['name']}, 语文成绩: {stu['chinese']}, 数学成绩: {stu['math']}, 英语成绩: {stu['english']}")
# # 6. 统计班级成绩：统计班级语文、数学、英语成绩的最高分、最低分、平均分，以及语文、数学、英语最高分和最低分的学员姓名。
#         case "6":
#           chinese_list = [stu['chinese'] for stu in student_info]
#           max_chinese = max(chinese_list)
#           min_chinese = min(chinese_list)
#           for stu in student_info:
#               if max_chinese == stu['chinese']:
#                   print(f"语文最高分学生姓名: {stu['name']}")
#           for stu in student_info:
#               if min_chinese == stu['chinese']:
#                   print(f"语文最低分学生姓名: {stu['name']}")
#           print(f"语文最高分:{max(chinese_list)} , 语文最低分:{min(chinese_list)}, 语文平均分:{sum(chinese_list) /len(chinese_list):.1f}")
#
#           math_list = [stu['math'] for stu in student_info]
#           max_math= max(math_list)
#           min_math = min(math_list)
#           for stu in student_info:
#               if max_math == stu['math']:
#                   print(f"数学最高分学生姓名: {stu['name']}")
#           for stu in student_info:
#               if min_math== stu['math']:
#                   print(f"数学最低分学生姓名: {stu['name']}")
#           print(f"数学最高分:{max(math_list )} , 数学最低分:{min(math_list)}, 数学平均分:{sum(math_list) / len(math_list):.1f}")
#
#           english_list = [stu['english'] for stu in student_info]
#           max_english = max(english_list)
#           min_english = min(english_list)
#           for stu in student_info:
#               if max_english == stu['english']:
#                   print(f"数学最高分学生姓名: {stu['name']}")
#           for stu in student_info:
#               if min_english == stu['math']:
#                   print(f"数学最低分学生姓名: {stu['name']}")
#           print(f"英语最高分:{max(english_list)} , 英语最低分:{min(english_list)}, 英语平均分:{sum(english_list) / len(english_list):.1f}")
# # 7. 退出系统。
#         case "7":
#             print("Bye~")
#             break
# # 8. 其他操作
#         case _:
#             print("该操作不支持哦~,请重新输入选择")
# print(menu)