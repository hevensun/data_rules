#!/usr/bin/python
#-*- coding: utf-8 -*-
"""
根据给定的字符串，生成部分匹配列表
"""
#
#
import sys
from  datetime import  *
from  time     import *
import pymongo
from pymongo   import MongoClient

    
def read_file(file):
    """read input file to list"""
    file_object = open(file, "r")
    try:
        all_lines = file_object.readlines( )
    finally:
        file_object.close( )
    return all_lines

def index_to_db(key_index_list, collection):
    """key/val to db"""
    table_list  =  []

    systime     = str(datetime.now()).split(".")[0]
    for item in key_index_list:

        #get val's list
        resVal = set([])
        res = collection.find({"host":item[0], "rule":item[1]})
        if res.count() == 1:
            collection.delete_many({"host":item[0], "rule":item[1]})

        one_row = {}
        one_row["host"] = item[0]
        one_row["rule"] = item[1]
        one_row["uptime"] = systime
        one_row["action"] = "search"
        table_list.append(one_row)


    # update stored index
    collection.insert_many(table_list)
    collection.create_index([("host", pymongo.DESCENDING), ("rule",pymongo.DESCENDING)], background=True)


def main_process(file_list, collection):
    """main process"""
    key_index_list = []

    # read file to list
    for file in file_list:
        keywords = read_file(file)

        # process keywords
        for kw in keywords:
            kw = kw.strip()
            key_index_list.append(kw.split("\t"))


    # store key_index_dict to MongoDB
    print "will update:",len(key_index_list)
    index_to_db(key_index_list, collection)


if __name__ == '__main__':

    try:
        conn  = MongoClient('192.168.34.94', 27017)
        collection = conn.dataManagePlatform.data_rules
        main_process(sys.argv[1:], collection)
    except Exception,e:
        print str(e)


