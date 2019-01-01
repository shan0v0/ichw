#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Shanye"
__pkuid__  = "1800011804"
__email__  = "1800011804@pku.edu.cn"
"""

import sys,string
from collections import Counter
from urllib.request import urlopen

ans = []

def wcount(lines,topn):
    '''对一段文本进行单词出现频数统计并从高到低进行排序，返回值为单词出现频数最高的前n（或全部）名的单词及出现次数信息（列表形式）'''
    newlines = ""
    for i in lines:#遍历文本中每个字符
        if i not in string.punctuation:#删去标点符号：将非标点符号的字符提取到新的文本中
            newlines = newlines + i
    newlines = newlines.lower()#将除去标点符号的新字符串中的大写字母全部变为小写字母，便于统计同一单词数目
    wordslist = newlines.split()#利用空格和空行等间隔，提取出所有的单词，建立单词列表
    
    wordsdict = Counter(wordslist)#对列表中单词进行计数，得出key为单词，value为单词频数的单词词典
    
    sorted_list = sorted(wordsdict.items(),key = lambda item:item[1],reverse = True)#将单词词典按value（频数）由高到低进行排序

    outputnumber = min(topn,len(sorted_list))#比较单词总数与用户想要了解的前n个单词的数目，如果n小，输出前n个；如果n大，输出全部单词词典
    
    for j in range(outputnumber):
        ans.append(sorted_list[j])
    
    return ans


if __name__ == '__main__':
    if  len(sys.argv) == 1:#如果用户输入了1一个参数，既输入了wcount.py，输出该程序功能和输入的注意事项的介绍
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    if 1 < len(sys.argv) < 4:#如果用户输入了2、3一个参数，既输入了wcount.py、文章链接、想了解的单词频率排名的前几名（如未输入，则给出前10），执行程序功能
        #将网页上的txt文本转化为本程序可操作的字符串
        doc = urlopen(sys.argv[1])
        docstr = doc.read()
        doc.close()
        lines = docstr.decode('utf-8')
        
        if len(sys.argv) == 2:#如果输入2个参数，既wcount.py、文章链接，则给出前10名
            topn = 10
        else:#输入3个参数，既wcount.py、文章链接、想了解的单词频率排名的前几名
            topn = int(sys.argv[2])
        
        ans = wcount(lines,topn)#得到结果（列表）
        
        for it in ans:#将列表结果中每一项（每个单词及其频数）换行制表显示
            print(it[0]+'\t'+str(it[1]))
        
    if len(sys.argv)>=4:#如果输入参数超过3个，则报错显示输入不符合改程序要求，请求重新输入。
        print('This input does not meet the requirements. Please input again.')
        sys.exit(1)

