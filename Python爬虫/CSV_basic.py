# CSV：（Comma-Separated Values，逗号分隔值），是一种简单、通用的文本文件格式，用于存储表格数据，
# 可以直接使用Excel打开。 --> 英文的逗号,选择ANSI(系统编码)
# 注意逗号要紧贴, 不能写空格, 否则写多个值在一个单元格中, 会分开显示

# CSV 操作 --> 方式一: 文件操作的原始方式
# 写
# with open("resources/data.csv", "w", encoding="UTF-8") as f:
#     f.write("姓名,年龄,性别,爱好\n") # 写入表头
#     f.write("张三,18,男,'篮球,羽毛球'\n") # 写入数据 --> 想写入多个数据用引号括起来
#     f.write("李四,19,女, 足球\n")
#     f.write("王五,20,男,游戏\n")
#     f.write("赵六,21,女,音乐\n")

# 读
# with open("resources/data.csv", "r", encoding="UTF-8") as f:
#     # data = f.read()
#     # print(data)
#     for line in f:
#         print(line.strip())

# CSV 操作 --> 方式二: 使用csv模块 --> 推荐
import csv
# newline="" --> 表示不换行, open 写入时默认换行
with open("resources/info.csv", "w", encoding="UTF-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["姓名", "年龄", "性别", "爱好"]) # 创建一个DictWriter对象
    writer.writeheader() # 写入表头
    writer.writerow({"姓名": "张三", "年龄": 18, "性别": "男", "爱好": "篮球,羽毛球"})
    writer.writerow({"姓名": "李四", "年龄": 19, "性别": "女", "爱好": "足球"})
    writer.writerow({"姓名": "王五", "年龄": 20, "性别": "男", "爱好": "游戏"})
    writer.writerow({"姓名": "赵六", "年龄": 21, "性别": "女", "爱好": "音乐"})

# 读
with open("resources/info.csv", "r", encoding="UTF-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)
