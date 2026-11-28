#--------------------------------------------多继承-----------------------------------------------
# 多继承指的是一个子类，同时继承了多个父类的情况（会将多个父类中的非私有的属性和方法都继承下来）

# 语法:
# class 子类名(父类1, 父类2, ...):

class Car:
    def __init__(self, brand, model, color, owner):
        self.brand = brand      # 品牌(公共属性)
        self.model = model      # 型号
        self.color = color      # 颜色
        self.__owner = owner    # 拥有者(私有属性)

    def start(self):  # 启动(公共方法)
        print(f'{self.brand} {self.model} 正在启动...')

    # run 是公开行驶方法, 内部使用私有属性并调用私有燃油控制方法
    def run(self):  # 行驶
        print(f'{self.__owner}: {self.brand} {self.model} 正在行驶...')

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def get_owner(self): # 使外部可以访问拥有者的属性的方法
        return self.__owner[0:1] + "**" # self.__owner 是字符串，所以可以使用字符串操作

    def charge(self):
        print(f' {self.brand} {self.model} 正在补充燃料...')

class HuaweiAiDriving:
    def __init__(self, version="v1.0"):
        self.version = version

    def run(self):
        print(f'使用华为AI智能驾驶系统 {self.version} 正在驾驶...')

# 问界汽车
# 在类里面定义 Car 和 HuaweiAiDriving 的实例对象, 创建对象时可以传递全部参数, 调用全部父类的方法
class WenJieCar(Car, HuaweiAiDriving): # --> Car, HuaweiAiDriving 调换顺序, 下面的创建对象会报错
    def __init__(self, brand, model, color, owner, version="v1.0"):

        # 既可以调用父类的构造方法，也可以调用父类的其他方法
        # 默认按继承的顺序调用父类的构造方法，即先调用Car的构造方法，再调用HuaweiAiDriving的构造方法 --> 不推荐
        # super().__init__(brand, model, color, owner)
        # super().__init__(version)

        # --> 推荐
        Car.__init__(self, brand, model, color, owner)
        HuaweiAiDriving.__init__(self, version)

    # 重写 run 方法
    def run(self):
        Car.run(self)
        HuaweiAiDriving.run(self)
# MRO: Method Resolution Order(方法解析顺序) --> 父类的搜索顺序
# 注意：当一个类继承了多个父类时，默认优先使用第一个父类中的同名属性或方法,
# 可以使用 类名.__mro__属性 或 类名.mro()方法 查看调用顺序
if __name__ == '__main__':
    # 如果没有在类里面定义 Car 和 HuaweiAiDriving 的实例对象, 只能传递 Car 的参数, 调用 Car 的方法,
    # 不能传递 HuaweiAiDriving 的参数, 调用 HuaweiAiDriving 的方法
    wj = WenJieCar("华为", "Model Y", "白色", "小王", "v1.1")
    print(wj.__dict__)

    # 如果想全部调用, 在子类中重写 run 方法
    # wj.run() # --> 小王: 华为 Model Y 正在行驶... --> MRO 只调用第一个父类的同名方法

    # 重写后
    wj.run()

    # print(WenJieCar.__mro__)
    # print(WenJieCar.mro())
