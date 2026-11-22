# Python-Learning-Journey
用来记录我的 Python 学习路程
## 项目结构
- **Python入门**：Python 入门练习
- **Python核心语法**：数据类型、流程控制、数据容器、函数、模块、包、面向对象、异常处理
- **AI应用**：文件操作、DeepSeek API 调用、Streamlit、JSON、AI 伙伴小项目
- **Python爬虫**：requests 抓网页、lxml/xpath 解析、CSV、正则表达式、电影榜单案例
## 目录说明
### 1. Python入门
Python 入门练习，用来熟悉 PyCharm 的运行环境和 Python 的基本写法
### 2. Python核心语法
- **数据存储与运算**：学习了 Python 中基本的数据类型、输入与输出、运算符、字符串的拼接与格式化、数据的基本运算
- **流程控制语句**：学习了 if 条件判断、match 模式匹配、for、while 循环
- **数据容器**：学习了 list（列表）、string（字符串）、tuple（元组）、dict（字典）、set（集合）
- **函数**：学习了函数基础、函数进阶
- **导入模块**：学习了怎么导入模块
- **自定义模块**：学习了怎么自定义模块，怎么导入自定义模块
- **utils**：存放通用工具函数的文件夹，把重复用到的小功能单独抽出来，方便别的代码调用和管理，有 `__init__.py` 作为标识
- **包**：学习怎么调用 utils 中的功能
- **面向对象编程**：学习了面向对象的基础知识，完成了一个教务管理系统的小项目案例，在此基础上完成了购物车管理系统的练习
- **异常处理**：学习了怎么处理异常，在此基础上处理了教务管理系统小项目案例出现的异常
### 3. AI应用
- 学习了文件的基本操作和扩展操作
- 学习了把 API_KEY 配置成环境变量，通过 os 模块读取，使用 `openai` 库调用 DeepSeek 官方模型，以及本地 Ollama 部署的 deepseek‑r1:8b
- 学习了 Streamlit 网页界面的基础
- 学习了基于 json 模块对 JSON 数据的读写与解析
- 基于以上基础完成了 AI 伙伴小项目的练习，包括学习了怎么流式输出，使用 datetime 模块获得系统时间
### 4. Python爬虫
- 了解爬虫的基本流程和 robots 协议，使用 requests 发送 HTTP 请求抓取网页
- 使用 lxml 配合 xpath 语法解析 HTML、提取数据，在 `resources/仙逆人物志.html` 上练习 xpath 的各种写法
- 学习到了什么是 CSV 文件，学会了怎么操作 CSV 文件，推荐方式是使用 csv 模块
- 学习了正则表达式基础和正则表达式基本语法，需要使用 re 模块
- 在这些基础上完成了爬取高分电影榜单 Top100 数据，并保存在 CSV 文件中的案例，最后利用正则表达式对这些数据进行数据清洗
## 环境依赖
- Python 3.14.10
- 第三方库：`streamlit`、`openai`、`requests`、`lxml`
- 安装命令：`pip install streamlit openai requests lxml`
- DeepSeek 的 API_KEY 通过环境变量配置，**不要直接把密钥写在代码内**




