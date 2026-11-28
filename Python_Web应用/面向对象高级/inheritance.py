#--------------------------------------------继承-----------------------------------------------
# 继承描述的是两个类之间的关系, 子类继承父类, 就可以获取到父类的 属性和方法(非私有)
# 类都有一个父类 object(默认继承自 object)
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
        self.__control_fuel()

    def stop(self):  # 停止
        print(f'{self.brand} {self.model} 停止行驶...')

    def __control_fuel(self):  # 控制燃油(私有方法)
        print(f'{self.brand} {self.model} 正在控制燃油...')

    def get_owner(self): # 使外部可以访问拥有者的属性的方法
        return self.__owner[0:1] + "**" # self.__owner 是字符串，所以可以使用字符串操作

# 燃油车
class FuelCar(Car):  # 继承自 Car 类
    pass

# 电车
class ElectricCar(Car):  # 继承自 Car 类
    pass

# 测试
if __name__ == '__main__':

    fc = FuelCar("BWM", "X5", "白色", "小王")
    fc.run()
