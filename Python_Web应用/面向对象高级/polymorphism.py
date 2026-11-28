#--------------------------------------------多态---------------------------------------------
# 多态是指同一个方法，具有不同的形态、行为、表现
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

# 燃油车
class FuelCar(Car):  # 继承自 Car 类
    def charge(self): # --> 重写父类的方法
        print(f' {self.brand} {self.model} 正在加油...')

# 电车
class ElectricCar(Car):  # 继承自 Car 类
    def charge(self):
        print(f' {self.brand} {self.model} 正在充电...')

# 补充燃料 函数
# 参数类型为父类,支持传入任意子类
def handle_charge(car: Car): # --> 函数参数类型声明为父类型
    car.charge()

if __name__ == '__main__':
    handle_charge(FuelCar("BWM", "X5", "白色", "小王"))
    handle_charge(ElectricCar("BYD", "X5", "白色", "小王"))
