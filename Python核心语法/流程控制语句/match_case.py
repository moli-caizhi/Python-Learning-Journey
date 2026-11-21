#实现一个简易的计算器
# num1 = float(input("请输入第一个数:"))
# num2 = float(input("请输入第二个数:"))
# oper = input("请输入运算符号(+ - * /):")
# match oper:
#     case "+":
#         print(f"{num1} + {num2} = {num 1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "/":
#         if num2 == 0.0:
#             print("除数不能为0哦~")
#         else:
#             print(f"{num1} / {num2} = {num1 / num2}")
#     case _:
#         print("操作不支持!!!")


#游戏角色移动控制系统
instruction = input("请输入指令:")
match instruction:
    case "上" | "w" | "W":
        print("角色向上移动")
    case "下" | "s" | "S":
        print("角色向下移动")
    case "左" | "a" | "A":
        print("角色向左移动")
    case "右" | "d" | "D":
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" | "J":
        print("角色发动攻击")
    case "退出" | "esc" | "ESC":
        print("角色退出游戏")