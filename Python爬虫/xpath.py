#---------------------------------------xpath语法----------------------------------------------
# Xpath：是一种用于在HTML / XML文档中导航或定位元素的查询语言，让你能够准确的定位文档中的特定元素、属性或文本
# text() : 获取标签的文本内容
# [@属性] 或 [@属性='值'], 需要 text() 获取该标签属性的文本内容
# @ | @* | @属性 : 获取属性的值, 不用text()

from lxml import html

with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 解析 HTML 文件, 将其转换为一个文本对象
    document = html.fromstring(html_text)

    """
        解析表头:
        /table/thead/tr/th/text()  
        / --> 表示从根结点开始 --> 根结点是 <html>
          
        th_list = document.xpath("/table/thead/tr/th/text()")
        print(th_list) --> []   
          
        // --> 表示从任意位置开始   
        
        . 在crawler_basic.py中, 遍历所有<tr>, 并获取<tr>中的<td>中的文本内容
    """
    # th_list = document.xpath("//thead/tr/th/text()")
    # th_list = document.xpath("//table/thead/tr/th/text()")
    th_list = document.xpath("/html/body/div/div/table/thead/tr/th/text()")
    print(th_list) # 都是 --> ['姓名', '性别', '头像', '修为', '技能', '身份地位', '师承', '法宝']

    # tr[1] : 表示匹配第一个 tr 标签
    td_list = document.xpath("//tbody/tr[1]/td/text()")
    print(td_list)

    # tr[last()] : 表示匹配最后一个 tr 标签
    td_list = document.xpath("//tbody/tr[last()]/td/text()")
    print(td_list)

    # tr[last()-1] : 表示匹配最后二个 tr 标签, last() 可以进行算数运算
    td_list = document.xpath("//tbody/tr[last()-1]/td/text()")
    print(td_list)

    # 获取 p 标签文本内容
    p_list = document.xpath("//p/text()")
    print(p_list)

    # p[@class]: 表示匹配 class 属性的 p 标签, @ 表示属性
    p_list = document.xpath("//p[@class]/text()")
    print(p_list) # --> ['探索修真世界的奥秘，记录修仙路上的传奇']
    # p[@class='xn']: 表示匹配 class 属性为 xn 的 p 标签
    p_list = document.xpath("//p[@class='xn']/text()")
    print(p_list) # --> ['探索修真世界的奥秘，记录修仙路上的传奇']

    # * : 表示匹配任意标签
    th_list = document.xpath("//thead/tr/*/text()")
    print(th_list)

    # @src : 表示匹配 src 属性的值 --> 指定属性
    # @* : 表示匹配任意属性的值
    a_list = document.xpath("//td/img/@src")
    print(a_list)
    a_list = document.xpath("//td/img/@*")
    print(a_list)

# ------------------------------------解析网页数据结果提取数据---------------------------------------
"""
    一个网页是由三个部分组成的，分别是：HTML、CSS、JS（JavaScript）
    HTML: 超文本标记语言, 由一堆预设的标签(<h1>一级标题</h1>)构成.  HTML负责网页的结构（页面元素和内容）
    CSS: 层叠样式表. CSS负责网页的表现（页面元素的外观、位置等样式, 如颜色、大小等）--> <style> </style>
    JS: 全称为JavaScript, 简称JS. 负责网页的行为（交互效果） --> <script> </script>
"""

"""
    lxml：是一个高性能的HTML/XML文档的解析库，支持基于Xpath语法来解析和获取网页数据。
    Xpath：是一种用于在HTML/XML文档中导航或定位元素的查询语言，让你能够准确的定位文档中的特定元素、属性或文本 

    安装: pip install lxml
"""

# 解析 HTML 中的数据
from lxml import html

# 读取 HTML 文件
with open("resources/仙逆人物志.html", "r", encoding="utf-8") as f:
    html_text = f.read()

    # 1. 解析 HTML 文件, 将其转换为一个文本对象
    document = html.fromstring(html_text)

    # 解析表头 -- 2. xpath 语法 --> //.../.../text() -- 获取文本数据
    th_list = document.xpath("//table/thead/tr/th/text()")
    print(th_list, "\n")

    # 解析表格中的第一个数据, 这个索引从 1 开始
    td_list = document.xpath("//table/tbody/tr[1]/td/text()")
    print(td_list, "\n")

    # 解析表格中的所有数据
    td_list = document.xpath("//table/tbody/tr/td/text()")
    print(td_list, "\n")

    # 解析表格中的所有数据, 并将数据分别存储到列表中
    tr_list = document.xpath("//table/tbody/tr")
    for tr in tr_list:
        # 注意: ./ 表示当前节点, 不是 .// --> .表示从当前节点开始
        td_list = tr.xpath("./td/text()")
        print(td_list)
