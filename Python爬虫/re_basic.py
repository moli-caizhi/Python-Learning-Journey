#------------------------------------------正则表达式基础---------------------------------------
# 正则表达式（Regular Expression）是一种用特定语法规则组成的字符串模式，
# 用来描述、匹配或替换文本中符合某种规则的字符序列，可以理解为是专门用于文本处理的“高级查找和匹配公式”。

import re

s1 = "18809090000是我的手机号, 你记住了吗? 我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗?"
s2 = "我的手机号是18809090000, 你记住了吗? 我的另一个手机号是18800008888，两个QQ号分别是155998992 和 18809091293821 你记住了吗?"

# r 让字符串表达本身的含义, 如: 转义字符不生效

# match - 从字符串的开头开始匹配(匹配第一个匹配项) ----> Match 对象
# .group() 是 Match 对象的实例方法, 获取匹配的结果
result = re.match(r"1[3-9]\d{9}", s1)
print(result) # <re.Match object; span=(0, 11), match='18809090000'>
print(result.group()) # 获取匹配的结果 --> 18809090000
print(result.span()) #获取匹配的索引 --> (0, 11)
print(result.start()) # 获取匹配的开始索引 --> 0
print(result.end()) # 获取匹配的结束索引 --> 11

# result = re.match(r"1[3-9]\d{9}", s2) # None
# print(result.group()) # 报错, 原因: result 是 None, None 没有 group() 方法

# search - 从任意位置开始, 搜索第一个匹配项 ----> Match 对象
result = re.search(r"1[3-9]\d{9}", s2)
print(result) # <re.Match object; span=(6, 17), match='18809090000'>
print(result.group()) # 获取匹配的结果 --> 18809090000
print(result.span()) #获取匹配的索引 --> (6, 17)
print(result.start()) # 获取匹配的开始索引 --> 6
print(result.end()) # 获取匹配的结束索引 --> 17

# findall - 从任意位置开始, 搜索所有匹配项 ---> list
result = re.findall(r"1[3-9]\d{9}", s2)
print(result) # ['18809090000', '18800008888', '18809091293']


