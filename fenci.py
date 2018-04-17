import jieba
import logging
f_c='/home/xumeng/DataSet/wikiData/wiki.zh.text'
f_s = '/home/xumeng/DataSet/wikiData/wiki.zh.text.seg'
f_c = open(file_cut,'r')
f_s = open(file_save,'w+')
for line in f_c.readlines():
    words = jieba.cut(line)
    words = ' '.join(words)
    words = list(words)
    for w in words:
        f_s.writelines(w)
f_c.close()
f_s.close()
