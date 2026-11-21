import streamlit as st
import os
from openai import OpenAI
# import datetime
from datetime import datetime
import json
# 内存中存放的数据在计算机关机后或网页刷新就会消失, 要永久保存数据, 就需要将数据保存在文件之中


# 设置页面配置项(通常放在页面开头)
st.set_page_config(
    page_title="AI聊天机器人", # 网页标题
    page_icon="🧊", # 网页图标
    layout="wide", # 控制整个网页的布局, wide 占满网页的整个区域, 默认是居中
    initial_sidebar_state="expanded", # 控制的是侧边栏的状态
    menu_items={}
)

# 保存会话信息的函数
def save_session():
    if st.session_state.current_session:

        # 构建新的会话对象
        # 把代表整个当前会话的所有关键信息打包到一个新变量中,
        # 这个打包好的数据对象（session_data）的好处在于可以作为一个整体进行处理、传输或存储,
        # 使其与直接操作 st.session_state 的方式有所区分, 达到特定的处理或集成目的
        session_data = {
            "current_session": st.session_state.current_session,
            "nick_name": st.session_state.nick_name,
            "nature": st.session_state.nature,
            "messages": st.session_state.messages,
        }

        # 检查 sessions 目录是否存在
        # os.path.exists("sessions") 检查相对当前工作目录的 sessions 路径是否存在
        if not os.path.exists("sessions"):
            # 如果 sessions 目录不存在, 则创建
            os.mkdir("sessions")

        # 保存会话数据
        with open(f"sessions/{st.session_state.current_session}.json", "w", encoding="utf-8") as f:
            json.dump(session_data, f, ensure_ascii=False, indent=2)

# 生成会话标识的函数
def generate_session_name():
    # "%Y-%m-%d %H:%M:%S" 不能使用:, 否则创建json文件报错
    return datetime.now().strftime("%Y-%m-%d %H-%M-%S")

# 加载所有的会话列表
def load_sessions():
    session_list = []
    # 加载 session 目录下的文件,
    if os.path.exists("sessions"):
        # os.listdir(), 获取 sessions 目录下的所有文件, 返回值是 list
        file_list = os.listdir("sessions")
        for filename in file_list:
            # 只要文件名为 .json 的文件, 这是历史会话信息的文件
            if filename.endswith(".json"):
                # 列表的切片, 只需要文件名
                session_list.append(filename[:-5])

    # 因为 session_list.sort 返回值为 None, 所以不能直接返回, 需要先进行排序, 再返回
    # return session_list.sort(reverse=True)

    session_list.sort(reverse=True) # 按时间倒序排列, 因为 session_list.sort 返回值为空
    return session_list

# 加载指定的会话信息
def load_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            # 读取会话数据
            with open(f"sessions/{session_name}.json", "r", encoding="utf-8") as f:
                session_data = json.load(f)
                st.session_state.current_session = session_data["current_session"]
                st.session_state.nick_name = session_data["nick_name"]
                st.session_state.nature = session_data["nature"]
                st.session_state.messages = session_data["messages"]
    except Exception:
        # 显示错误信息
        st.error("加载会话失败!")

# 删除指定的会话信息
def delete_session(session_name):
    try:
        if os.path.exists(f"sessions/{session_name}.json"):
            os.remove(f"sessions/{session_name}.json") # 删除文件
            # 如果删除的是当前会话, 则需要更新列表
            if session_name == st.session_state.current_session:
                st.session_state.messages = [] # 更新当前会话的消息列表
                st.session_state.current_session = generate_session_name() # 生成新的会话标识
    except Exception:
        # 显示错误信息
        st.error("删除会话失败!")

# 大标题
st.title("AI聊天机器人")

# Logo
st.logo("resources/molicaizhi.jpg")

# 系统提示词
# 它的意思是: 我准备了一张试卷, 上面有两个空(%s 就是空位, s 代表 string 字符串)
# 注意: 这个时候, 这只是一张"空白的试卷", 并没有填答案
system_prompt= "你是一个非常可爱的助理, 你的名字叫 %s, 性格为 %s"

