#------------------------------------------字符串-----------------------------------------

s1 = "hello" #双引号
s2 = 'world' #单引号
s3 = """
Hello World!
    Hello Python!
        Hello!
""" # 三引号(多行字符串)
print(s1)
print(s2)
print(s3)

print(type(s1))
print(type(s2))
print(type(s3))

#转义字符 \'  \"  \n  \t
msg1 = 'It\'s very good'
print(msg1)

msg2 = "It's very good"
print(msg2)

msg3 = "Hello的意思是\"您好\""
print(msg3)

msg4 = 'Hello的意思是"您好"'
print(msg4)

print("Hello World!Hello Python!")
print("Hello World!\nHello Python!")
print("\tHello World!\n\tHello Python!")

#-------------------------------------------字符串的拼接---------------------------------------
# 1.字符串的拼接 --> + 拼接
s1 = "人生苦短" "我用Python"        ",OK"
print(s1)

msg1 = "人生苦短"
msg2 = "我用Python"
print("龟叔说:" + msg1 + "," + msg2)
# 2.----
name = "茉莉"
age = "20" # 忘记给 20 加引号了, 是整数类型, 导致报错
pro = "物联网工程"
hobby = "python,AI"
print("大家好,我是" + name + "," + "今年" + age + "岁,学习的专业是"+ pro + ",爱好" + hobby)

# 3. str(int) --> 将int类型转为字符串
# # 字符串与非字符串不能拼接
name = "茉莉"
age = 20
pro = "物联网工程"
hobby = "python,AI"
print("大家好,我是" + name + "," + "今年" + str(age) + "岁,学习的专业是"+ pro + ",爱好" + hobby)

#-------------------------------------字符串的格式化-------------------------------------------
# 1. 字符串的格式化 --> 方式一: %s 占位符
name = "茉莉"
age = 20
pro = "物联网工程"
hobby = "python,AI"
print("大家好,我是 %s , 今年 %s 岁 , 学习的专业是 %s , 爱好 %s" %(name, age, pro, hobby))


# 2. 字符串的格式化 --> 方式二: f"...{变量名/表达式}..." (推荐用这个)
name = "茉莉"
age = 20
pro = "物联网工程"
hobby = "python,AI"
print(f"大家好,我是 {name} , 今年 {age} 岁 , 学习的专业是 {pro} , 爱好 {hobby}")


