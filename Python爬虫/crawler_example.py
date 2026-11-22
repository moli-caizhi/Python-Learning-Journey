#---------------------------------------------案例----------------------------------------------
# 获取高分电影榜单(Top100)数据，并保存在CSV文件中
# 数据包括：电影名、年份、上映时间、类型、时长、评分、语言、导演、作者、主演、Slogan(宣传语)、简介

import requests
from lxml import html
import csv

# 常量
TMDB_BASE_URL = "https://www.themoviedb.org"
TMDB_TOP_URL_1 = "https://www.themoviedb.org/movie/top-rated" # 高分电影榜单的URL(默认第1页)
TMDB_TOP_URL_2 = "https://www.themoviedb.org/discover/movie/items" # 高分电影榜单的URL(默认第2页)

# 保存所有电影数据
def save_all_movies(all_movies):
    with open("resources/all_movie.csv", "w", newline="", encoding="utf-8") as csvfile:
        # 我出现的问题: --> fieldnames 里写 "Slogan", 而字典里写的是 "宣传语"
        # csv.DictWriter的机制是：写入每一行时，会把字典里的每个键去fieldnames里对照。fieldnames
        # 里有"Slogan"却没有"宣传语"，于是"宣传语"成了「多出来的、无法放进表头的字段」
        writer = csv.DictWriter(csvfile, fieldnames=["电影名", "年份", "上映时间", "类型", "时长", "评分", "语言", "导演", "作者", "宣传语", "简介"])
        writer.writeheader() # 写入表头
        writer.writerows(all_movies)



# 获取电影详情
def get_movie_info(movie_info_url):
    # 1. 发送请求, 获取电影详情数据
    movie_response = requests.get(movie_info_url, timeout = 60)
    print(f"正在爬取电影详情：{movie_info_url}")

    # 2. 解析数据, 获取电影详情
    movie_doc = html.fromstring(movie_response.text)

    # 电影名称
    movies_name = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/a/text()")
    # 电影年份
    movies_years = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/h2/span[1]/text()")
    # 电影上映时间
    movies_dates = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[2]/text()")
    # 电影类型
    movies_tags = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[3]/a/text()")
    # 电影时长
    movies_cost_time = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[1]/div/span[4]/text()")
    # 电影评分
    movies_scores = movie_doc.xpath("//*[@id='consensus_pill']/div/div[1]/div/div/@data-percent")
    # 电影语言
    movies_languages = movie_doc.xpath("//*[@id='media_v4']/div/div/div[2]/div/section/div[1]/div/section[1]/p[3]/text()")
    # 电影导演
    movies_directors = movie_doc.xpath("//*[@id='featured_crew']/li[1]/p[1]/a/text()")
    # 作者
    movies_actors = movie_doc.xpath("//*[@id='featured_crew']/li[2]/p[1]/a/text()")
    # 电影宣传语
    movies_slogans = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/h3[1]/text()")
    # 电影简介
    movies_descriptions = movie_doc.xpath("//*[@id='original_header']/div[2]/section/div[3]/div[1]/p/text()")

    # xpath 返回永远是列表：
    # 匹配到内容：["肖申克的救赎"]
    # 没匹配到：[]
    # .strip() 是字符串 str 对象的方法
    # movies_name 是 xpath(...) 返回的列表
    # movies_name[0] 取出列表里第一个字符串；再.strip()
    # 如果直接写 movies_name.strip() -->  列表没有 .strip() 方法，直接报错。
    # 如果写 movies_name[0].strip()，没有 if 判断，一旦 XPath 没抓到内容，程序直接终止

    # 3. 返回电影详情 --> 字典
    movie_info = {
        "电影名": movies_name[0].strip() if movies_name else '',
        "年份": movies_years[0].strip() if movies_years else '',
        "上映时间": movies_dates[0].strip() if movies_dates else '',
        # ",".join 用逗号连接多个元素, 这里是把整个列表全部拼接成一个字符串，不是拿其中某一项，所以不需要索引
        "类型": ",".join(movies_tags) if movies_tags else '',
        "时长": movies_cost_time[0].strip() if movies_cost_time else '',
        "评分": movies_scores[0].strip() if movies_scores else '',
        "语言": movies_languages[0].strip() if movies_languages else '',
        "导演": ",".join(movies_directors) if movies_directors else '',
        "作者": ",".join(movies_actors) if movies_actors else '',
        "宣传语": movies_slogans[0].strip() if movies_slogans else '',
        "简介": movies_descriptions[0].strip() if movies_descriptions else ''
    }

    return movie_info

# 主函数, 定义核心逻辑
def main():
    all_movies = [] # 定义一个空列表, 用于保存所有电影数据
    for page_num in range(1, 6):
        if page_num == 1:
            # 1. 发送请求, 获取高分电影榜单
            # timeout = 60 --> 表示请求超时时间为60秒
            response = requests.get(TMDB_TOP_URL_1, timeout=60)
        else:
            response = requests.post(TMDB_TOP_URL_2,
                                     f"air_date.gte = & air_date.lte = & certification = & certification_country = CN & debug = & first_air_date.gte = & first_air_date.lte = & include_adult = false & include_softcore = false & latest_ceremony.gte = & latest_ceremony.lte = & page = {page_num} & primary_release_date.gte = & primary_release_date.lte = & region = & release_date.gte = & release_date.lte = 2027 - 05 - 22 & show_me = everything & sort_by = vote_average.desc & vote_average.gte = 0 & vote_average.lte = 10 & vote_count.gte = 300 & vote_count.lte = & watch_region = CN & with_genres = & with_keywords = & with_networks = & with_origin_country = & with_original_language = & with_watch_monetization_types = & with_watch_providers = & with_release_type = & with_runtime.gte = 0 & with_runtime.lte = 400 & view = & discover_preset = top - rated",
                                     timeout=60)
        print(f"发送请求, 访问第 {page_num} 页, 获取高分电影榜单数据...")

        # 2. 解析数据, 获取电影信息
        document = html.fromstring(response.text)
        movies_list = document.xpath("//*[@id]/div[@class='flex flex-wrap content-start items-start']")

        # 遍历电影列表, 获取电影详情
        # all_movies = [] # 局部变量, save_all_movies(all_movies), 作用不到, 无法保存数据
        for movie in movies_list:
            movie_urls = movie.xpath("./div/a/@href")
            if movie_urls:
                # 电影详情URL
                movie_info_url = TMDB_BASE_URL + movie_urls[0]
                # 调用函数get_movie_info()获取电影详情
                movie_info = get_movie_info(movie_info_url)
                all_movies.append(movie_info)

    # 4.保存数据, 保存为 csv 文件
    print("保存所有电影数据, 保存到CSV文件中...")
    save_all_movies(all_movies)

if __name__ == '__main__':
    main()



