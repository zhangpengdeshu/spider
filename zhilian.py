import requests
from bs4 import BeautifulSoup
import time
import os
import xlwt

def get_page(url,params,headers):
    try:
        resp = requests.get(url,params=params,headers=headers)
        resp.encoding = 'utf-8'
        return resp.text
    except:
        return None

def parse_page(html):
    soup = BeautifulSoup(html,'html.parser')
    items = soup.find_all('table','newlist')
    for item in items:
        if item.find('b') is not None:
            yield {
                "job": item.find('b').get_text(),
                "companyName": item.find('td','gsmc').find('a').get_text(),
                'companyAddress': item.find('td','gzdd').get_text(),
                'salary':item.find('td','zwyx').get_text()
            }

def save_to_execle(content):
    pass

def main(url,params,headers):
    path = 'D:\\work'
    os.chdir(path)
    #创建工作簿
    book = xlwt.Workbook(encoding='utf-8')
    #创建sheet
    sheet = book.add_sheet('sheet', cell_overwrite_ok=True)
    sheet.write(0,0,'job')
    sheet.write(0,1,'companyName')
    sheet.write(0,2,'companyAddress')
    sheet.write(0,3,'salary')
    val1 = 1
    val2 = 1
    val3 = 1
    val4 = 1
    data = []
    for item in parse_page( get_page(url,params,headers) ):
        print(item)
        for key,value in item.items():
            if key == 'job':
                sheet.write(val1,0,value)
                val1 += 1

            elif key == 'companyName':
                sheet.write(val2,1,value)
                val2 += 1

            elif key == 'companyAddress':
                sheet.write(val3,2,value)
                val3 += 1
            elif key == 'salary':
                sheet.write(val4,3,value)
                val4 += 1
    #保存
    book.save('d:\\data-analysis.xls')



if __name__ == "__main__":
    url = 'http://sou.zhaopin.com/jobs/searchresult.ashx'
    headers = {
        "Connection": "keep-alive",
        "Host": "sou.zhaopin.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"
    }

    payload = {
        'jl':'北京',
        'kw':'数据分析',
        'sm':0,
        'isadv':0,
        'sg':'2e17cb71147245f5836b075a6b3d18fa',
        'p':1
    }

    for p in range(1,100):
        payload['p'] = p
        main(url,payload,headers)
        time.sleep(1)
