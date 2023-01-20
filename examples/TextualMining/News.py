#注意：黑色方框背景里的代码可以左右滑动查看
#引入需要用到的包
#金融量化分析常用到的有：pandas（数据结构）、
#numpy（数组）、matplotlib（可视化）、scipy（统计）
import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
import jieba
import jieba.analyse
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)
# df = pro.news(src='sina', start_date='2023-01-20 09:00:00', end_date='2023-01-20 20:00:00')
# df = pro.cctv_news(date='20230120')
df = pro.major_news(src='', start_date='2023-01-20 09:00:00', end_date='2023-01-20 20:00:00')

#获取当前即时财经新闻（如本文是2018年11月17日）
#默认是80条，可以通过参数“top= ”来设置
#保存数据到本地
# df.to_csv("news.csv",encoding='gbk')
# #加encoding='gbk'才不会中文乱码，如果存在“非法字符”,可能也会报错
# #数据清洗，保留需要的字段
# # df=df[['time','title','content']]
# #查看前三条数据
print(df.head())