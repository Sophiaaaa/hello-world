# !/usr/bin/python
# LUO Chen
# Date: 2016_09_15

# coding: utf-8
# 首先在命令行中使用pip install requests, pip install beautifulsoup4安装好两个模块，安装完成后执行以下代码

import re
import time
import requests
from bs4 import BeautifulSoup

# 文件保存路径
f = open('comments.txt', 'a')
# 通过Chrome登录weibo.cn，使用'审查元素'——'Network'获取你的Cookie
Cookies = {'Cookie': '__Your Cookie__'}
# 粘贴你要抓取评论的微博链接，此处以人民日报的一条微博为例，链接最后要有'&page=*'
url = 'http://weibo.cn/comment/E8pHMn6wb?uid=2803301701&rl=0&page=1'
# 输入评论的总页数
pages = 10
for i in range(1, pages + 1):
    new_url = re.sub('&page=(\d+)', '&page=%s' % (str(i)), url)
    content = requests.get(new_url, cookies=Cookies)
    soup = BeautifulSoup(content.text)
    comment_info = soup.find_all('div', class_='c')[2: -1]
    for comments in comment_info:
        # 抓取用户名
        user_name = comments.text.split(':')[0].strip()
        # 抓取用户认证类型
        try:
            authen = comments.select('img')[0]['alt']
        except:
            authen = ' '
        # 抓取评论内容
        comment_field = comments.find_all('span', class_='ctt')
        try:
            comment = comment_field[0].text
        except:
            comment = ' '
        # 抓取点赞数量
        praise_field = comments.find_all('span', class_='cc')
        try:
            praise = praise_field[0].text
        except:
            praise = ' '
        # 抓取评论发布时间与客户端
        time_device_field = comments.find_all('span', class_='ct')
        try:
            time_device = time_device_field[0].text
        except:
            time_device = ' '
        print user_name, '\t', authen, '\t', comment, '\t', praise, '\t', time_device
        f.write(user_name.encode('utf-8') + '\t' + authen.encode('utf-8') + '\t' + comment.encode(
            'utf-8') + '\t' + praise.encode('utf-8') + '\t' + time_device.encode('utf-8'))
        f.write('\n')
    # 为了避免微博的爬虫监测机制，time.sleep(n)中的n表示每抓取一页暂停n秒，可以酌情调整
    time.sleep(2)
f.close()
