from urllib import request
import ssl

if __name__ == '__main__':
    ssl._create_default_https_context = ssl._create_unverified_context
    durl = 'http://fanyi.baidu.com'
    res = request.urlopen(durl)
    html = res.read().decode('utf8')
    print(html)
