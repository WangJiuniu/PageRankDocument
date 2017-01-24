# coding=utf-8
import heapq
import pickle


resFile = '../inlinks_int_res_2'
docIDtoIntIdFile = '../docIDtoIntId.pkl'
urlFile = '../docid_to_url'
lastFile = '../finalDocidURL_2.txt'
TOPN = 100

# resFile = 'rankRes.txt'
# wordListFile = 'wordListLocal.pkl'
# urlFile = 'url.txt'
# lastFile = 'finalDocidURL.txt'
# TOPN = 5



#读取pagerank结果，并将其用堆排序取出前100(Top100)
print('正在排序取出TOPN')
objFile = open(resFile,'r')
flag = 0
pageDict = []
for line in objFile:
    #print line
    word = line.split('=')
    dict = {'intName':int(word[0]),'rankVaule':float(word[1])}
    pageDict.append(dict)
print('len(pageDict):',len(pageDict))
Top100 = heapq.nlargest(TOPN, pageDict, key=lambda s: s['rankVaule'])

#读取wordList，并构造 IntId->docid字典
print('正在构造 IntId->docid字典')
pkl_file = open(docIDtoIntIdFile, 'rb')
wordList = pickle.load(pkl_file)
pkl_file.close()
IntWordList = {}
for key,value in wordList.iteritems():
    IntWordList[value] = key
# IntWordList =((value,key) for key,value in wordList.iteritems())

#读取url文件，构造docid->url字典
print('正在构造 docid->url字典')
objURL = open(urlFile,'r')
docidURL ={}
for line in objURL:
    word = line.split()
    docidURL[word[0]] = word[1]
print('len(docidURL):',len(docidURL))
#在Top100中，加入 docid和url字段并保存
print('正在组装docid和URL')
aimWords = ''
for iterm in Top100:
    print iterm
    iterm['docid'] = IntWordList[iterm['intName']]
    iterm['url'] = docidURL[iterm['docid']]
    aimWords += iterm['docid'] +' '+ iterm['url']+'\r\n'
objFinal = open(lastFile,'w')
objFinal.write(aimWords)
objFinal.close()
print('程序运行结束')

