import json

# 写入json文件
user = {
    "name": "茉莉彩脂",
    "age": 20,
    "gender": "女",
    "hobbies": ["reading", "gaming", "coding"],
}

with open("resources/user.json", "w", encoding="utf-8") as f:
    # ensure_ascii: 默认为 True, 确保所有的数据输出的数据都是ascii码(非ascii码会进行转义), False 表示不进行转义
    # indent = 2 每个 key 值占一行, 缩进为 2 个空格
    # dump() 将 Python 对象序列化为 JSON 格式字符串 写入文件
    # obj = user 保存的数据, f 文件对象
    json.dump(user, f, ensure_ascii = False , indent = 2)

# 读取json文件
with open("resources/user.json", "r", encoding="utf-8") as f:
    # load() 从文件中读取 JSON 格式数据,并将其反序列化为 Python 对象
    user = json.load(f)
    print(user)
    print(type(user)) # <class 'dict'>


