#-----------------------------------TMDB-TOP300电影榜单数据统计-----------------------------------
# 本文件由同目录下的 Jupyter Notebook (TMDB_TOP300_movies_analysis.ipynb) 改写而来，
# 将原本平铺在单元格中的代码，按功能拆分为若干函数，便于复用和维护

import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.axes import Axes

# Notebook 中相对路径以 Notebook 所在目录为基准；.py 文件运行时的当前工作目录不一定相同，
# 因此这里以脚本自身所在目录为基准拼接路径，避免因运行位置不同而找不到文件
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_PATH = os.path.join(BASE_DIR, "data", "movies.csv")
OUTPUT_PATH = os.path.join(BASE_DIR, "data", "TMDB_TOP300_movies_analysis.png")


def setup_chinese_font():
    """配置 matplotlib 运行时参数，使其能正常展示中文"""
    plt.rcParams['font.sans-serif'] = ['SimHei']


def create_figure():
    """创建 2x2 的子图布局，用于放置 4 个统计图表，返回 figure 和 4 个子图"""
    figure, axes = plt.subplots(nrows=2, ncols=2, figsize=(20, 12), dpi=100)
    figure.suptitle("TMDB-TOP300电影榜单数据统计", fontsize=20, x=0.5, y=0.98) # 设置主标题, x: 主标题水平位置, y: 主标题垂直位置
    figure.subplots_adjust(wspace=0.3, hspace=0.4) # 调整子图之间的间距, wspace: 水平间距, hspace: 垂直间距

    axes1: Axes = axes[0][0]
    axes2: Axes = axes[0][1]
    axes3: Axes = axes[1][0]
    axes4: Axes = axes[1][1]

    return axes1, axes2, axes3, axes4


def load_data() -> pd.DataFrame:
    """
    加载电影数据
    int64: 整型数字(不支持空值)
    Int64: 整型数字(支持空值)
    float64: 浮点型数字(支持空值)
    """
    df = pd.read_csv(
        DATA_PATH,
        usecols=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言"],
        dtype={"年份": "Int64"}
    )
    return df


