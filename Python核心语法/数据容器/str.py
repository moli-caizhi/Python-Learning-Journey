# #字符串基本操作  -->不可变的(无法修改),有序性,可迭代性
# s = "Hello-Python"
#
# print(s[4]) #o(正向索引)
# print(s[-8]) #o(反向索引)
#
# for i in s:
#     print(i)
# print("----------------------------------------")
# #---------------------------切片----------------------------------
# # Hello
# print(s[0:5:1])
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print("----------------------------------------")
#
# #Python
# print(s[6:12:1])
# print(s[6::1])
# print("----------------------------------------")
#
# # 步长 ---> 正数: 从前往后截取,负数: 从后往前截取
# # 总之开始索引到结束索引的方向要和步长方向一致才有输出
# print(s[0:5:2]) # Hlo
#
# # 没有输出任何结果, 因为0:5是从索引为0的位置到索引为五的位置,指定了开始和结束
# # 而最后的步长为-1,是从后往前截取,方向冲突,所以没有输出然任何结果
# print(s[0:5:-1])
#
# print(s[-1:4:-1]) # nohtyP-
#
# #反转字符串
# print(s[-1:-13:-1]) # nohtyP-olleH
# print(s[::-1]) #nohtyP-olleH


#--------------------str常用方法--------------------
s = "  Hello-Python-Hello-Python  "
# # find()查找指定字符串第一次出现的索引位置
# index = s.find("-")
# print(index)
#
# # count() 统计子字符串在指定字符串中出现的次数
# c = s.count("o")
# print(c)
#
# # upper() 转为大写
# su = s.upper()
# print(su)
#
# # lower() 转为小写
# sl = s.lower()
# print(sl)
#
# # split() 将字符串按照指定切割 -- 列表
slist = s.split("-") # ['  Hello', 'Python', 'Hello', 'Python  ']
print(slist)

for i in slist:
    print(i) #  Hello
             # Python
             # Hello
             # Python



# strip() 去除字符串两端空格
# ss = s.strip()
# print(ss)
#
# # replace() 将字符串中的指定字串替换为新内容
# sr = s.replace("-", "_")
# print(sr)
# print(s)
#
# # startswith() / endswith() 判断字符串是否以指定的字符串开头 / 结尾返回布尔值
# print(s.startswith("  Hello"))
# print(s.endswith("Python  "))

#----------------------------案例-----------------------------
# 邮箱格式验证：用户输入一个邮箱，验证邮箱格式是否正确
# (包含一个 @和至少一个.)，如果输入正确，输出 "邮箱格式正确"，否则输出 "邮箱格式错误"。

# 1.接收用户输入的邮箱
# mail = input("请输入邮箱: ")
#
# # 2.判断邮箱格式是否正确
# # 方式一:
# # if mail.count("@") == 1 and mail.count(".") >= 1:
# #     print("邮箱格式正确")
# # else:
# #     print("邮箱格式错误")
#
# # 方式二:
# if mail.count("@") == 1 and "." in mail:
#     print("邮箱格式正确")
# else:
#     print("邮箱格式错误")


#----------------------------练习-----------------------
# 1.输入一个字符串,判断该字符串是否是回文(两边对称)
# 黄山落叶松叶落山黄
# 上海自来水来自海上

# 1.接收输入的字符串
# s = input("请输入字符串: ")
#
# 2.判断是否为回文
# if s[0:2:1] == s[-1:-3:-1]:
#     print(f"{s} 是回文")
# else:
#     print(f"{s} 不是回文")


# 2.将用户输入的10个字符串,反转后全部转换为大写,然后记录在列表中,最后将列表内容,遍历输出出来

# 1.接收用户输入的字符串
# s = input("请输入10个字符串: ")
# # 2.将字符串反转,全部转换为大写 upper()
# new_str = s[::-1].upper()
# print(new_str)
# # 3.记录在列表中 list
# list1 = [new_str]
# # 4.将列表内容,遍历输出出来 for
# for i in list1:
#     print(f"元素: {i}")