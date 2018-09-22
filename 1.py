import requests
import re

def getHtmlContent(url):
    page = requests.get(url)
    return page.text

def getJPGs(html):
    jpgReg = re.compile(r'<img.+?src="(.+?\.jpg)" width')
    jpgs = re.findall(jpgReg,html)
    return jpgs

def downloadJPG(imgUrl,fileName):
    from contextlib import closing
    with closing(requests.get(imgUrl,stream = True)) as resp:
        with open(fileName,'wb') as f:
            for chunk in resp.iter_content(128):
                f.write(chunk)

def batchDownloadJPGs(imgUrls, path = 'D:/Temp/'):
    count = 1
    for url in imgUrls:
        downloadJPG(url, ''.join([path, '{0}.jpg'.format(count)]))
        print('下载中...请稍后...{0}.jpg'.format(count))
        count = count + 1

def download(url):
    html = getHtmlContent(url)
    jpgs = getJPGs(html)
    batchDownloadJPGs(jpgs)

def main():
    url = 'http://image.baidu.com/search/index?tn=baiduimage&ct=201326592&lm=-1&cl=2&ie=gb18030&word=%CD%BC%C6%AC&fr=ala&ala=1&alatpl=others&pos=0'
    download(url)
    print('=======================================')
    print("已完成下载...请到指定目录进行查看！！！")

if __name__ == '__main__':
    main()
    
