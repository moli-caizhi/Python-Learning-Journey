#-----------------------------------------图书管理系统---------------------------------------
# 某社区图书馆需要开发一个简单的图书管理系统。系统需要支持会员登录、图书借阅、图书归还等功能。系统中有两种类型的
# 会员：普通会员和VIP会员，他们的借书权限不同。你需要使用面向对象编程的思想，设计并实现这个图书管理系统。
# 核心功能：
#     1.会员登录：会员通过卡号和密码登录系统
#     2.借书：会员可以借阅库存中有余量的图书
#     3.还书：会员可以归还借阅的图书
#     4.查看我的借阅：展示当前会员已经借阅的图书列表
#     5.退出系统
# 借阅规则：
#     1.普通会员最多可借3本
#     2.VIP会员最多可借6+VIP等级本（VIP等级，默认为1）
# 注意：
#     1.登录成功（卡号和密码均正确）后，才可以访问该系统
#     2.图书库存不足，或当前会员借书数量达到最大借书数量，不能再借新书

from abc import ABC, abstractmethod
import json

# 书籍类
class Book:
    def __init__(self, book_id, title, author, total_num):
        self.book_id = book_id      # 书籍编号
        self.title = title          # 书籍标题
        self.author = author        # 作者
        self.total_num = total_num  # 总数量
        self.__available_num = total_num    # 可用数量

    def borrow_book(self): # 借阅书籍
        if self.__available_num > 0:
            self.__available_num -= 1
            return True
        return False

    def return_book(self): # 归还书籍
        self.__available_num += 1

    def get_available_num(self): # 获取可用数量
        return self.__available_num

# 抽象类: 是一种只能被继承, 不能被直接实例化的类,
# 作用就是规定子类必须要实现哪些方法, 强制子类必须遵守统一的代码规范
# Python中的抽象类, 需要继承 abc 模块中的ABC类 ---> ABC: Abstract Base Class
# 会员类
class Member(ABC):
    def __init__(self, member_id, name, password):
        self.member_id = member_id      # 会员卡号
        self.name = name                # 会员姓名
        self.__password = password      # 会员密码
        self.__borrowed_books = []      # 借阅书籍列表

    def borrow_book(self, book: Book):  # 借阅书籍
        # 判断当前会员借阅数量是否达到最大限制
        if len(self.__borrowed_books) >= self.get_max_books():
            print("借阅失败，您的借阅数量已达到最大限制！")
            return False

        # 判断书籍是否可借阅
        if book.borrow_book():
            self.__borrowed_books.append(book)
            print(f"{self.name} 已成功借阅图书 {book.title}")
            return True
        else:
            print(f"借阅失败，图书 {book.title} 已被借完！")
            return False

    def return_book(self, book: Book): # 归还书籍
        # 判断当前会员是否借阅了该书籍
        if book in self.__borrowed_books:
            # 还书
            book.return_book()
            self.__borrowed_books.remove(book)
            print(f"{self.name} 已成功归还图书 {book.title}")
        else:
            print(f"归还失败，您没有借阅图书 {book.title}")

    def get_password(self): # 获取会员密码
        return self.__password

    def get_borrowed_books(self): # 获取借阅的书籍
        return self.__borrowed_books

    # 获取会员最大借阅数量(在子类中实现)
    @abstractmethod # --> 这个装饰器表示这个方法是抽象方法，必须在子类中实现, 否则无法创建子类对象
    def get_max_books(self) -> int:
        pass

# 普通会员类
class NormalMember(Member):
    def get_max_books(self) -> int:
        return 3

# VIP会员类
class VIPMember(Member):
    def __init__(self, member_id, name, password, vip_level):
        super().__init__(member_id, name, password)
        self.vip_level = vip_level # 会员等级

    def get_max_books(self) -> int:
        return 6 + self.vip_level