# 初始化聊天消息, 把消息存入列表, 包括用户和大模型的聊天内容
if 'messages' not in st.session_state: # st.session_state
    # st.session_state是Streamlit框架提供的一个基于会话的全局状态管理 容器, 由于 HTTP 协议是无状态的,
    # 且 Streamlit 在用户任何交互时都会自上而下重跑整个脚本, 普通的局部变量会被销毁
    # st.session_state 用于跨越重跑, 持久化保存属于当前特定用户会话的变量
    # 也是就因为网页一刷新, 代码就会从头运行, 之前存的变量全没了, 有了这个保险箱,
    # 你放进去的东西（比如聊天记录）就不会因为网页刷新而丢失, 只要网页不关，它就一直记得

    st.session_state.messages = []
    # session_state 是一个类似字典的对象, messages 是字典中的一个键, messages 对应的值是一个列表, 存储着聊天消息

    # 点号 . 是属性访问操作符。在面向对象编程中, 用于访问对象的内部属性（数据）或调用其方法（函数）
    # 在 A.B.C 这种链式结构中, 表示从 A 对象的命名空间中访问 B, 再从 B 中访问 C
    # 它是从大到小、层层包含的关系
    # st.session_state.messages 的意思就是：先找到 st 这个总管家, 掏它的口袋拿到记忆柜（session_state）,
    # 再掏记忆柜的口袋，拿到聊天记录抽屉（messages）

# 设置昵称初始值
if 'nick_name' not in st.session_state:
    st.session_state.nick_name = "小渔"
# 设置性格初始值
if 'nature' not in st.session_state:
    st.session_state.nature = "温柔可爱"

# 会话标识
if "current_session" not in st.session_state:
    # datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # %Y-%m-%d %H:%M:%S(格式化时间) --> %Y - 年, %m - 月, %d - 日, %H - 小时, %M - 分钟, %S - 秒
    # 没有 strftime("%Y-%m-%d %H:%M:%S") 秒是毫秒
    # st.session_state.current_message = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # 获取当前系统时间
    st.session_state.current_session = generate_session_name()

# 展示全部聊天信息, 遍历消息列表展示在网页中
st.text(f"会话名称{st.session_state.current_session}")
for message in st.session_state.messages:
# message = [{"role": "user", "content": prompt}, {"role": "assistant", "content": system_prompt}]
# 因为每一次对话都存入一次 user, assistant
    st.chat_message(message["role"]).write(message["content"])

    # if message["role"] == "user":
    #     st.chat_message("user").write(message["content"])
    # elif message["role"] == "assistant":
    #     st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象, os.environ 拿到系统的所有环境变量, get 就是得到某个变量
# DEEPSEEK_API_KEY 是环境变量的名字, 值就是DeepSeek的API_KEY的值
# client = OpenAI(api_key=os.environ.get('DEEPSEEK_API_KEY'),base_url="https://api.deepseek.com",)

# 调用本地部署大模型
# 下面这行正在运行的代码：是连接【本地 Ollama 部署的大模型】
# api_key="ollama"：因为本地跑模型不需要云端校验，所以随便填个假密码（非空即可）骗过格式检查。
# base_url="http://127.0.0.1:11434/v1": 告诉代码去连本机（127.0.0.1）的 11434 端口（Ollama 默认服务端口
# 每个软件都有自己的默认端口号, 根据端口号找到软件, 如果没有启动软件或者敲错端口号, 就会报错 "连接失败"
# 127.0.0.1 是本地主机的 IP 地址，表示连接本机 --> 本地回环地址
# /v1 是为了兼容 OpenAI 的标准接口格式。
client = OpenAI(api_key="ollama", base_url="http://127.0.0.1:11434/v1")

# # 左侧侧边栏(要在左侧侧边栏添加元素, 必须加.sidebar, 否则会出现在主界面)
# # 如果添加元素多, 就会一直出现 .sidebar, 不方便) --> 不推荐
# st.sidebar.subheader("AI聊天机器人信息")
# nick_name = st.sidebar.text_input("昵称")

