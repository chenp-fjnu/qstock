# -*- coding=utf-8 -*-
# #引入需要的包
import jieba
import jieba.analyse
import numpy as np
import codecs
import pandas as pd
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator

import matplotlib.pyplot as plt
#画图正常显示中文
from pylab import mpl
plt.rcParams['font.sans-serif'] = ['SimHei']
# 用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False

#读入《倚天屠龙记》文本内容
text=codecs.open('倚天屠龙记.txt',
                 'r', encoding='UTF-8').read()
tags=jieba.analyse.extract_tags(text,topK=100,
      withWeight=True)
tf=dict((a[0],a[1]) for a in tags)
print(tf)
#识别中文文本
#产生一个以(150,150)为圆心,半径为130的圆形mask
x,y = np.ogrid[:300,:300]
mask = (x-150) ** 2 + (y-150) ** 2 > 130 ** 2
mask = 255 * mask.astype(int)
wc=WordCloud(background_color="white",repeat=True,mask=mask)
wc=wc.generate_from_frequencies(tf)
plt.figure(num=None,figsize=(12,10),facecolor='w',edgecolor='k')
plt.imshow(wc,interpolation="bilinear")
plt.axis('off')
plt.show()
