#列表操作
s = [56, 90, 88, 65, 90, "A", "Hello", True]
#
# print(type(s))
#
# #获取元素
# print(s[0]) #正向索引,从0开始
# print(s[-8]) #反向索引,从-1开始
#
# #修改
# s[5] = "ABC"
# print(s)
#
# #注意:如果指定的索引,超出范围,将会报错: list assignment index out of range
# #s[10] = 100
# #print(s)
# #删除
# del s[6]
# print(s)
#
#遍历(有序)
for item in s:
    print(item)


#-----------------列表切片--------------------
# s = ["A", "S","D", "F", "G", "H", "K", "L"]
#
# #切片操作 s[开始索引:结束索引:步长]
# print(s[0:5:1])
# print(type(s[0:5:1]))
#
# #简写:因为从0开始索引,步长为1
# print(s[:5:1])
# print(s[:5:])
# print(s[:5])
#
# print(s[0:5:2])
#
# print(s[0:-2:1]) #正,反索引混用


#-------------------列表list常用方法-------------------
# s = [56, 90, 88, 65, 90, 100, 209, 72, 145]
# print(s)
#
# # append(): 在列表尾部追加元素
# s.append(188)
# print(s)
#
# # insert(): 在指定索引之前,加入元素
# s.insert(2,80)
# print(s)
#
# # remove(): 移除列表中第一个匹配到的元素
# s.remove(90)
# print(s)
#
# # pop(): 删除列表中指定索引位置的元素并返回(如果未指定,默认删除最后一个)
# e = s.pop(1)
# print(e)
#
# e = s.pop()
# print(e)
#
# print(s)
#
# # sort(): 排序
# s.sort()
# print(s)
#
# # reverse(): 反转列表元素
# s.reverse()
# print(s)


#----------------------列表list案例-------------------------
# 案例1: 将用户输入的10个数字,存储到一个列表中,
# 并将列表的数字进行排序, 输出最小值, 最大值和平均值

# 1.定义列表
# num_list = []
#
# 2.将用户将用户输入的10个数字,存储到一个列表中
# for i in range(10):
#     num = int(input("请输入一个数字: "))
#     num_list.append(num)
# print("数字列表: ", num_list)
#
# # 3.将列表的数字进行排序 输出最小值, 最大值和平均值
# num_list.sort()
# print("排序后的数字列表: ", num_list)
#
# # 输出最小值, 最大值和平均值
# # sum()求和, len() 获取元素的个数(列表长度)
# print(f"最小值为{min(num_list)}, 最大值为{max(num_list)}")
# print(f"平均值为{sum(num_list)/len(num_list)}")


# 案列2: 合并两个列表中的元素，并对合并的结果进行去重处理 (去除列表中的重复元素)。
# num_list1 = [19, 23, 54, 64, 875, 20, 109, 232, 123, 54]
# num_list2 = [55, 80, 72, 35, 60, 123, 54, 29, 91]
#
# # 1.合并列表(我写的,写的有点臃肿了)
# # new_list = []
# # for num in num_list2:
# #     new_list.append(num)
# # print(new_list)
# # for num in num_list2:
# #     new_list.append(num)
# # print(new_list)
#
# # 1.合并列表(不推荐用,如果元素过多,就要循环很多次)
# # for num in num_list2:
# #     num_list1.append(num)
# # print("合并后的列表: ", num_list1)
#
# # 1.合并列表
# # 解包: 将列表这一类容器解开成一个一个独立的元素
# # 组包: 将多个值合并到一个容器
# # num_list = [*num_list1, *num_list2]
#
# # 1.合并列表:
# num_list = num_list1 + num_list2
#
# # 2.去除重复的元素
# new_list = [] # 去除重复记录后的列表
# for num in num_list:
#     if num not in new_list: # in: 判断元素是否在于列表中, 如果存在, 则返回True; 不存在, 返回False
#         new_list.append(num)
# print("去除重复后元素后的列表: ", new_list)


# 案例3: 生成1-20的平方列表

# 方式一:传统方式
# num_list = []
# for num in range(1,21):
#     num_list.append(num ** 2)
# print("1-20的平方列表", num_list)
#
# # 方式二: 列表推导式 --> 就是按照一定的规则快速生成一个列表的方法
# # 语法格式: [要插入的值 for num in 序列/列表]
# num_list2 = [num**2 for num in range(1,21)]
# print("1-20的平方列表", num_list2)


# 案列四: 从一个数字列表中提取所有偶数, 并计算其平方, 组成一个新的列表

# 列表推导式 --> 就是按照一定的规则快速生成一个列表的方法
# 语法格式2: [要插入的值 for num in 序列/列表 if 条件]
# num_list = [12, 32, 45, 77, 80, 92, 33, 57, 97, 98]
# new_list = [i**2 for i in num_list if i % 2 == 0]
# print(new_list)


#-------------------------练习----------------------------
# 1.将如下多个列表合并为一个列表，并去重重复元素，排好序（升序）后输出到控制台。
# 合并如下三个列表，并对合并后的列表进行元素的去重，然后排好序后输出到控制台
# list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
# list2 = ['X', 'Z', 'T', 'Y', 'D', 'E', 'F', 'G']
# list3 = ['W', 'A', 'S', 'D']
# new_list = list1 + list2 + list3
# print("合并后的列表: ", new_list)
# new_list2 = []
# for i in new_list:
#     if i not in new_list2:
#         new_list2.append(i)
# new_list2.sort()
# print("去重并且升序后的列表为: ",new_list2)


# 2.将如下列表中能被 3 或 5 整除的元素提出来，并获取这些数字对应的平方，组成一个新的列表。
# list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
# new_list = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
# print("能被 3 或 5 整除的元素的平方的列表为: ", new_list)


# 3.将如下列表中的正数提取出来，封装为一个新的列表。
# list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
#
# new_list = [i for i in list1 if i > 0]
# print("只有正数的列表为: ", new_list)