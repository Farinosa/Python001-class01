# 使用BeautifulSoup解析网页

import requests
from bs4 import BeautifulSoup as bs
import pandas as pd
# bs4是第三方库需要使用pip命令安装


user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'

header = {'user-agent':user_agent}

myurl = 'https://maoyan.com/films?showType=3'

response = requests.get(myurl,headers=header)

# print(response.text)

bs_info = bs(response.text, 'html.parser')

index = 0
mylist = []
# Python 中使用 for in 形式的循环,Python使用缩进来做语句块分隔
for infos in bs_info.find_all('div', attrs={'class': 'movie-hover-info'}):
    
    # print(titles.get('class'))
    for titles in infos.find_all('div', attrs={'class': 'movie-hover-title'}):
        # print(titles.get('href'))
        # 获取所有链接
        s1 = titles.text.replace('\n', '').replace('\r', '').replace(' ', '')
        print(s1)
        mylist.append(s1)
        # 获取电影名字
        # print(infos.find('div', attrs={'class': 'movie-hover-title movie-hover-brief'}).text.replace('\n', '').replace('\r', '').replace(' ', ''))
    mylist.append("————————————————————")
    print('\n' + str(index))
    
    index += 1
    if index > 10:
        movie1 = pd.DataFrame(data = mylist)

        # windows需要使用gbk字符集
        movie1.to_csv('./movie1.csv', encoding='utf-8', index=False, header=False)
        break
        #return



# mylist = [film_name, plan_date, rating]