# 左侧侧边栏 --> 推荐
# with: streamlit 中的上下文管理器
with st.sidebar:

    st.subheader("AI控制面板")

    # 新建会话的按钮
    # button 的宽度与里面的 content 宽度一致, 默认情况下, button 的宽度会根据 content 的长度自动调整
    # width = "stretch" 表示按钮的宽度会拉伸到最大宽度, 使其占满整行
    # 所以你创建新对话, 虽然内容保存了, 但对话内容还在页面中显示
    if st.button("新建会话", width = "stretch", icon = "🚀"):
        # Streamlit是自上而下全脚本重跑模型 ：
        # 1. 页面上所有交互组件 st.button 只有在本次脚本跑完之后(渲染页面), 才会去判断按钮有没有被点击,
        # 2. 一旦检测到按钮点击, 触发一次全新的完整脚本重跑
        # 3. 重跑时：st.button(...)这一行会返回True,进入 if 内部代码, 执行里面的逻辑, 保存当前会话的内容
        # 4. 虽然内容保存了, 你创建新对话, 但对话内容还在页面中显示, 这时候 st.rerun(), 就会重新运行脚本, 重新渲染页面

        # 1. 保存当前会话
        save_session()

        # 为了方便使用, 和侧边栏结构更清晰, 把以下代码定义成一个函数

        # 1. 保存当前会话
        # 首先检查 st.session_state.current_message 是否存在且不为空, 只有在这个条件为真时, 才会执行下面的代码
        # if st.session_state.current_message:
        #
        #     # 构建新的会话对象
        #     # 把代表整个当前会话的所有关键信息打包到一个新变量中,
        #     # 这个打包好的数据对象（session_data）的好处在于可以作为一个整体进行处理、传输或存储,
        #     # 使其与直接操作 st.session_state 的方式有所区分, 达到特定的处理或集成目的
        #     session_data = {
        #         "messages": st.session_state.messages,
        #         "nick_name": st.session_state.nick_name,
        #         "nature": st.session_state.nature,
        #         "current_message": st.session_state.current_message,
        #     }
        #
        #     # 检查 sessions 目录是否存在
        #     # os.path.exists("sessions") 检查相对当前工作目录的 sessions 路径是否存在
        #     if not os.path.exists("sessions"):
        #         # 如果 sessions 目录不存在, 则创建
        #         os.mkdir("sessions")
        #
        #     # 保存会话数据
        #     with open(f"sessions/{st.session_state.current_message}.json", "w", encoding="utf-8") as f:
        #         json.dump(session_data, f, ensure_ascii=False, indent=2)

        # 2. 创建新的对话
        # 会出现两份 json 文件, 一份是当前会话, 一份是新的会话, 当前会话会直接保存当前对话的内容, 新的对话则是一个空列表
        # 那些昵称, 性格就不用重新创建了, 有默认值, 只需要创建一个空的会话列表即可
        if st.session_state.messages: # 如果当前会话存在(True), 则创建新的会话, 否则不创建
            st.session_state.messages = []
            # 这段代码和 会话标识 的代码一致, 可以定义为一个函数
            st.session_state.current_session = generate_session_name()
            # 保存当前会话
            save_session()
            st.rerun() # 重新运行页面

    # 会话历史
    # st.text 普通文本, 无样式
    st.text("会话历史")
    session_list = load_sessions()
    for session in session_list:
        # 将一行分若干列, 4:1 的比例, 一行能放多个元素
        col1, col2 = st.columns([4,1])
        with col1:
            # 加载会话信息
            # 三元运算符: 如果条件为真, 则返回第一个表达式的值; 否则返回第二个表达式的值 --> 语法: 表达式1 if 条件 else 表达式2
            # 如果点击当前会话等于 st.session_state.current_session, 则按钮类型为 "primary", 否则为 "secondary"
            if st.button(session, width="stretch", icon="📄", key=f"load_{session}", type="primary" if session == st.session_state.current_session else "secondary"):
                load_session(session)
                st.rerun()
        with col2:
            # 删除会话信息
            # 在循环中相同元素不断出现, 每个组件都要有唯一标识, 否则就会报错
            if st.button("", width="stretch", icon="❌", key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分割线
    st.divider()
    
    st.subheader("AI聊天机器人信息")
    # 昵称输入框
    # st.text_input --> 单行输入框
    # 长什么样: 网页上只会出现一个很窄的单行输入框（就像你平时登录账号输密码的那个框）
    # 适用场景: 适合输入短小、单行的文本, 比如：昵称、年龄、城市名、搜索关键词
    # 限制: 如果你敲了回车, 它就自动把内容交出去了，不能换行
    # placeholder 提示占位符, value 提供初始值, 这个初始值前面定义了
    nick_name = st.text_input("昵称", placeholder="请输入昵称", value=st.session_state.nick_name)
    # 修改昵称的初始值
    if nick_name:
        st.session_state.nick_name = nick_name

    # 性格输入框
    # st.text_area --> 多行输入框
    # 长什么样: 网页上会出现一个很大的、有高度的矩形框（就像你在论坛发帖、写长评论的那个大框)
    # 适用场景: 适合输入较长、需要换行的文本
    # 比如: 你的性格描述、个人简介、一大段提示词（Prompt）、或者用户的长篇大论
    # 特点: 在这个框里, 你按回车键是换行, 不会直接提交, 你可以写很长很长的一篇小作文
    nature = st.text_area("性格", placeholder="请输入性格描述", value=st.session_state.nature)
    # 修改性格的初始值
    if nature:
        st.session_state.nature = nature

# 消息输入框
prompt = st.chat_input("请输入您问的问题") # 创建一个消息输入框, ( ) 里面是提示占位符(Placeholder)
if prompt: # 字符串会自动转化为布尔值, 如果字符串非空, 则为True; 否则为False
    st.chat_message("user").write(prompt)
    #    -> 作用：专门用来生成“聊天气泡”。
    #    -> 特点：会在网页上生成一个带有头像、圆角背景框的聊天对话框，非常美观。适合做聊天机器人界面。

    # st.write(f"用户: {prompt}")
    #    -> 作用：普通的文本输出。
    #    -> 特点：仅仅是在网页上打印一段白底黑字的普通文本，没有头像和气泡框。通常用来展示普通说明或数据。

    print(f"------------> 调用AI大模型, 提示词: {prompt}")

    # 保存用户输入的提示词
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 在控制台输出日志
    #    -> 作用：在控制台输出调试日志。
    #    -> 特点：只有在终端黑框框（或PyCharm底部控制台）才能看到，网页上看不见。
    #    -> 注意：这是给“程序员”看的，用于确认数据是否成功传递给后端。

    # 与AI大模型进行交互()
    response = client.chat.completions.create(
        # model="deepseek-flash",
        model="deepseek-r1:8b",
        # 如果调用的本地模型没有下载, 就会报错 "找不到模型"
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.nick_name, st.session_state.nature)},
            # system_prompt % (st.session_state.nick_name, st.session_state.nature) 把昵称和性格填入系统提示词中
            # 然后把系统提示词填入大模型, 系统提示词要在定义默认值前面

            *st.session_state.messages, # 解包消息列表
            # 我的疑惑: --> 为什么不把与AI大模型进行交互的代码放在回复后面,
            # 如果把与AI大模型进行交互的代码放在大模型回复后面, 还没调用大模型, 进行不了回复, 随后报错
            # 解释:
            # 先输入 -> 再解包发给AI -> 等AI返回结果 -> 最后把你们俩的对话存入本地档案
            # 1. 用户输入了提示词。
            # 2. 代码去执行解包（此时列表里必须有用户和大模型的聊天内容，不然大模型不知道你问了啥）。
            # 3. 把解包后的内容发给大模型。
            # 4. 大模型思考几秒钟，吐出大模型的回复 。
            # 5. 代码拿着大模型的回复，用 append 存进本地的列表里。

        ],
        # stream=False, # 非流式输出
        stream=True,
        # reasoning_effort="high", # 推理强度: 高
        # extra_body={"thinking": {"type": "enabled"}}, # 开启思考过程
    )

    # 输出大模型返回的结果(非流式输出的解析方式)
    # print("<------------大模型返回的结果: ", response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 输出大模型返回的结果(流式输出的解析方式)
    response_message = st.empty()
    # st.empty() 创建一个空的组件, 用于显示大模型的回复, 每次在这个空组件覆盖刷新
    # 没有这个, 大模型每吐一个字就会输出一个聊天气泡框

    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            # 根据APIfox的流式输出json代码
            context = chunk.choices[0].delta.content
            full_response += context
            response_message.chat_message("assistant").write(full_response)

    # 保存大模型返回的结果
    st.session_state.messages.append({"role": "assistant", "content": full_response})

    # 保存会话, 如果不点击新建会话, 直接点击最新的会话历史记录会导致会话记录丢失
    save_session()
