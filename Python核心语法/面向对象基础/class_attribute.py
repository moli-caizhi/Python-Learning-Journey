   #-------------------------------------------类与对象-----------------------------------------
# # 类名的命名规范, 遵循大驼峰命名法, 每个单词的首字母都是大写, 单词之间没有分隔符, 比如UserInfo, UserAccount
# # __dict__ 是Python中用户自定义实例的一个特殊属性, 用字典的形式存储对象的所有属性
#
#
# # 定义类的语法: --> 不推荐
# # class 类名:
# #     pass --> 结构
# #
# # # 创建对象
# # 对象名 = 类名()
#
# # 动态的为对象添加属性
#
# # 对象名.属性名1 = 属性值1
# # 对象名.属性名2 = 属性值2
# # print(c1.__dict__)
#
# #定义类 --> 不推荐 动态的为对象添加属性 -->会降低项目的可读性, 可维护性, 增加开发的难度
# class Car:
#     pass
#
# # 创建对象
# c1 = Car()
#
# # 动态的为对象添加属性
# c1.color = "red"
# c1.brand = "BMW"
# c1.name = "X5"
# c1.price = 500000
#
# print(c1.__dict__) # 会将对象中的所有属性以字典的形式输出出来
# print(c1.brand) # 查看某一个属性
# print(c1) # 输出 Car 的内存地址
#
#------------------------------------------------------------------------------------------
#
# # 定义类的语法: --> 推荐
# # class 类名:
# #     def __init__(self, 参数列表):
# #         self.属性名 = 参数值
# #         self.属性名 = 参数值
# #
# # # 创建对象
# # 对象名 = 类名(参数列表)
#
# class Car:
#     # 说明 def ... 定义在类的外面称之为函数, 定义在类中的函数称之为方法
#     # __init__: 初始化方法, 对象创建成功后 自动调用 , 主要用于设置对象的初始状态(设置对象属性)
#     # self: 方法的第一个参数, 表示当前创建的实例对象, 在这里相当于 c1
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已添加完毕")
#
# # 创建对象
# c1 = Car("红色", "BWM", "X7", 800000)
# print(c1.color)
# print(c1.brand)
# print(c1.name)
# print(c1.price)
# print(c1.__dict__)
#
# # c2 = Car() # 报错, 没传递形参
#
# c2 = Car("白色", "奔驰", "E300", 450000)
# print(c2.__dict__)


#-------------------------------------实例方法---------------------------------------
# # 语法:
# # class 类名:
# #     def __init__(self, 参数列表):
# #         self.属性名 = 参数值
# #         self.属性名 = 参数值
# #
# #     def 方法名(self, 形参列表):
# #         ...
# #     def 方法名(self, 形参列表):
# #         ...
# #
# # # 创建对象
# # 对象名 = 类名(参数列表)
# # # 调用方法
# # 对象名.方法名(实参)
#
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price):
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已添加完毕")
#
#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶中...")
#
#     def total_cost(self, discount, rate):
#         """
#         计算提车的总费用
#         :param discount: 折扣
#         :param rate: 税率
#         :return: 提车的总费用
#         """
#         total_cost = self.price * discount + self.price * rate
#         return total_cost
#
# # 创建对象
# c1 = Car("白色", "BWM", "X5", 800000)
#
# # 调用方法
# c1.running()
# total = c1.total_cost(0.9, 0.1)
# print("提车的总费用为: ", total)


#------------------------------------------魔法方法---------------------------------------
# # 魔法方法是指 Python 中提供的以双下划线开头和结尾的特殊方法, 用于定义类的特殊行为, 比如: __init__
# # 魔法方法是不需要我们手动调用, Python 会在合适的时机自动调用
#
# class Car:
#     def __init__(self, c_color, c_brand, c_name, c_price): # 初始化方法
#         self.color = c_color
#         self.brand = c_brand
#         self.name = c_name
#         self.price = c_price
#         print("Car 类型的对象初始化完毕, 对象属性已添加完毕")
#     # 定义实例方法
#     def running(self):
#         print(f"{self.brand} {self.name} 正在高速行驶中...")
#
#     def total_cost(self, discount, rate):
#         total_cost = self.price * discount + self.price * rate
#         return total_cost
#
#     # 魔法方法
#     def __str__(self): # 字符串的表示方法
#         return f"{self.color} {self.brand} {self.name} {self.price}"
#
#     def __eq__(self, other): # 比较两个对象是否相等(equal)
#         return self.color == other.color and self.brand == other.brand and self.name == other.name and self.price == other.price
#
# # 支持比较两个对象的大小
# # __lt__ (小于(less than)),
# # __le__ (小于等于(less than or equal))
# # __gt__ (大于(greater than)),
# # __ge__ (大于等于(greater than or equal))
#     def __lt__(self, other):
#         return self.price < other.price
#
# # 测试
# c1 = Car("白色", "BYD", "汉", 180000)
# print(c1)
#
# c2 = Car("白色", "BYD", "汉", 180000)
# print(c2)
#
# print(c1 == c2)
# print(c1 > c2)


#------------------------------------实例属性与类属性--------------------------------
class Car:
    # 类属性: 属于类本身的属性, 所有实例共享的(所有实例对象共享的数据或配置)
    # 类属性(所有实例对象共享的) --> 通过 类名.属性 的方式访问
    wheel = 4 # 轮胎的数量
    tax_rate = 0.1 # 购置税的税率

    def __init__(self, c_color, c_brand, c_name, c_price):
        # 实例属性: 属于每个具体对象的属性, 每个对象都是独立的(各个对象特有的数据)
        # 实例属性 --> 通过 实例对象.属性 访问
        self.color = c_color
        self.brand = c_brand
        self.name = c_name
        self.price = c_price
        self.wheel = 2
    # 定义实例方法
    def running(self):
        print(f"{self.brand} {self.name} 正在高速行驶中...")

    def total_cost(self, discount, rate):
        total_cost = self.price * discount + self.price * rate
        return total_cost

c1 = Car("白色", "BYD", "汉", 180000)
print(c1.brand) # BYD
print(c1.wheel) # 2 --> 通过实例对象查找属性时, 会先查找实例属性; 实例属性不存在, 再查找类属性

# 通过类名访问类属性 --> 通过 类名.属性 的方式访问
print(Car.wheel) # 4

c2 = Car("黑色", "Tesla", "Model Y", 250000)
print(c2.brand)


