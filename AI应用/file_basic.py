#------------------------------------------文件操作----------------------------------
# 编码:是将字符(文字,数字, 符号)转换为计算机能够存储和处理的数字代码的规则系统，如ASCII,G BK, UTF-8等
# 文件操作基本步骤: 打开, 读/写, 关闭
# 注意: 如果操作完文件,并未调用close方法关闭文件,同时程序没有停止运行,那么这个文件就会一直被Python文件占用,无法操作

# 打开文件:
# "r" 是读的意思, "w" 是写的意思, encoding 是编码的意思
f= open("file.txt", "r", encoding =" utf-8")

# 读取文件
content = f.read()
print(content)

# 关闭文件
f.close()

# 写入文件
f.write()


# 1. 读取文件内容
# 打开文件
# encoding 关键字传参, 因为中间有一个参数没使用
f = open("resources/望庐山瀑布.txt", "r", encoding =" utf-8")

# 读取文件
content = f.read() # 读取所有内容
print(content)

content = f.readlines() # ['你好\n', '\n', '我是茉莉彩脂\n', '今年20岁\n', '专业是物联网工程\n', '爱好无\n']
# 一次性把所有的行都读出来
print(content)

content = f.readlines()
for line in content:
    print(line.strip()) # 去掉行末的换行符(去掉多余的空格)

# 2. 写入文件内容
# 打开文件
# 如果创建的文件不存在,会自动创建
f = open("resources/静夜思.txt", "w", encoding =" utf-8")

try:
    # 写文件
    # f.write() 一行一行的写入
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

    # f.writelines(), 一次性写入多行, 里面是列表的形式
    f.writelines(["静夜思(李白)\n\n", "床前明月光\n", "疑是地上霜\n", "举头望明月\n", "低头思故乡\n"])

finally: # 表示无论是否发生异常,都会执行, 通常用于关闭文件 --> 不推荐使用 try -- finally
    # 关闭文件
    f.close()



#------------------------------------------推荐使用方式--------------------------------------------
# with(上下文管理器): 核心作用就是确保资源总是被正确获取和释放(即使发生异常也会被正确释放), 也是项目开发中的推荐方式
# with 语句会在代码块执行完毕后自动关闭文件对象(调用 __exit__ 方法), 无需手动调用 close()
with open("resources/静夜思.txt", "w", encoding =" utf-8") as f:

    # 写文件
    # f.write() 一行一行的写入
    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")

    # f.writelines(), 一次性写入多行, 里面是列表的形式
    f.writelines(["静夜思(李白)\n\n", "床前明月光\n", "疑是地上霜\n", "举头望明月\n", "低头思故乡\n"])
