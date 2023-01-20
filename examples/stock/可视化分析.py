#先引入后面可能用到的包（package）
import pandas as pd
import numpy as np
from scipy import stats
import tushare as ts
import matplotlib.pyplot as plt

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
#调取股票基本面数据和行情数据
#基本面数据
#设置token
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
#ts.set_token(token)
pro = ts.pro_api(token)
basics_data=pro.stock_basic(list_status='L')

#定义一个画图函数
def plot_data(data,title):
    d=dict(basics_data)
    plt.figure(figsize=(8,5))
    fig=plt.bar(d.keys(), d.values())
    autolabel(fig)
    plt.title(title,fontsize=15)
    plt.ylim(0,max(d.values())*1.1)
    plt.show()
#查看十大最低市盈率行业
#这里行业划分不是很严谨，直接从数据库导出的
pe_ind=basics_data.groupby('industry')['pe'].mean()
pe=pe_ind.sort_values()[:10].round(2)
title='十大最低市盈率行业'
plot_data(pe,title)