def plot_year_count(axes: Axes, df: pd.DataFrame):
    """统计 TOP300 的电影中，每一年上映的电影数量的变化（折线图）"""
    # 1. 缺失值/异常值的处理：年份缺失时，用"上映时间"的前 4 位(即年份)填充
    df["年份"] = df["年份"].fillna(df["上映时间"].str[0:4])

    # 2. 分组统计
    year_count = df.groupby('年份')['年份'].count()

    # 3. 组装数据
    # x 轴数据
    # year_count 的索引只有有电影的年份，是断断续续的
    # 如果直接拿索引当 x，年份中间会跳过去，折线就不是连续时间线
    # 所以手动生成从最早到最晚的全部连续年份作为 x；找不到的年份用 .get 填 0
    min_year = year_count.index.min()
    max_year = year_count.index.max()
    x = [i for i in range(min_year, max_year + 1)]

    # y 轴数据
    # 遍历所有连续年份，存在该年份就取电影数量，不存在则取 0，统一转为整数，生成 y 轴数据
    y = [int(year_count.get(i, 0)) for i in x]

    # 4. 绘制折线图
    axes.plot(x, y, color='green')  # 折线图
    axes.set_title('每年电影数量变化折线图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('年份', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签

    axes.set_xticks(x[::8])  # 设置X轴刻度间隔
    y_ticks = [i for i in range(0, 31, 3)]
    axes.set_yticks(y_ticks)  # 设置Y轴刻度间隔
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线


def plot_language_count(axes: Axes, df: pd.DataFrame):
    """统计对比不同语言电影数量（柱状图）"""
    # 1. 获取不同语言对应的电影数量
    language_count = df.groupby('语言')['语言'].count().sort_values(ascending=False)

    x_language = language_count.index.tolist()
    y_language_count = language_count.values.tolist()

    # 2. 绘制柱状图
    axes.bar(x_language, y_language_count, color='green', width=0.7)  # 柱状图
    axes.set_title('不同语言电影数量柱状图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('语言', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线
    axes.tick_params(axis='x', rotation=90)  # 旋转X轴标签


def plot_type_count(axes: Axes, df: pd.DataFrame):
    """统计对比不同类型电影数量（柱状图）"""
    # 1. 获取不同类型的电影数量 --> 用字典存储
    type_count = {}  # {'剧情': 5, '犯罪': 3}

    for types in df['类型'].str.split(','):  # ['剧情', '犯罪']
        for type in types:  # '剧情'
            if type in type_count:  # 如果类型在字典中
                type_count[type] += 1  # 值加1
            else:
                type_count[type] = 1

    # type_count.keys() --> type: <class 'dict_keys'>(视图对象, 跟着原字典实时变动) --> 不支持索引，需要转换为列表
    x_types = list(type_count.keys())  # 类型列表
    y_values = list(type_count.values())  # 数量列表

    # 2. 绘制柱状图
    axes.bar(x_types, y_values, color='green', width=0.7)  # 柱状图
    axes.set_title('不同类型电影数量柱状图', fontsize=18)  # 添加子图标题
    axes.set_xlabel('类型', fontsize=12)  # 添加X轴标签
    axes.set_ylabel('电影数量', fontsize=12)  # 添加Y轴标签
    axes.grid(linestyle='--', alpha=0.5)  # 添加网格线
    axes.tick_params(axis='x', rotation=90)  # 旋转X轴标签


def plot_score_ratio(axes: Axes, df: pd.DataFrame):
    """统计对比各部电影评分的比例（饼状图）"""
    # 1. 获取各部电影评分的比例
    score_count = df.groupby('评分')['评分'].count()

    # 2. 合并小数据(比例小于 2%) --> 其他
    total = score_count.sum()
    large_scores = score_count.loc[score_count >= total * 0.02]  # 大数据, 比例 >= 2%
    small_scores = score_count.loc[score_count < total * 0.02]  # 小数据, 比例 < 2%

    # small_scores.shape 说明一共有多少行 --> 返回一个元组, (2,)
    # small_scores.shape[0] --> 取这个元组里的第 1 个值, 也就是元素个数(行数 --> 2)
    # if small_scores.shape[0] > 0 如果小数据行数大于 0, 就是有小数据
    if small_scores.shape[0] > 0:
        # Series 本质就是: 索引(index)-> 值(values)的映射, 跟字典的[key -> value]结构是同一套思想
        # 没有的索引项, 可以直接新增
        large_scores['其他'] = small_scores.sum()  # 把所有占比不足2%的分组数量求和, 新增其他索引项

    scores = large_scores.index.tolist()  # 评分列表
    scores_values = large_scores.values.tolist()  # 数量列表

    # 3. 绘制饼状图
    axes.pie(scores_values, labels=scores, autopct='%1.1f%%', startangle=0, radius=1.2)  # startangle 起始角度, radius=1.2 调整饼状图的半径
    axes.set_title('不同评分电影数量占比饼状图', fontsize=18)
    axes.legend(loc='lower center', ncol=4, bbox_to_anchor=(0.5, -0.2))  # bbox_to_anchor : 图例位置


def main():
    """串联各个步骤，完成数据的加载、4 个图表的绘制与保存展示"""
    # 1. 准备工作：配置运行时参数、创建子图完成基本布局、加载数据
    setup_chinese_font()
    axes1, axes2, axes3, axes4 = create_figure()
    df = load_data()

    # 2. 依次绘制 4 个子图
    plot_year_count(axes1, df)      # 统计每年上映电影数量变化（折线图）
    plot_language_count(axes2, df)  # 统计不同语言电影数量（柱状图）
    plot_type_count(axes3, df)      # 统计不同类型电影数量（柱状图）
    plot_score_ratio(axes4, df)     # 统计不同评分电影数量占比（饼状图）

    # 3. 保存图片并展示
    plt.savefig(OUTPUT_PATH)
    plt.show()


if __name__ == '__main__':
    main()
