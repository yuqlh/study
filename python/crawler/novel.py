# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import requests, sys

class downloader(object):

    def __init__(self):
        self.server = 'https://www.biqukan.com/'
        self.target = self.server + '38_38836/'
        self.names = []            #存放章节名
        self.urls = []            #存放章节链接
        self.nums = 0            #章节数
        self.f = open('沧元图.txt', 'a', encoding='utf8')

    def get_download_url(self):
        req = requests.get(url = self.target)
        html = req.content.decode('gbk', 'ignore')

        div_bf = BeautifulSoup(html, 'lxml')
        div = div_bf.find_all('div', class_ = 'listmain')
        a_bf = BeautifulSoup(str(div[0]), 'lxml')
        a = a_bf.find_all('a')
        a = a[12:]
        self.nums = len(a)                                #剔除不必要的章节，并统计章节数
        for each in a:
            self.names.append(each.string)
            self.urls.append(self.server + each.get('href'))

    def get_contents(self, target):
        req = requests.get(url = target)
        html = req.content.decode('gbk', 'ignore')
        bf = BeautifulSoup(html, 'lxml')
        texts = bf.find_all('div', class_ = 'showtxt')
        texts = texts[0].text.replace('\xa0'*8,'\n\n')
        return texts

    def writer(self, name, text):
        self.f.write(name + '\n')
        self.f.writelines(text)
        self.f.write('\n\n')

    def close(self):
        self.f.close()

if __name__ == "__main__":
    dl = downloader()
    dl.get_download_url()
    print('《沧元图》开始下载：')
    for i in range(dl.nums):
    #for i in range(1):
        dl.writer(dl.names[i], dl.get_contents(dl.urls[i]))
        sys.stdout.write("  (%d of %d) 已下载:%.3f%%" % (i, dl.nums, float(i*100.0/dl.nums)) + '\r')
        sys.stdout.flush()
    dl.close()
    print('《沧元图》下载完成')