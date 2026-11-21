#-----------------------------------函数变量的作用域-------------------------------
# 全局变量: 在函数外部 或 函数内部都是可以访问的
num = 100

#定义函数
def circle_area(r):
    # 局部变量: 只能在函数中使用
    pi = 3.14
    area = pi * r * r
    # print("num = ", num) # num =  100

# global 关键字用于明确的告诉 Python 解释器, 在函数中要使用全局变量, 使得可以在函数内部修改全局变量的值
# 不建议使用 global 关键字, 在项目中容易出现 bug, 数据乱套, 造成代码污染
    global num
    num = 1000
    # num = 10000
    # print("num = ", num) #num =  10000

    return area

# 报错, 都是为解析的引用, 因为都是局部变量, 只能在函数之中使用
# print("pi = ", pi)
# print("area = ", area)
# print("r =", r)

# 调用函数
c_area = circle_area(10)
print(c_area)

print("num = ", num) # num =  1000


#--------------------------------- 函数 - 传参方式 -------------------------------
# 定义函数
def reg_stu(name, age, gender, city):
    print(f"注册成功, 姓名: {name}, 年龄:  {age}, 性别:  {gender}, 城市:  {city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 传参方式一: 位置传参(严格按照位置顺序)
stu = reg_stu("张三", 18, "男", "北京")
print(stu)

# 传参方式二: 关键字传参(顺序随便)
stu = reg_stu(name = "茉莉", age = 20, gender = "女", city = "北京")
print(stu)

stu = reg_stu(gender = "女", city = "北京", name = "彩脂", age = 20)
print(stu)

# 传参方式三: 位置传参 + 关键字传参(位置参数 要位于 关键字参数 前面, 否则会报错)
stu = reg_stu( "茉莉", 20, gender = "女", city = "北京")
print(stu)


#--------------------------------- 函数 - 默认参数 -------------------------------
# 默认参数可以不传递, 默认参数要在非默认参数后面, 否则会报错
# 函数调用时, 如果为默认参数传递了值, 则会修改默认参数的值; 如果没有传递该参数, 则直接使用默认值
# 定义函数
def reg_stu(name, age, gender = "男", city = "北京"):
    print(f"注册成功, 姓名: {name}, 年龄:  {age}, 性别:  {gender}, 城市:  {city}")
    return {"name":name, "age":age, "gender":gender, "city":city}

# 调用参数
stu = reg_stu("张三", 18)
print(stu)
# 注册成功, 姓名: 张三, 年龄:  18, 性别:  男, 城市:  北京
# {'name': '张三', 'age': 18, 'gender': '男', 'city': '北京'}

stu = reg_stu("茉莉", 20, "女")
print(stu)
# 注册成功, 姓名: 茉莉, 年龄:  20, 性别:  女, 城市:  北京
# {'name': '茉莉', 'age': 20, 'gender': '女', 'city': '北京'}

stu = reg_stu("王林", 20, "上海") # 要改城市, 可以用关键字传参
print(stu)
# 注册成功, 姓名: 王林, 年龄:  20, 性别:  上海, 城市:  北京
# {'name': '王林', 'age': 20, 'gender': '上海', 'city': '北京'}

stu = reg_stu("王林", 20, city= "上海") # 要改城市, 可以用关键字传参
print(stu)
# 注册成功, 姓名: 王林, 年龄:  20, 性别:  男, 城市:  上海
# {'name': '王林', 'age': 20, 'gender': '男', 'city': '上海'}


#---------------------------------不定长参数 - 位置传递(*args--> 元组)------------------------------
# 不定长参数也叫可变参数, 用于函数定义及调用时参数不确定(0个或多个)的场景
# 案例:根据传入的数据, 计算数据的最大值, 最小值, 平均值
def cacl_data(*args):
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)
    return min_data, max_data, round(avg_data, 1)

    # return args  # (10, 23, 32, 7, 200, 3, 55)

# 调用函数
print(cacl_data(10, 23, 32, 7, 200, 3, 55))


#---------------------------------不定长参数 - 关键字传递(**kwargs --> 字典)------------------------------
# 案例:根据传入的数据, 计算数据的最大值, 最小值, 平均值
def cacl_data(*args, **kwargs):
    """
    根据传入的数据, 计算数据的最大值, 最小值, 平均值
    :param args: 不定长位置参数, 需要计算的这批数据
    :param kwargs: 不定长关键字参数
        round: 保留的小数位数个数
        print: 是否打印输出
    :return: 最大值, 最小值, 平均值
    """
    min_data = min(args)
    max_data = max(args)
    avg_data = sum(args) / len(args)


    if kwargs.get("round") is not None:
        avg_data = round(avg_data, kwargs.get("round"))

    if kwargs.get("print"):
        print(f"计算出来的最小值{min_data}, 最大值{max_data}, 平均值{avg_data}")

    return min_data, max_data, avg_data
    # return args, kwargs # ((10, 23, 32, 7, 200, 3, 55), {'round': 3, 'print': False})
