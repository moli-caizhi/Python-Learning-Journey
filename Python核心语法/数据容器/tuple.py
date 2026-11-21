# 元组基本操作
# 定义
# t1 = (80, 95, 78, 50, 80, 85, 20)
#
# print(t1)
# print(type(t1))
#
# # 索引访问
# print(t1[0])
# print(t1[-1])
#
# # 切片
# print(t1[0:5:1])
#
# # count() 统计元素个数
# print(t1.count(80))
#
# # index() 获取元素的索引(第一个元素的位置)
# print(t1.index(80))
# print("-----------------------------------------")
#
# 定义空元组
# 注意点:如果定义单元素元组, 单个元素之后要加上逗号, 比如(100,)
# t2= ()
# print(t2)
# print(type(t2))

# ----------------------------元组的组包与解包------------------------------
# 不用小括号也可以,但推荐第一种
# t1 = (5, 7, 9, 10, 2, 23, 12)
# t2 = 5, 7, 9, 10, 2, 23, 12
#
# print(t1)
# print(t2)
#
# # 解包操作
# # 基础解包(变量数量与容器的元素个数一致)
# a, b, c, d, e, f, g = t1
# print(a, b, c, d, e, f, g)
#
# # 扩展解包(* 收集剩余的所有元素, 封装list中)
# first, second, *other, last = t1
# print(first, second)
# print(other)
# print(last)
#
# *other, last1, last2 = t1
# print(other)
# print(last1)
# print(last2)
#
# # 案例1：现有两个变量，分别为：a = 10，b = 20，现需要将这两个变量值交换，然后输出到控制台。
# a = 10
# b = 20
#
# # # 组包
# # t = b,a
# # # 解包
# # a,b = t
#
# # 合并
# a,b = b,a
#
# print(a) # 20
# print(b) # 10
#
# # 案例 2：现有三个变量，分别为：a = 100，b = 200，c = 300，
# # 现需要将这三个变量值进行交换，将 a,b,c 的值分别赋值给 c,a,b，并将其输出到控制台。
#
# a = 100
# b = 200
# c = 300
#
# c,a,b = a,b,c
#
# print(a)
# print(b)
# print(c)

#-----------------------------案例-------------------------------
# 学号	    姓名	    语文  	数学	    英语
# S001	    王林	    85	    92	    78
# S002	    李慕婉	92	    88	    95
# S003	    十三	    78	    85	    82
# S004	    曾牛	    88	    79	    91
# S005	    周轶	    95	    96	    89
# S006	    王卓	    76	    82	    77
# S007	    红蝶	    89	    91	    94
# S008	    徐立国	75	    69	    82
# S009	    许木	    86	    89	    98
# S010	    通天	    66	    59	    72
# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
# 3. 查找成绩优秀（平均分大于 90）的学生，并输出。
students = (
    ("S001", "王林", 85, 92, 78),
    ("S002", "李慕婉", 92, 88, 95),
    ("S003", "十三", 78, 85, 82),
    ("S004", "曾牛", 88, 79, 91),
    ("S005", "周轶", 95, 96, 89),
    ("S006", "王卓", 76, 82, 77),
    ("S007", "红蝶", 89, 91, 94),
    ("S008", "徐立国", 75, 69, 82),
    ("S009", "许木", 86, 89, 98),
    ("S010", "通天", 66, 59, 72)
)
# 1. 计算每个学生的总分、各科平均分，然后一并输出出来。
print("学号\t\t姓名\t\t语文\t\t数学\t\t英语\t\t平均分")
# 方式一:
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     print(f" {s[0]} \t {s[1]} \t {s[2]} \t {s[3]} \t {s[4]} \t {avg:.1f}")

# 方式二:元组的解包
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    print(f" {id} \t {name} \t {chinese} \t {math} \t {english} \t {avg:.1f}")

print()

# 2. 统计各科成绩的最低分、最高分、平均分，并输出。
chinese_score = [i[2] for i in students]

print(f"语文最低分:{min(chinese_score)}, 最高分:{max(chinese_score)}, 平均分:{sum(chinese_score)/len(chinese_score)}")

math_score = [i[3] for i in students]
print(f"数学最低分:{min(math_score)}, 最高分:{max(math_score)}, 平均分:{sum(math_score)/len(math_score)}")

english_score = [i[4] for i in students]
print(f"英语最低分:{min(english_score)}, 最高分:{max(english_score)}, 平均分:{sum(english_score)/len(english_score)}")

print()

# 3. 查找成绩优秀（平均分大于 90）的学生，并输出。
# 方式一:
print("优秀学生名单: ")
# for s in students:
#     total = s[2] + s[3] + s[4]
#     avg = total / 3
#     if avg > 90:
#         print(f"学号: {s[0]} \t 姓名: {s[1]}\t平均分: {avg:.1f}")

# 方式二:
for id,name,chinese,math,english in students:
    total = chinese + math + english
    avg = total / 3
    if avg > 90:
        print(f"学号: {id} \t 姓名: {name}\t平均分: {avg:.1f}")


