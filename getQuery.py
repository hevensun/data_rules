#!/usr/bin/env python
# -*- coding: UTF-8 -*-
import sys  
import time
from urlparse import urlparse

reload(sys)
sys.setdefaultencoding("utf-8")

keyList = ["key","keyword","keyword","kw","k",\
        "q","query","search","wd","word"]

def is_cn_str(str):
    str = str.decode('utf-8')
    for i in range(0, len(str)):
        if 0x4e00<=ord(str[i])<0x9fa6:
            return True
    return False

def get_chinese_segment(query, hostname, url):
    segsArr = query.split("&")
    for i in range(0, len(segsArr)):
        (k,v) = segsArr[i].split("=")
        if (k in keyList) and (is_cn_str(v)):
            (path,param) = url.split("?")
            print hostname, k, v, path, url
            #print '%s%s\t%s' % (hostname,k,1)  

def get_query(url):
    # get query pattern 
    try:  
        parseRes = urlparse(url)
        hostname = parseRes.hostname
        query    = parseRes.query
        get_chinese_segment(query, hostname, url)


    except Exception, tx:  
        pass

  

if __name__ == '__main__':  
 
    for line in sys.stdin:
        line = line.strip()
        if len(line)!=0:
            lines = line.split("|")
            get_query(lines[18])
            get_query(lines[-7])
