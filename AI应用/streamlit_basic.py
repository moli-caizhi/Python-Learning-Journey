import streamlit as st

# 设置页面配置项(通常放在页面开头)
st.set_page_config(
    page_title="streamlit入门", # 网页标题
    page_icon="🧊", # 网页图标
    layout="wide", # 控制整个网页的布局, wide 占满网页的整个区域
    initial_sidebar_state="expanded", # 控制的是侧边栏的状态, 我目前的网页没有侧边栏
    menu_items={  # 菜单的信息
        'Get Help': 'https://www.deepaeek.com',
        'Report a bug': "https://Ollama.com",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

# 标题
st.title("streamlit入门")
st.header("这是一级标题")
st.subheader("这是二级标题")

# 段落文字
st.write("AI 是很好的学习助手，但不能直接代替我们思考")
st.write("AI 可以帮我们梳理知识点、解释难懂的概念、提供解题思路、整理背诵提纲、翻译文字，帮我们节省查找资料的时间。遇到卡住的题目，我们可以让 AI 提示方向")
st.write("我现在正在学streamlit")
st.write("我喜欢学Python")

# 图片
# 在当前目录前面可以不用 ./
st.image("resources/molicaizhi.jpg")
# st.image("./resources/caizhimoli.png",width=300)

# 音频
st.audio("resources/news.mp3")

# 视频
st.video("resources/news.mp4")

# Logo --> 在左上角
st.logo("resources/caizhimoli.png")

# 表格
student_data = {
    # 表头: key
    "姓名": ["王林", "李慕婉", "贝罗", "莫厉海", "石萧"],
    "学号": ["20260001", "20260002", "20260003", "20260004", "20260005"],
    "语文": [98, 90, 59, 29, 80],
    "数学": [88, 78, 65, 70, 39],
    "英语": [99, 89, 87, 59, 62],
    "总分": [285, 257, 211, 158, 181]
}
st.table(student_data)

# 输入框
# 普通输入框
name = st.text_input("请输入姓名: ")
st.write("您输入的姓名为: ", name)
# 密码输入框
password = st.text_input("请输入密码: ", type = "password")
st.write("请输入您的密码: ", password)

# 单选按钮
# 默认为男, 索引为0
gender = st.radio("请输入您的性别:", ["男", "女", "未知"], index = 2)
st.write(f"您的性别为: {gender}")