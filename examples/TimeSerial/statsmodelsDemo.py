import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#获取数据，从tushare上获取沪深300指数为例
import tushare as ts
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)

def get_data(code,n=250*3):
    df=pro.index_daily(ts_code=code)
    #将日期设置为索引
    df.index=pd.to_datetime(df.trade_date)
    #最近n日价格走势
    df=df.sort_index()[-n:]

    return df.close
df=get_data('000300.SH')

import statsmodels.tsa.api as smt
#tsa是Time Series analysis缩写
#tsa的stattools（统计工具）提供了计算acf和pacf以及后面要用到的adfuller单位根检验函数
#使用help(smt.stattools.acf)可以查看相关参数设置
#计算自相关系数，这里设置滞后项为5期,默认是40期滞后
acf=smt.stattools.acf(df,nlags=5)
#计算偏自相关系数
pacf=smt.stattools.pacf(df,nlags=5)
print(f'自相关系数为：{acf};\n'
      f'：{pacf}')

def acf_pacf_plot(data, lags=None):
    #判断是否为pandas的Series格式数据
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    #设定画面风格，这里设置为'bmh', colspan=2
    with plt.style.context('bmh'):
        fig = plt.figure(figsize=(10, 8))
        #设置子图
        layout = (3,1)
        ts_ax = plt.subplot2grid(layout, (0, 0))
        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (2, 0))
        data.plot(ax=ts_ax)
        ts_ax.set_title('时间序列图')
        smt.graphics.plot_acf(data, lags=lags, ax=acf_ax, alpha=0.5)
        acf_ax.set_title('自相关系数')
        smt.graphics.plot_pacf(data, lags=lags, ax=pacf_ax, alpha=0.5)
        pacf_ax.set_title('偏自相关系数')
        plt.tight_layout()
        plt.show()
    return

#设置20阶滞后期
acf_pacf_plot(df,lags=20)