【运行环境】
Python2.7

【文件结构说明】
1.stringToInt.py：将字符串链接关系映射为整型变量链接关系的程序
2.pageRank.py：pageRank算法函数
3.pagerank_test.py：调用pageRank.py，实现pagerank功能的程序
4.Top100rank.py：根据pageRank分值生成最终结果的程序
5.finalDocidURL.txt：最终结果文件（分值由高到低排列，两列内容为docid和对应URL）

【使用方法】
1.使用stringToInt.py，读取链接关系文件inlinks，将字符串表示的链接关系映射成为整型变量表示的链接关系，保存成文件inlinks_int（将映射关系保存在docIDtoIntId.pkl中）。
2.使用pagerank_test.py，读取整型变量表示的链接关系，使用pagerank算法计算每一个Intdocid（整型文档ID）对应的分值，保存成文件inlinks_int_res。
3.使用Top100rank.py，读取文件inlinks_int_res，使用堆排序的方法找出分值最高的前100个Intdocid（整型文档ID）。根据前面保存的映射关系docIDtoIntId.pkl，以及包含URL信息的文件docid_to_url，将选出的100个Intdocid（整型文档ID）映射回docid和对应URL，并保存为finalDocidURL.txt。
注：程序中的文件名变量需要与本地环境相适应。

【实验结果】
保存在finalDocidURL.txt文档中
