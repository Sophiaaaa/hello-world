# coding:utf-8
import requests
import time
from lxml import etree

f_1 = open('level_3.txt', 'w')
with open('level_2.txt', 'r') as f:
    for item in f.readlines():
        link = item.strip('\n').split('\t')
        if link[0] != ' ':
            user_page = link[0]
            field = requests.get(user_page)
            html = etree.HTML(field.text)
            try:
                age = html.xpath('//div[@class="userinfo_userdata"]/span[2]/text()')[0]
            except:
                age = ' '
            try:
                posts = html.xpath('//div[@class="userinfo_userdata"]/span[4]/text()')[0]
            except:
                posts = ' '
        else:
            age, posts = '', ''
        # 作为抓取提示标识
        print age
        f_1.write(age.encode('utf-8') + '\t' + posts.encode('utf-8'))
        f_1.write('\n')
        time.sleep(1)
f_1.close( )
