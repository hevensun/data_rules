#!/bin/bash
input=/user/hive/warehouse/xdr_http_etl_decode/*
input=/user/hive/warehouse/xdr_http_etl_decode/003403_0
output=/user/admin/songgang/query/
hadoop dfs -rmr $output
JAR=/usr/lib/hadoop-mapreduce/hadoop-streaming.jar
hadoop jar $JAR \
-mapper  queryMapper.py    \
-file    queryMapper.py    \
-reducer queryReducer.py   \
-file    queryReducer.py   \
-input   $input            \
-output  $output           \
-jobconf mapred.reduce.tasks=3 
