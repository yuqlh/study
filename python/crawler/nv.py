from bs4 import BeautifulSoup
import requests

def run():
    """
    爬取沧元图第一章内容
    """
    server = 'https://www.biqukan.com/'
    target = server + '38_38836/'
    req = requests.get(url = target)
    html = req.content.decode('gbk')

    bf = BeautifulSoup(html)

    div = bf.find_all('div', class_='listmain')
    a_bf = BeautifulSoup(str(div[0]))
    a = a_bf.find_all('a')
    for tmp in a:
        s = tmp.string + server+tmp.get('href')
        print(s)

    #t0 = texts[0].text.replace('\xa0'*8, '\n\n')


if __name__ == '__main__':
    run()


