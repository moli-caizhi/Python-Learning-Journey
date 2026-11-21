# Please install OpenAI SDK first: `pip3 install openai`
import os
from openai import OpenAI

# 创建与AI大模型交互的客户端对象, os.environ 拿到系统的所有环境变量, get 就是得到某个变量
# DEEPSEEK_API_KEY 是环境变量的名字, 值就是DeepSeek的API_KEY的值
client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com",)

# 与AI大模型进行交互()
response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[
        {"role": "system", "content": "你是一个非常可爱的助理, 你的名字叫小渔, 会使用温柔可爱的语气回答用户的问题"},
        {"role": "user", "content": "你好, 你能为我做什么?"},
    ],
    stream=False,
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

# 输出大模型返回的结果
print(response.choices[0].message.content)