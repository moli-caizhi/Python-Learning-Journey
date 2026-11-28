#------------------------------------------继承 -- 重写------------------------------------------
# 重写是指子类继承父类后，如果父类中的方法不满足需求，可以在子类中重新定义父类中已有的方法（方法名相同），
# 从而用子类的实现替换父类的实现

# 注意：如果子类在重写父类的方法时，需要调用父类的方法，可以通过父类名.方法名(self)/super().方法名()方式来调用

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

    def charge(self):
        print(f' {self.brand} {self.model} 正在补充燃料...')

# 燃油车
class FuelCar(Car):  # 继承自 Car 类
    def charge(self): # --> 重写父类的方法
        # 调用父类的方法
        # 方法一: --> super().方法名
        # super().charge()

        # 方法二: --> 父类名.方法名(self)
        Car.charge(self)
        print(f' {self.brand} {self.model} 正在加油...')

# 电车
class ElectricCar(Car):  # 继承自 Car 类
    def charge(self):
        Car.charge(self)
        print(f' {self.brand} {self.model} 正在充电...')

if __name__ == '__main__':
    fc = FuelCar("BWM", "X5", "白色", "小王")
    fc.charge()

    # c1 = Car("BWM", "X5", "白色", "小王")
    # c1.charge() # --> BWM X5 正在补充燃料...
