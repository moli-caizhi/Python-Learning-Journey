#----------------------------------------案例---------------------------------------
# 教务系统
# 采用面向对象的编程思想，完成教务管理系统的开发。
# 1. 添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
# 2. 修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
# 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
# 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
#     4.1 输出格式为："姓名: 张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"
# 5. 展示全部学生成绩：展示出系统中所有学生的成绩

# 定义学生类
class Student:
    def __init__(self, name, chinese, math, english):
        self.name = name
        self.chinese = chinese
        self.math = math
        self.english = english

    def __str__(self):
        # 输出格式为："姓名: 张三 | 语文: 85 | 数学: 90 | 英语: 88 | 总分: 263"
        return f"姓名: {self.name} | 语文: {self.chinese} | 数学: {self.math} | 英语: {self.english} | 总分: {self.chinese + self.math + self.english}"

    # 修改的学生成绩
    def update_score(self, chinese = None, math = None, english = None):
        if chinese is not None:
            self.chinese = chinese
        if math is not None:
            self.math = math
        if english is not None:
            self.english = english

# 定义教务管理系统类
class EduManagement:
    system_version = "1.0"
    system_name = "教务管理系统"

    def __init__(self):
        self.student_list = [] # 列表, 记录的是在校学生信息

    # 1.添加学生成绩：根据输入的学生姓名、语文成绩、数学成绩、英语成绩，记录在系统中
    def add_student(self):
        name = input("请输入学生姓名: ")

        # 1.1 检查学生姓名是否已存在，如果学生不存在，再添加（存在则，不添加）
        for s in self.student_list:
        # 第一个疑问:    --> s 是什么?
        # 遍历的 s 就是相当于遍历在列表中添加进来的 stu
        # 在 for s in self.student_list: 循环中, 每次迭代取出的s, 就是该地址所指向的 实例对象 本身。


            if s.name == name: # 对象.属性
                # 第二个疑问:    --> s.name 是什么意思?
                # s.name的含义：
                # 通过 对象.属性 的语法，访问该学生对象内部的 name 数据
                # if s.name == name 即：判断当前取出的对象的名字, 是否与输入的姓名一致

                print("该学生已存在, 添加失败!")
                return

        chinese = int(input("请输入学生语文成绩: "))
        math = int(input("请输入学生数学成绩: "))
        english = int(input("请输入学生英语成绩: "))

        # 验证成绩范围（0-100分）
        if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:

            # 创建学生对象并添加到系统
            stu = Student(name, chinese, math, english)
            self.student_list.append(stu)
            # 第三个疑问:    --> stu 的存入形式是什么?
            # self.student_list 是一个列表, 存入其中的 stu 不是普通数据, 是一个一个地址
            # 地址相当于 Student 类的实例对象
            # 实例对象不仅包含 全部属性，还包含类里定义的 所有方法（比如修改成绩的方法）
            # 实例对象 = 属性（数据） + 方法（行为）

            # 第四个疑问:    --> 为什么这个输出能直接掉调用 __str__ 魔法方法
            # 所以print(f"当前成绩: {s}") 就能直接使用 __str__ 魔法方法

            print("学生信息添加成功~")
        else:
            print("各科成绩必须得在0-100之间")

    # 2.修改学生成绩：根据输入的学生姓名，修改对应的学生成绩
    def update_student(self):
        # 输入要修改的学生姓名
        name = input("请输入要修改的学生姓名: ")

        # 根据姓名查找该学生，显示该生当前成绩信息
        for s in self.student_list:
            if s.name == name:
                print(f"当前成绩: {s}") # 不懂, 为什么是直接输出 Student 类中的魔法方法

                # 输入新的语文、数学、英语成绩
                chinese = int(input("请输入修改后的学生语文成绩: "))
                math = int(input("请输入修改后的学生数学成绩: "))
                english = int(input("请输入修改后的学生英语成绩: "))
                # 验证成绩范围（0-100分）
                if 0 <= chinese <= 100 and 0 <= math <= 100 and 0 <= english <= 100:
                    # 创建学生对象并添加到系统
                    s.update_score(chinese, math, english)
                    print("学生信息添加成功~")
                    print(f"修改后的成绩: {s}")
                    return
                else:
                    print("各科成绩必须得在0-100之间")
                    return

        print("未找到该学生, 修改失败!")
    # 3. 删除学生成绩：根据输入的学生姓名，删除对应的学生成绩
    def delete_student(self):
        name = input("请输入要删除的学生姓名: ")

        for s in self.student_list:
            if s.name == name:
                self.student_list.remove(s)
                print("学生信息删除成功~")
                return

        print("未找到该学生, 修改失败!")
    # 4. 查询指定学生成绩：根据输入的学生姓名，查找对应的学生成绩，并输出
    def query_student(self):
        name = input("请输入要查询的学生姓名: ")

        for s in self.student_list:
            if s.name == name:
                print(f"学生信息: {s}")
                return

        print("未找到该学生!")

    # 5.展示全部学生成绩：展示出系统中所有学生的成绩
    def list_students(self):
        for s in self.student_list:
            print(s)

    # 运行系统
    def run(self):
        print(f"欢迎使用教务管理系统, 当前版本为 {EduManagement.system_version}")

        while True:
            print()
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            print("# 1.添加学生  2.修改学生  3.删除学生  4.查询指定学生  5.查询所有学生  6.退出系统 #")
            print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
            choice= input("请选择你要执行的操作, 输入1-6: ")

            try:
                match choice:
                    # 在 方法里面 调用方法, 语法: 当前实例对象.方法名
                    # 在 类 那里调用方法, 先创建对象, 再调用方法
                    case "1": # 添加学生
                        self.add_student()
                    case "2": # 修改学生
                        self.update_student()
                    case "3": # 删除学生
                        self.delete_student()
                    case "4": # 查询指定学生
                        self.query_student()
                    case "5": # 查询所有学生
                        self.list_students()
                    case "6": # 退出系统
                        print("Bye ~")
                        break
                    case _:
                        print("操作不支持, 请重新输入!")
            except ValueError as e:
                print("输入的数据有误, 请检查, 然后重新输入!!!", e)
                # continue # 跳过本次循环, 继续下一次循环, 如果后面有其他的逻辑, 又不想运行, 就用 continue

            except Exception as e:
                print("程序运行出错了, 请重新选择!", e)

