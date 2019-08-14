# -*- coding:utf-8 -*-
import requests,time,codecs
from jg import *
import sys
sys.path.append('d:/yq/patents/')
import socket
socket.setdefaulttimeout(15)
localDir = 'd:/yq/patents/'
Number = xl2lst('d:/yq/patents/上市公司专利个数统计.xlsx',4)[1:]
r = []
e = []
for i in range(1168,2780):
    if int(Number[i])>0:
        time.sleep(10)
        jc = jcs[i]
        print("\n\n 开始下载:  " + codes[i] + ': ' + str(i) + jc + "\n\n")
        pageNumber = int(int(Number[i])/10) + 1
        if pageNumber > 1000:
            pageNumber =1000
        for p in range(1, pageNumber + 1):
            time.sleep(2)
            print("还剩下" + str(pageNumber - p) + '页。')
            try:
                url = 'http://so.baiten.cn/results?q=' + qcs[i] + '&page=' + str(p)
                response = requests.get(url)
                response.encoding = 'utf-8'
                c = response.text.replace('\r\n','')
                h = c.split('<span class="mlr256" name="')[1:]
                for x in h:
                    cls = x.split('[')[1].split(']')[0]
                    ttl = x.split('data-al-ti="')[1].split('"')[0]
                    pn = x.split('主分类号')[1].split('" >')[1].split('<')[0]
                    ndx = x.split('data-index="')[1].split('"')[0]
                    hrf = x.split('/detail')[1].split('"')[0]
                    stt = x.split('lawState')[1].split('>')[1].split('<')[0]
                    tm = x.split('Search/GoToSearch?sq=ad:("')[1].split('"')[0]
                    smr = x.split('data-summary="')[1].split('"')[0]
                    r.append([codes[i],jcs[i],cls,ttl,pn,ndx,hrf,stt,tm,smr])
            except Exception as ex:
                e.append([i,p,ex])
                lst2xl(e,localDir + 'eror.xlsx', 1)
                #print(e)
            if p % 200 == 0:
                print('写Excel文件。')
                lst2xl(r,localDir + str(i) + '_' + codes[i] + '_' + str(pageNumber+1) + '_of_' + str(p)+ '.xlsx',1)
                time.sleep(5)
        lst2xl(r,localDir + codes[i] + '.xlsx', 1)
        r = []
        
