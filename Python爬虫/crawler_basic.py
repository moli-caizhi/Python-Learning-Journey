#-------------------------------------------爬虫步骤--------------------------------------------
"""


    爬虫: 也称为网络爬虫(网络机器人), 是一种按照一定的预设规则, 自动浏览并抓取网络数据的程序或脚本

             如果还有其他任务, 第一次处理完, 继续处理, 直到所有任务处理完, 爬虫结束
                        ------------------------------------
                       |                                   |
                       v                                  |
    步骤: 开始 --> 发送HTTP请求 --> 解析结果提取数据 --> 数据处理(清洗) --> 数据存储 --> 结束

    数据清洗: 是指对采集到的原始数据进行处理、修正、转换和标准化的过程, 目的是让数据变得规范、准确
"""


#---------------------------------------robots协议--------------------------------------------
"""
    robots协议也称为爬虫协议、爬虫规则, 是指网站根目录下存放的一份文本文件robots.txt,
    用于告诉爬虫哪些页面可以抓取, 哪些页面不能抓取(君子协议)
    Ctrl + f --> 搜索
    域名/robots.txt, 访问该网站的robots.txt文件, 即可查看该网站的爬虫规则
    
    安装: pip install requests 
"""

# -------------------------------------发送 HTTP 请求-----------------------------------------
# import requests
#
# # 定义url
# # 目标url
# target_url = "https://www.tiobe.com/tiobe-index/"
#
# # 发送请求, 获取数据
# response = requests.get(target_url)
#
# # 输出数据到控制台 --> 获取到的是网页的前端代码
# print(response.text)

#------------------------------------解析网页数据结果提取数据---------------------------------------
# xpath路径可以不用自己找来写, 打开浏览器, 按下 F12, 找到需要解析的元素, 右键, 复制, xpath
# 复制 xpath 从任意位置开始
# 复制完整的 xpath 就是从根目录开始

import requests
from lxml import html

# 定义url
target_url = "https://www.tiobe.com/tiobe-index/"

# 发送请求, 获取数据
response = requests.get(target_url)

# 解析 HTML 文件, 将其转换为一个文本对象
document = html.fromstring(response.text)

# 解析表头数据
# th_list = document.xpath("//table[@id='top20']/thead/tr/th/text()")
# th_list = document.xpath("/html/body/section/div/article/table[1]/thead/tr/th/text()") # -- 复制完整的 xpath
th_list = document.xpath("//*[@id='top20']/thead/tr/th/text()")  # -- 复制 xpath 从任意位置开始
print(th_list) # --> 结果都一样

# 解析表格中的数据
tr_list = document.xpath("//table[@id='top20']/tbody/tr")
for tr in tr_list:
    td_list = tr.xpath("./td/text()")
    print(td_list)