# 调用函数
# print(cacl_data(2, 7 , 9, 10, 45, round = 3, print= True))

print(cacl_data(10, 23, 32, 7, 200, 3, 55, round = 3, print= False))


#-------------------------------------函数 - 参数的类型 --------------------------------------
# 函数的参数类型
# 特殊参数: 函数参数
# 加
def add (x, y):
    return x + y

# 减
def sub (x, y):
    return x - y

# 乘
def mul (x, y):
    return x * y

# 除
def div (x, y):
    return x / y

# 计算(oper是函数)
def cacl(x, y, oper):
    return oper(x,y)

print(cacl(1, 2, add))


#-------------------------------------函数 - 匿名函数----------------------------------
# 匿名函数指的是没有名称的函数, 需要通过lambda表达式来声明, 可以简化函数的编写(单行表达式)
# 语法: lambda 参数列表 : 函数体
#
# 案例1: 打印一个分割线
# 函数
def out_line():
    print("------------------------------------------")
out_line()

# 匿名函数 --> 无参数列表
out_line = lambda : print("------------------------------------------")
out_line()

# 案例2: 就算两个数之和
# 函数
def add(x, y):
    return x + y
print(add(1, 2))

# 匿名函数 --> 有参数列表
add = lambda x,y : x + y
print(add(2, 3))

# 案例3:: 完成如下列表的排序操作，按照每一个元素的字符个数，从小到大排序；
data_list = ["C++", "C", "Python", "Jack", "PHP", "Java", "Go", "JavaScript", "Rust"]
print(data_list)

# sort ‘边排序，边计算’！
# sort() 接受两个只能通过关键词传递的参数, key 可以是一个函数, reverse 是一个 bool 值
data_list.sort(key = len, reverse = True)
print(data_list)
# 1. 因为是 data_list.sort()，所以 sort 拿到的就是 data_list，它知道该对谁动手。
# 2. 因为 sort() 是个写好的内置方法，它自带遍历功能，自己会去挨个拿元素。
# 3. 你给了它 key=len，它就会把拿到的每个元素去量长度, 然后根据长度，从小到大（递增）排好队。
# 5. reverse = True 从大到小（降序）排好队; reverse = False(默认的) 从小到大（升序）排好队

data_list.sort(key = lambda item : len(item))
print(data_list)
# 1. 因为是 data_list.sort(),data_list.sort() 唤醒了排序 sort ，它知道要排 data_list。
# 2. item 接收元素：因为 sort() 在遍历，所以它把每次拿出来的一个单词，强行塞进了 lambda 的 item 这个变量里。
# 3. len 量长度：lambda 拿到单词后，立刻执行冒号后面的 len(item)，算出这个单词有几个字母。
# 4. 最后排序：sort() 根据算出来的数字，从小到大把单词排好。”


def get_len(item):
    return len(item)
data_list.sort(key = get_len) # key = get_len 函数参数
print(data_list)
# 之所以觉得难，是因为脑子里有一个潜意识的误区：
# 觉得 get_len(item) 里面的 item，必须得是你真真实实填进去的一个具体数据（比如你得写 get_len("Python")）。
# 但 data_list.sort(key = get_len)。这里并没有写括号，也没有传任何数据进去，只是把工具（函数名）递交给了 sort。
# 那 sort 拿到这个工具后，怎么工作呢？”
# sort 自己会写一个隐藏的循环。它遇到列表里的第一个元素 "C++"，就会在心里偷偷调用你的函数：get_len("C++")。
# 这个时候，你的函数收到指令，立刻把 "C++" 塞进 item 这个变量里，
# 然后执行 return len(item)，算出 3，把结果交回给 sort。”


#-----------------------------------------案例------------------------------------------
# n的阶乘
# 定义一个函数,根据传入的数据, 计算该数据的阶乘
# def factorial (n):
#     # # 我写的, 繁琐了 TvT
#     # fa = 1
#     # while True:
#     #     if num > 0:
#     #         fa *= n
#     #         n -= 1
#     #     else:
#     #         break
#     # return fa
#
#     fa = 1
#     while n > 0:
#
#         fa *= n
#         n -= 1
#     return fa
# print(factorial(4))