class LibrarySystem:
    def __init__(self):
        self.books = {}  # 图书列表 --> {"AI001": Book对象, "AI002": Book对象, ...}
        self.members = {} # 会员列表 --> {"N001": Member对象, "N002": Member对象, ...}
        self.current_member: Member | None = None      # 当前登录的会员
        # 加载数据(书籍, 会员)
        self.load_books_data()
        self.load_members_data()

    def load_books_data(self):
        # 加载书籍数据 --> ../ 向上跳一层，去到 Python Web应用, 再进入同级的 data 目录
        with open("../data/books.json", "r", encoding="utf-8") as f:
            books_data = json.load(f)
            for book in books_data:
                # 我的疑惑: --> 为什么要写成这样?直接添加json文件的值不行吗?为什么还要创建实例对象来保存?
                # 读取json中的书籍原始数据，不直接保存字典，而是用数据创建Book实例
                # json读出的字典只有静态数据，无法自带业务逻辑；
                # Book对象同时保存属性（编号、书名、可用数量）和方法（借书、还书）
                # 书籍借阅判断逻辑封装在Book类中，会员相关逻辑封装在Member及其子类中
                # 不需要在多处重复编写判断代码，统一管控数量
                self.books[book["编号"]] = Book(book["编号"], book["标题"], book["作者"], book["数量"])
            print("加载书籍数据成功")

    def load_members_data(self):
        with open("../data/members.json", "r", encoding="utf-8") as f:
            members_data = json.load(f)
            for member in members_data:
                # 判断这个字符串是不是以字母 N 开头
               if member["卡号"].startswith("N"):
                   self.members[member["卡号"]] = NormalMember(member["卡号"], member["姓名"], member["密码"])
               elif member["卡号"].startswith("V"):
                   self.members[member["卡号"]] = VIPMember(member["卡号"], member["姓名"], member["密码"], member["会员等级"])
            print("加载会员数据成功")

    def login(self):
        while True:
            print("\n【登录】")
            member_id = input("请输入会员卡号: ")
            password = input("请输入会员密码: ")

            # 判断会员卡号是否存在
            if member_id not in self.members:
                print("登录失败，会员卡号不存在！")
                continue

            # 判断密码是否正确
            member = self.members[member_id]
            if member.get_password() == password:
                print(f"登录成功, 欢迎您, {member.name}")
                self.current_member = member
                return True
            else:
                print("登录失败，密码错误！")
                continue

    def borrow_book(self):  # 借阅图书
        # 1. 展示出当前图书馆的图书列表
        for book in self.books.values():
            print(f"编号: {book.book_id}, 标题: {book.title}, 作者: {book.author}, 总数: {book.total_num}, 可用: {book.get_available_num()}")

        # 2. 获取用户输入的图书编号, 执行借书操作
        book_id = input("请输入要借阅的图书编号: ")
        if book_id not in self.books:
            print("借阅失败，图书编号不存在！")
            return
        # self.books[book_id] --> self.books["AI001"] 去字典里面查找 key,
        # 因为 self.books = {}  # 图书列表 --> {"AI001": Book对象, "AI002": Book对象, ...}
        # 所以根据 key 取出对应的 Book 对象
        # 这一步执行完, 得到的结果就是一本实实在在的书对象, 里面有书名、库存, 还有 borrow_book() 方法
        self.current_member.borrow_book(self.books[book_id]) # --> borrow_book 方法在 Member 类中定义

    def return_book(self):  # 归还图书
        # 1. 展示出当前会员的借阅列表
        borrowed_books = self.current_member.get_borrowed_books()
        print("【已经借阅的图书列表:】")
        for book in borrowed_books:
            print(f"编号: {book.book_id}, 标题: {book.title}")

        # 2. 获取用户输入的图书编号, 执行还书操作
        book_id = input("请输入要归还的图书编号: ")
        if book_id not in self.books:
            print("还书失败，图书编号不存在！")
            return
        self.current_member.return_book(self.books[book_id])

    def show_borrowed_books(self):  # 查看借阅
        borrowed_books = self.current_member.get_borrowed_books()
        if len(borrowed_books) > 0:
            print("【已经借阅的图书列表:】")
            for book in borrowed_books:
                print(f"编号: {book.book_id}, 标题: {book.title}")
        else:
            print("您没有借阅任何图书！")

    def run(self):  # 运行系统
        if self.login():
            while True:
                print("\n1. 借阅图书")
                print("2. 归还图书")
                print("3. 查看借阅")
                print("4. 退出系统")

                choice = input("请选择操作(1-4): ")
                match choice:
                    case "1":
                        self.borrow_book()
                    case "2":
                        self.return_book()
                    case "3":
                        self.show_borrowed_books()
                    case "4":
                        print("退出系统, Bye Bye ~")
                        break
                    case _:
                        print("无效的选项，请重新选择！")

if __name__ == "__main__":
    ls = LibrarySystem()
    ls.run()
