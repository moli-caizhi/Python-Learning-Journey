#-------------------------------------函数的参数与返回值--------------------------------
# 函数的定义
# 注意: 函数定义的时候并不会执行, 只有在调用函数的时候, 函数体的逻辑才会执行; 函数必须先定义后调用

# 1. 语法: --> 无参数列表
# def 函数名():
#     函数体
#     ...

# 调用函数
# 函数名() --> 也是输出, 不用 print

def out_line():
    print("-------------------------")
    print("-------------------------")

# 函数调用
out_line()

# 2. 语法: --> 有参数列表
# def 函数名(参数列表):
#     函数体
#     ...
#
#     return 返回值 --> return 语句只有返回功能, 而没有输出打印的功能, 如果要输出, 需要结合 print() 函数来实现

# 调用函数
# 函数名(参数)

# 输出
# print(函数名(参数))
def circle_area(r):

    area = 3.14 * r ** 2
    return area

# 调用函数
c_area = circle_area(10)
print(c_area)

print(circle_area(10)) # 可以不用重新定义变量接收, 直接调用输出


#------------------------------函数说明文档-----------------------------------
# 函数1: 计算圆的面积
# def circle_area(r):
#     """
#     根据圆的半径, 计算圆的面积
#     :param r: 半径
#     :return: 圆的面积
#     """
#     area = 3.14 * r ** 2
#     return area
#
# c_area = circle_area(10.)
# print(c_area)
#
# # 函数2: 计算长方形的面积
# def rectangle_area(l,w): # 函数定义时如果有多个参数,多个参数之间用 , 分格
#     """
#     根据长方形的长度和宽度, 计算长方形的面积
#     :param l: 长度
#     :param w: 宽度
#     :return: 长方形的面积
#     """
#     area = l * w
#     return area
#
# help(rectangle_area) # 调用 help() 内置函数来查看说明文档
#
# print(rectangle_area(20,10))
#
#
# # 函数3: 计算圆的面积和周长 -->如果返回值有多个, 多个返回值之间用逗号分隔 --> 多个返回值会封装到元组之中
# # round(number, ndigits) 内置函数, number: 为表达式, ndigits: 你要保留的小数位数(1为保留一位, 2为两位...)
# def circle_area_len(r):
#     """
#     根据圆的半径, 计算圆的面积和周长
#     :param r: 半径
#     :return: 圆的面积, 圆的周长
#     """
#     return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)
# al = circle_area_len(10)
# print(al)
# print(type(al))
#
# area, len = circle_area_len(10) # 解包
# print(area)
# print(len)


#------------------------------------函数的嵌套调用---------------------------------------
# # 函数的调用遵循栈的结构, 最后被调用的函数最先返回(后进先出)
# def function_a():
#     print("a ... before")
#     function_b()
#     print("a ... after")
#
# def function_b():
#     print("b ... before")
#     function_c()
#     print("b ... after")
#
# def function_c():
#     print("c ... ")
#
# function_a()
#
# print("函数调用完毕~")


#-------------------------------------案例--------------------------------------
# # 1. 定义一个函数：根据传入的底和高计算三角形面积的函数（三角形面积 = 底 × 高 / 2）。
# def triangle_area(b, h):
#     """
#     根据三角形的底和高, 计算三角形的面积
#     :param b: 底
#     :param h: 高
#     :return: 三角形的面积
#     """
#     area = b * h / 2
#     return area
# print("底为4, 高为2的三角形的面积为: ", triangle_area(4, 2))
#
# # 2. 定义一个函数：计算传入的字符串中元音字母的个数（元音字母为 aeiouAEIOU）。
# def count_aeiou(s):
#     """
#     统计字符串中元音字母的个数
#     :param s: 字符串
#     :return: 元音字母的个数
#     """
#
#     num = 0
#     for w in s:
#         if w in 'aeiouAEIOU':
#             num += 1
#     return num
# print(count_aeiou("Hello World Hello Python OK"))
#
# # 3. 定义一个函数：计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分 (保留 1 位小数)，并返回。
# def calc_score(score_list):
#     """
#     计算传入的班级学员高考成绩列表中成绩的最高分、最低分、平均分 (保留 1 位小数)
#     :param score_list: 传入的班级学员高考成绩列表
#     :return: 最高分、最低分、平均分
#     """
#     max_s = max(score_list)
#     min_s = min(score_list)
#     avg_s = round(sum(score_list) / len(score_list), 1)
#     return max_s, min_s, avg_s
#
# s_list= [690, 609, 407, 509, 700, 409, 300, 500]
# max_score, min_score, avg_score = calc_score(s_list) # 解包
# print(f"最高分: {max_score}, 最低分{min_score}, 平均分{avg_score}")


#----------------------------------------练习-----------------------------------------
# 1. 定义一个函数，根据传入的分数，计算对应的分数等级并返回。
#     分数 >= 90：A
#     分数 >= 75：B
#     分数 >= 60：C
#     分数 < 60：D
def score_grade(score):
    """
    根据传入的分数，计算对应的分数等级
    :param score: 传入的分数
    :return: 返回对应的等级
    """
    if score >= 90:
        return "A"
    elif score >= 75:
        return "B"
    elif score >= 60:
        return "C"
    else:
        return "D"
s = int(input("请输入要传入的成绩: "))
print("传入的分数等级为: ", score_grade(s))

# 2. 定义一个函数，用于判断一个字符串是否是回文串，返回 bool 值。
# 把字符串反转，如果和原字符串相同，就是回文串。（如："level"，"radar"，"黄山落叶松叶落山黄"）
def is_palindrome(s):
    """
    判断一个字符串是否是回文串，返回 bool 值
    :param s: 输入的字符串
    :return: 返回 bool 值
    """
    # if s == s[::-1]:
    #     return True
    # else:
    #     return False

    return s == s[::-1] # 可以精简为一行, s == s[::-1] 计算出来的就是布尔值

st = input("请输入字符串: ")
print(is_palindrome(st))

# 3. 定义一个函数：完成时间转换功能，将传入的秒转换为小时、分钟、秒。
def convert_second(s):
    # 计算小时
    hour = s // 3600
    # 计算分钟, 先去掉小时占用的秒数(s % 3600)
    minute = s % 3600 // 60
    # 计算秒数
    second = s % 60

    return f"{hour}小时{minute}分钟{second}秒"

sec = int(input("请输入秒: "))
print(f"{sec}为{convert_second(sec)}")

# 4. 定义一个函数：根据传入的三角形三个边的边长，判定三角形的类型（等边、等腰、普通，或者不能构成三角形）。
def get_triangle_type(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return f"边长为{a},{b},{c},不能构成三角形"

    if a == b == c:
        return f"边长为{a,}{b},{c}构成等边三角形"

    elif a == b or b == c or c == a:
        return f"边长为{a},{b},{c}构成等腰三角形"

    else:
        return f"边长为{a},{b},{c}构成普通三角形"
print(get_triangle_type(1, 2, 3))

