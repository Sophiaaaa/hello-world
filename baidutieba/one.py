# coding:utf-8
import requests
from lxml import etree

url = 'http://tieba.baidu.com/f?kw=%E6%98%BE%E5%8D%A1&ie=utf-8&pn='
lst = []
url_1 = 'http://tieba.baidu.com'
page = int(raw_input(u'输入50的倍数：'))
for i in range(105900, page, 50):
    lst.append(url + str(i))
with open('level_1.txt', 'a') as f:
    for item in lst:
        link, time = ' ', ' '
        print u'正在抓取...' + str(item)
        html_1 = requests.get(item)
        selector_1 = etree.HTML(html_1.text)
        field = selector_1.xpath('//div[@class="t_con cleafix"]')
        for each in field:
            title = each.xpath('div[@class="col2_right j_threadlist_li_right "]/div')[0].xpath('string(.)').strip().split('\n')[0].strip()
            reply_num = each.xpath('div[@class="col2_left j_threadlist_li_left"]/span/text()')[0]
            author = each.xpath('div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_author pull_right"]/span/@title')[0].split(':')[1]
            try:
                time = each.xpath('div[@class="col2_right j_threadlist_li_right "]/div')[0].xpath('string(.)').strip().split('\n')[3].strip('\n')
            except Exception, e:
                print e
                time = ' '
            if len(each.xpath('div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@href')) != 0:
                link = url_1 + each.xpath('div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit "]/a/@href')[0]
            elif len(each.xpath('div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit  member_thread_title_frs "]/a/@href')) != 0:
                link = url_1 + each.xpath('div[@class="col2_right j_threadlist_li_right "]/div[@class="threadlist_lz clearfix"]/div[@class="threadlist_title pull_left j_th_tit  member_thread_title_frs "]/a/@href')[0]
            f.write(title.encode('utf-8') + '\t' + str(reply_num) + '\t' + str(link) + '\t' + author.encode('utf-8') + '\t' + time.encode('utf-8'))
            f.write('\n')
            # 作为抓取提示标识
            print time, title