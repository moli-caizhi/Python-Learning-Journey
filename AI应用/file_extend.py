#------------------------------------------文件扩展------------------------------------------
"""
路径的写法:
    1. 相对路径: 从当前文件所在目录开始查找 --> 推荐: 可移植性好, 代码简洁, 便于阅读
        . : 表示当前目录 --> ./resources/望庐山瀑布.txt  ./ 可以省略
        .. : 表示上一级目录 --> ../上一级目录的子目录/文件.txt
        ../../ : 表示上两级目录 --> ../../上两级目录的子目录/文件.txt
    2. 绝对路径: 从文件系统的根目录开始查找, 文件位置的完整路径(注意: \ 在字符串中表示的是转义字符, 如: \n, \t)
    C:\Python-Project\py_project01\AI应用\resources\望庐山瀑布.txt --> 不能写成这样
    写成这样:
    方式一: C:\\Python-Project\\py_project01\\AI应用\\resources\\望庐山瀑布.txt
    方式二: C:/Python-Project/py_project01/AI应用/resources/望庐山瀑布.txt
"""


"""
操作模式:
    r：只读的方式打开文件，指针放在文件的开头。（默认模式）
    w：只写入模式，从头编辑，原有内容会被删除；文件不存在则创建新文件
    a：追加模式，新内容会被追加在原有内容之后；文件不存在则创建新文件
"""
# 读取文件
with open("resources/望庐山瀑布.txt", "r", encoding =" utf-8") as f:

    content = f.read() # 读取所有内容
    print(content)

# 写文件 --> 追加内容
# a: append
with open("resources/静夜思.txt", "a", encoding =" utf-8") as f:

    f.write("静夜思(李白)\n\n")
    f.write("床前明月光\n")
    f.write("疑是地上霜\n")
    f.write("举头望明月\n")
    f.write("低头思故乡\n")