# 创建对象
system = EduManagement()
# 调用方法
system.run()


#--------------------------------------------练习-----------------------------------------------
# 采用面向对象的编程思想，开发一个购物车管理系统，实现商品信息的添加、修改、删除、查询功能。
# 系统使用自定义对象存储商品数据，通过控制台菜单与用户交互。具体功能如下：
# 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
# 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
# 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
# 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
# 5．退出购物车

# 定义购物车类
class Cart:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"商品名称：{self.name}，商品价格：{self.price}，商品数量：{self.quantity}"

# 定义购物车管理系统类
class CartManagement:
    system = "2.0"
    system_name = "购物车管理系统"
    def __init__(self):
        self.cart_list = [] # 列表, 记录的是购物车信息

    # 1．添加购物车：用户根据提示录入商品名称、以及该商品的价格、数量，保存该商品信息到购物车。
    def add_Cart(self):
        name = input("请输入商品名称: ")
        # 判断商品是否存在
        for c in self.cart_list:
            if c.name == name:
                print("该商品已存在, 添加失败!")
                return

        price = float(input("请输入商品价格: "))
        quantity = int(input("请输入商品数量: "))
        cart = Cart(name, price, quantity)
        self.cart_list.append(cart)
        print("商品添加成功~")
    # 2．修改购物车：要求用户输入要修改的购物车商品名称，然后再提示输入该商品的价格、数量，输入完成后修改该商品信息。
    def update_Cart(self):
        name = input("请输入要修改的购物车商品名称: ")
        for c in self.cart_list:
            if c.name == name:
                price = float(input("请输入修改后的商品价格: "))
                quantity = int(input("请输入修改后的商品数量: "))
                c.update_score(price, quantity)
                print("商品修改成功~")
                return
        print("未找到该商品, 修改失败!")

    # 3．删除购物车：要求用户输入要删除的购物车名称，根据名称删除购物车中的商品。
    def delete_Cart(self):
        name = input("请输入要删除的购物车名称: ")
        for c in self.cart_list:
            if c.name == name:
                self.cart_list.remove(c)
                print("商品删除成功~")
                return
        print("未找到该商品, 删除失败!")
    # 4．查询购物车：将购物车中的商品信息展示出来，格式为："商品名称：xxx，商品价格：xxx，商品数量：xxx"。
    def list_Cart(self):
        for c in self.cart_list:
            print(c)
    # 5．退出购物车
    def exit_Cart(self):
        print("退出购物车系统~")
        exit()

# 购物车管理系统菜单
    def run(self):
        print()
        print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
        print("# 1. 添加购物车   2. 修改购物车   3. 删除购物车   4. 查询购物车   5. 退出购物车 #")
        print("# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #")
        choice = input("请选择你要执行的操作, 输入1-5: ")
        while True:
            try:
                match choice:
                    case "1": # 1. 添加购物车
                        self.add_Cart()
                    case "2": # 2. 修改购物车
                        self.update_Cart()
                    case "3": # 3. 删除购物车
                        self.delete_Cart()
                    case "4": # 4. 查询购物车
                        self.list_Cart()
                    case "5": # 5. 退出购物车
                        self.exit_Cart()
                    case _: # 其他操作
                        print("操作不支持, 请重新输入!")
            except ValueError as e:
                print("输入的数据有误, 请检查, 然后重新输入!!!", e)

# 创建对象
system = CartManagement()
system.run()
