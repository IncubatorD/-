# coding=utf-8              #默认使用UTF-8编码
import requests


headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)  \
    Chrome/70.0.3538.102 Safari/537.36'}
response = requests.get('http://www.taobao.com', headers=headers)
output = open('data.txt ', 'a+', encoding='utf-8')  # 以创建追加的方式打开download文本文件，编码格式为得到的格式
output.write('—>' + response.url + '\n\n' + response.text + '\n\n\n')  # 将URL与对应的HTML追加写入文件
output.close()

# print(rsp)  # 以文本形式打印网页源码
# print(response.status_code)  # 打印状态码
# print(response.url)  # 打印请求url
# print(response.headers)  # 打印头信息
# print(response.cookies)  # 打印cookie信息
