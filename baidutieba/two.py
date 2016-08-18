# coding:utf-8
import re
import requests
from lxml import etree

f = open('xiankaba_June.txt', 'r')
level_2 = open('level_2.txt', 'w')
url = 'http://tieba.baidu.com'
user_page, content, time_, rank = ' ', ' ', ' ', ' '
for line in f.readlines():
    lst = line.strip('\n').split('\t')
    if len(lst) > 2:
        link = lst[2]
        if link != ' ':
            html = requests.get(link)
            selector = etree.HTML(html.text)
            field = selector.xpath('//div[@class="l_post j_l_post l_post_bright noborder "]')
            for each in field:
                user_page = url + \
                            each.xpath('div[@class="d_author"]/ul[@class="p_author"]/li[@class="d_name"]/a/@href')[0]
                # print user_page
                try:
                    content = each.xpath('div[@class="d_post_content_main d_post_content_firstfloor"]')[0].xpath(
                        'string(.)').strip().split('\n')[0]
                    # 作为抓取提示标识
                    print content
                except Exception, e:
                    content = ' '
                    print e
                time_ = re.findall("date&quot;:&quot;(.*?)&quot;", html.text, re.S)[0]
                # print time_
                rank = \
                    each.xpath(
                        'div[@class="d_author"]/ul[@class="p_author"]/li[@class="l_badge"]/div[@class="p_badge"]/a')[
                        0].xpath('string(.)')
                # print rank
    else:
        user_page, content, time_, rank = ' ', ' ', ' ', ' '
    level_2.write(
        user_page.encode('utf-8') + '\t' + content.encode('utf-8') + '\t' + time_.encode('utf-8') + '\t' + rank.encode(
            'utf-8'))
    level_2.write('\n')
level_2.close()
