#!/usr/bin/env python
# coding=utf-8
import itertools
import re
import urllib2
from bs4 import BeautifulSoup
import sys
import lxml.html
import time

reload(sys)
sys.setdefaultencoding("utf-8")
def download(url,user_agent='Android',proxy=None,num_retries=1):
    headers={'User-agent':user_agent}
    request=urllib2.Request(url,headers=headers)
    opener=urllib2.build_opener()
    try:
        html=opener.open(request).read()
    except urllib2.URLError as e:
        print 'error ',e.reason
        html=None
    return html

def findChs(pattern,html):
    try:
        return str(re.findall(pattern,html)[0]).decode('string_escape')
    except IndexError:
        return None

def getContentFromHtmlByBS(html):
    soup=BeautifulSoup(html,'html.parser')
    return soup.select(".article-content")[0].get_text()

def getContentFromHtmlByLxml(html):
    tree=lxml.html.fromstring(html)
    return tree.find_class('article-content')[0].text_content()

print '开始'
titleFile=open('luo.txt','w')
count=0
for page in itertools.count(720):
    if page<1500:
        url='http://www.luofans.com/blogs/%d'%page
        html=download(url)
        if html==None:
            print 'html is none'
            break
        title=findChs('<title>(.*?)</title>',html).replace('文字版_罗辑思维视频文字版更新_罗友之家','').strip()
        if title.startswith('No'):
            start=time.time()
            content=getContentFromHtmlByLxml(html)
            print 'time consumed:',time.time()-start
            if content==None:
                print 'content is none'
            else:
                print content[50:100]
                contentFile=open(title+'.txt','w')
                contentFile.write(content)
                contentFile.close()
                count+=1
                print title
                titleFile.write('\n')
                titleFile.write(title)
                titleFile.write('\n')
                titleFile.write(url)
    else:
        break
print 'count is ',count
titleFile.close()
