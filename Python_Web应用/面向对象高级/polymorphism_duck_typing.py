#------------------------------------多态(鸭子类型)-----------------------------------------
# 鸭子类型(DuckTyping)是指如果它走路像鸭子，叫起来叫鸭子，那么它就是鸭子。
# 在鸭子类型中，我们关注的是对象的行为（它有什么方法），而不是对象的类型（它是什么类）
# 注意：鸭子类型的优势是不需要存在继承关系，只要对象有相应的方法就能使用

class Duck:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Duck: {self.age} 岁的 {self.name} 正在游泳...')


class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Dog: {self.age} 岁的 {self.name} 正在游泳...')


class Pig:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def swimming(self):  # 启动
        print(f'Pig: {self.age} 岁的 {self.name} 正在游泳...')

# 这里的 duck 只是变量名字
# 这里使用类型注解, 说明他是 类Duck 的实例, 但下面传入 Dog, Pig, 会警告:
# 应为类型 'Duck'，但实际为 'Dog'
# 应为类型 'Duck'，但实际为 'Pig'
# def go_swimming(duck: Duck):
#     duck.swimming()


def go_swimming(duck): # 这里的 duck 只是变量名字, 不是代表它一定是 Duck类
    duck.swimming()

if __name__ == '__main__':
    # Python不检查这个变量原本应该是什么类，它只做一件事：
    # 这个对象有没有.swimming()这个方法？有就直接调用
    go_swimming(Duck('鸭子', 1))
    go_swimming(Dog('狗', 2))
    go_swimming(Pig('猪', 3))