# 案例1: n的阶乘定义一个函数,根据传入的数据, 计算该数据的阶乘
# 阶乘公式: f(n) = n * f(n - 1)
# 递归调用(先层层递进, 再层层回归): 指的是在函数中自己调用自己的情况 --> 要有终结点, 否则会无限调用, 然后报错
"""
    f(6) = 6 * factorial(5)                = 6 * 120 = 720 # 层层回归
    f(5) = 5 * factorial(4)                = 5 * 24 = 120
    f(4) = 4 * factorial(3)                = 4 * 6 = 24
    f(3) = 3 * factorial(2)                = 3 * 2 = 6
    f(2) = 2 * factorial(1)                = 2 * 1 = 2
    f(1) = 1                # 层层递进      = 1
"""
def factorial (n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
print(factorial(6))

# 案例2: 电商订单计算器
# 定义一个函数，用于根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额。
# 具体规则如下：
# 1. 优惠券需要商品金额满 5000 才可以使用，且优惠券金额不能超过商品总价。
# 2. 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）。
def cacl_order_cost(*args, coupon=0, score=0 ,express= 0.0):
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单总金额 = 商品总金额 - 优惠卷 - 积分抵扣 + 运费
    # 1. 计算商品总金额
    good_price = [goods[1] * goods[2] for goods in args]
    total_price = sum(good_price)
    # 2. 扣减优惠卷 --> 优惠券金额不能超过商品总价。
    if total_price >= 5000 and coupon <= total_price:
        total_price -= coupon
    # 3. 积分抵扣 --> 积分抵扣需要商品总金额满 5000 才可以使用，100 积分抵扣 1 元（且抵扣金额不能超过商品总价，积分只能整百抵扣）
    if total_price >= 5000 and score // 100 <= total_price:
        total_price -= score // 100
    # 4. 运费
    total_price += express
    return total_price
print(cacl_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1)))


#----------------------------------------类型注解---------------------------------------
# 变量定义 - 未指定类型注解 --> 类型推断
# 如果对变量直接赋值, 变量运算等场景, Python会自动进行类型推断
# Python是动态类型语言, 添加的类型注解只是提示, 并不是强制约束!!!
a = 596
score = 98.5
hobby = "Python"
flag = True
pic = None

names = ["A", "B", "C", "D", "E", "F"]
names1 = ["A", "B", "C", "D", "E", 594, 1000]
phones = {"1111111111", "222222222"}
options = {"count":2, "total":10}
goods = ("手机", 3999, 1)

# 变量定义 - 指定类型注解
# 语法: 变量: 数据类型 (如: a: int)
a2: int = 596
score2: float = 98.5
hobby2 = "Python"
flag2: bool = True
pic2: None = None

names2: list[str] = ["A", "B", "C", "D", "E", "F"]
names3: list[str | int] = ["A", "B", "C", "D", "E", 594, 1000]
phones2: set[str] = {"1111111111", "222222222"}
options2: dict[str, int] = {"count":2, "total":10}
goods2: tuple[str, int, int] = ("手机", 3999, 1)

# 函数类型注解
# 推荐使用类型注解
def circle_area_len(r:float) -> tuple[float, float]:
    return round(3.14 * r * r, 1), round(2 * 3.14 * r, 1)

al = circle_area_len(10)
print(al)


def cacl_order_cost(*args: tuple[str, float, int], coupon=0, score=0 ,express= 0.0) -> float:
# *args 不定长参数, 里面的每一个元素是元组,
# 所以冒号后面跟*args的元素类型, 即tuple , 再跟里面每一个元素要注解的类型 --> 即 *args: tuple[str, float, int]
    """
    根据传入的一批商品信息（商品名、价格、数量）、优惠（优惠券、积分抵扣）、运费信息计算订单的总金额
    :param args: 商品信息（商品名、价格、数量）
    :param coupon: 优惠券
    :param score: 积分抵扣
    :param express: 运费
    :return: 订单的总金额
    """
    # 订单总金额 = 商品总金额 - 优惠卷 - 积分抵扣 + 运费
    # 1. 计算商品总金额
    good_price = [goods[1] * goods[2] for goods in args]
    total_price = sum(good_price)
    # 2. 扣减优惠卷
    if total_price >= 5000 and coupon <= total_price:
        total_price -= coupon
    # 3. 积分抵扣
    if total_price >= 5000 and score // 100 <= total_price:
        total_price -= score // 100
    # 4. 运费
    total_price += express
    return total_price
print(cacl_order_cost(("鼠标", 188, 2), ("键盘", 388, 1), ("手机", 6999, 1)))