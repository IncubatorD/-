# coding=utf-8              #默认使用UTF-8编码
import requests
from urllib.error import URLError, HTTPError, ContentTooShortError  # 导入库urllib.error中的错误类型模块

do = 3  # 设置同一网址请求次数上限
reset = do
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  \
    Chrome/70.0.3538.102 Safari/537.36'}  # 设置伪装UA，默认为Chrome7，另：' \'为语句换行连接符
while True:
    base_url = input('>请输入目标网址：')  # 输入目标URL
    print('>正在爬取......')
    while do != 0:
        try:
            url = requests.get(base_url, headers=headers)  # 爬取准备：以设置的UA进行伪装URL# 1.利用request模块中的urlopen方法打开目标URL 2.利用read方法读取URL中的内容，初始数据为十六进制编码(0x)
            html = requests.urlopen(url).read()
            break
        except (URLError, HTTPError, ContentTooShortError) as e:  # 若下载发生错误则将错误类型模块导入命名为e
            print('>爬取失败:', e.code, e.reason)  # 提示错误代码以及错误原因
            html = None
            do -= 1
    if do == 0:  # 若剩余尝试次数为0，则重置次数，并重新输入网址
        do = reset
        continue
    dic = detect(html)  # 利用detect方法获取初始数据的格式字典
    encode = dic.get('encoding ', 'utf-8')  # 利用get方法查询格式字典中的编码格式，若无法查询则默认返回UTF-8格式
    html = html.decode(encode)  # 利用decod方法以得到的编码格式进行解码，并将初始数据(0x)覆盖
    output = open('download.txt ', 'a+', encoding=encode)  # 以创建追加的方式打开download文本文件，编码格式为得到的格式
    output.write('—>' + base_url + '\n\n' + html + '\n\n\n')  # 将URL与对应的HTML追加写入文件
    output.close()
    print('>爬取成功！')
    i = input('>继续或结束Y/N：')
    if i == 'N' or 'n':  # 输入Y则继续，N则结束
        break
print('>爬取结束')
print('>数据见文本文件。')

'''
# coding=utf-8
import urllib.request
from urllib.error import URLError,HTTPError,ContentTooShortError
def download(url,user_agent='wswp',num_rettirs=2):
    print('Downloading:',url)
    request=urllib.request.Request(url)
    request.add_header('User-agent',user_agent)
    try:
        html=urllib.request.urlopen(url).read()
    except (URLError,HTTPError,ContentTooShortError) as e:
        print('Download error:',e.reason)
        html=None
        if num_rettirs>0:
            if hasattr(e,'code') and 500 <=e.code<600:
                return download(url,num_rettirs-1)
        return html
c=download('https://http://www.runoob.com/')
print(c)
'''
