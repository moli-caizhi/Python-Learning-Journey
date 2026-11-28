#--------------------------------------------封装--------------------------------------------
"""
封装：将数据(属性)和操作数据的方法绑定在一起，形成一个独立的单元(类)，保护数据不被外部访问，通过访问修饰符实现封装。

1. 私有属性：在属性名前加双下划线__
2. 私有方法：在方法名前加双下划线__
"""
# self: 代表正在创建的那一辆车对象
# self.color: 这辆车自己的颜色属性
# 等号右边的 color: 用户调用类时传进来的颜色值, 例如 Car("Audi", "A6", "黑色"), 这里 color 就等于 "黑色"
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

if __name__ == '__main__':
    # 创建对象
    car = Car("Audi", "A6", "黑色", "茉莉")

    # 访问属性
    print(car.brand) # --> Audi
    print(car.color) # --> 黑色
    print(car.model) # --> A6

    # 调用方法
    # 调用方法, 方法内部自带print, 直接输出; 如果方法用return返回内容, 则需要 print(car.start())
    car.start() # --> Audi A6 正在启动...
    car.run() # --> 茉莉: Audi A6 正在行驶...
              #     Audi A6 正在控制燃油...
    car.stop() # --> Audi A6 停止行驶...

    
    # 调用使外部可以访问拥有者的属性的方法
    print(car.get_owner()) # --> 茉**

    # print(car.start()) # --> Audi A6 正在启动...
                         #     None --> 方法里面没有返回值, 默认为 None

    """
        # 注意: Python中并没有真正的私有机制，约定在私有属性名和方法名前加__(两个下划线)表示私有，
        # 但实际上仍然可以通过 _ClassName__attr 或 _ClassName__method 的方式访问, 
        # 例如 car._Car__owner, car._Car__control_fuel()
        # print(car.__owner) --> # 报错
        # car.__control_fuel() --> # 报错
        
        print(car._Car__owner) # --> 茉莉
        car._Car__control_fuel() # --> Audi A6 正在控制燃油...
    """

