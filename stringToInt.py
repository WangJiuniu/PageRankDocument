# -*- coding: utf-8 -*-
"""
Created on Fri Dec 16 21:48:33 2016

@author: Wang
"""
import pickle

fileSource = '../inlinks'
fileDist = '../inlinks_int_2'
urlFile = '../docid_to_url'
docIDtoIntIdFile = '../docIDtoIntId.pkl'
# fileSource = 'file7.txt'
# fileDist = 'file8.txt'
sentence = ''
aimWords = ''
wordList = {}


print('读取URL并建立docID->IntId字典')
count = 0
objURL = open(urlFile,'r')
docIDtoIntId ={}
for line in objURL:
    word = line.split()
    docIDtoIntId[word[0]] = count
    count +=1

print('正在读取文件并替换...')
print(' 正在读取文件...')
objSource = open(fileSource,'r')
sentence = objSource.readlines()#读取并替换文件内容
print(' 文件总行数：'+str(len(sentence)))
objSource.close()
print(' 正在进行替换...')


for ind,word in enumerate(sentence):
    if(not ind%50000):
        print str(ind),
    words = word.split()
    if words==[]:
	    break
    aimWords += str(docIDtoIntId[words[0]])+' '+str(docIDtoIntId[words[1]])+'\r\n' #生成新的文件内容

print('\n正在写入文件...')
objDist = open(fileDist,'w')
objDist.write(aimWords)
objDist.close()

print('正在保存字典...')
output = open(docIDtoIntIdFile, 'wb')
pickle.dump(docIDtoIntId, output)
output.close()
