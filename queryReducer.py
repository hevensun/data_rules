#!/usr/bin/env python  
# -*- coding: UTF-8 -*-
  
from operator import itemgetter  
import sys  
  
current_host = None  
host         = None  
current_list = [] 
change       = False
  
# input comes from STDIN  
for line in sys.stdin:  
    # remove leading and trailing whitespace  
    line = line.strip()  
    if len(line)==0:
        continue
  
    # parse the input we got from mapper.py  
    (host, query) = line.split("\t")  

  
    # this IF-switch only works because Hadoop sorts map output  
    # by key (here: word) before it is passed to the reducer  
    if current_host == host:  
        current_list.append(query)
    else:  
        if current_host:  
            # write result to STDOUT  
            queryList = ("|").join(set(current_list))
            print '%s\t%s' % (host, queryList)  
        change = True
        current_host = host  
        current_list = []
        current_list.append(query)
  
# do not forget to output the last word if needed!  
if (current_host == host) and (change==False):  
    #current_list.append(query)
    queryList = ("|").join(set(current_list))
    print '%s\t%s' % (host, queryList)  
