#先引入后面分析、可视化等可能用到的库
import tushare as ts
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#设置token
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
#ts.set_token(token)
pro = ts.pro_api(token)
# #获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
# basic=pro.stock_basic(list_status='L')
# #定义获取多只股票函数：
# def get_stocks_data(stocklist,start,end):
#     all_data={}
#     for code in stocklist:
#         all_data[code]=pro.daily(ts_code=code,
#                  start_date=start, end_date=end)
#     return all_data
#
# #保存本地
# def save_data(all_data):
#     for code,data in all_data.items():
#         data.to_csv(code+'.csv',
#                      header=True, index=False)
#
# stocklist=list(basic.ts_code)[:15]
# start=''
# end=''
# all_data=get_stocks_data(stocklist,start,end)
#
# all_data['000002.SZ'].tail()
#
# #将数据保存到本地
# save_data(all_data)

#读取本地文件夹里所有文件
import os
#文件存储路径
file=os.getcwd()+'\data\\'
g=os.walk(file)
filenames=[]
for path,d,filelist in g:
    for filename in filelist:
        filenames.append(os.path.join(filename))
print(filenames)

#将读取的数据文件放入一个字典中
df={}
#从文件名中分离出股票代码
code=[name.split('.')[0] for name in filenames]
for i in range(len(filenames)):
    filename=file+filenames[i]
    df[code[i]]=pd.read_csv(filename)

#查看第一只股票前五行数据
print(df[code[0]].head())

#
# #获取常见股票指数行情
# indexs={'上证综指': '000001.SH','深证成指': '399001.SZ',
#          '沪深300': '000300.SH','创业板指': '399006.SZ',
#           '上证50': '000016.SH', '中证500': '000905.SH',
#          '中小板指': '399005.SZ','上证180': '000010.SH'}
index_data = {}
for i in range(len(filenames)):
    dft = df[code[i]]
    dft.index = pd.to_datetime(dft.trade_date)
    index_data[code[i]] = dft.sort_index()

#对股价走势进行可视化分析
subjects =list(index_data.keys())
#每个子图的title
plot_pos = [421,422,423,424,425,426,427,428]
# 每个子图的位置
new_colors = ['#1f77b4','#ff7f0e', '#2ca02c',
'#d62728','#9467bd','#8c564b', '#e377c2',
'#7f7f7f','#bcbd22','#17becf']

fig = plt.figure(figsize=(16,18))
fig.suptitle('多股股指走势',fontsize=18)
for pos in np.arange(len(plot_pos)):
    ax = fig.add_subplot(plot_pos[pos])
    y_data =index_data[subjects[pos]]['close']
    b = ax.plot(y_data,color=new_colors[pos])
    ax.set_title(subjects[pos])
    # 将右上边的两条边颜色设置为空，相当于抹掉这两条边
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
plt.show()
