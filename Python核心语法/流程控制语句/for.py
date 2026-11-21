msg = input("请输入需要遍历的字符串:")
for char in msg:
    print(f"元素:{char}")
else:
    print("遍历结束!")


#计算1-100之间所有奇数之和
# total = 0
#
# for i in range(1,101):
#     if i % 2 == 1:
#         total += i

# print(f"1-100之间所有奇数之和: {total}")

#简化:
# total = 0
#
# for i in range(1,101,2):
#         total += i

# print(f"1-100之间所有奇数之和: {total}")


#计算100-500之间所有3的倍数的数字之和
# total = 0
#
# for i in range(100,501):
#     if i % 3 ==0:
#         total += i
#
# print(f"计算100-500之间所有3的倍数的数字之和: {total}")


#循环嵌套:根据输入的长方形的长度 m,宽度 n,打印一个长方形:
# 长度为 10, 宽度为 5
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *
#    *  *  *  *  *  *  *  *  *  *

# m = int(input("请输入长方形的长度: "))
# n = int(input("请输入长方形的宽度: "))
# for j in range(n):
#     for i in range(m):
#         print("*", end ="  ")
#     print()


#打印九九乘法表
# for i in range(1,10):
#     for j in range(1,i+1):
#         print(f"{j} x {i} = {j * i}",end="\t")
#     print()


#打印直角边为五的等腰直角三角形
# *
# *  *
# *  *  *
# *  *  *  *
# *  *  *  *  *

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end="  ")
#     print()


#打印数字金字塔
# 1
# 1  2
# 1  2  3
# 1  2  3  4
# 1  2  3  4  5
# 1  2  3  4  5  6

# for i in range(1,7):
#     for j in range(1,i+1):
#         print(j,end="\t")
#     print()


#打印
# 1   2   1   2   1   2   1   2
# 2   1   2   1   2   1   2   1
# 1   2   1   2   1   2   1   2
# 2   1   2   1   2   1   2   1
# 1   2   1   2   1   2   1   2
# 2   1   2   1   2   1   2   1
# 1   2   1   2   1   2   1   2
# 2   1   2   1   2   1   2   1

# for i in range(1,9):  # i 行：1~8
#     for j in range(1,9): # j 列：1~8
#         if i % 2 == 1:
#             # 奇数行：奇数列是1，偶数列是2
#             if j % 2 == 1:
#                 print(1, end="\t")
#             else:
#                 print(2, end="\t")
#         else:
#             # 偶数行：奇数列是2，偶数列是1
#             if j % 2 == 1:
#                 print(2, end="\t")
#             else:
#                 print(1, end="\t")
#     print()


#将1-1000之间所有五的倍数的数字累加起来
# total = 0
# for i in range(1,1001):
#     if i % 5 == 0:
#         total += i
# print(f"1-1000之间所有五的倍数的数字累加之和为{total}")


#统计字符串 "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd" 字符串中有多少个 a 和 k
# msg = "akiwksjakdiklowiqaamnvbamvaxnsjdsjkaaxkjd"
# j = 0
# for i in msg:
#     if i == "a" or i == "k":
#         j += 1
# print(f"共有{j}个a和k")


