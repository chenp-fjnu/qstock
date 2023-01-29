import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
#引入statsmodels和scipy.stats用于画QQ和PP图
import scipy.stats as scs
import statsmodels.api as sm
import statsmodels.tsa.api as smt
def ts_plot(data, lags=None,title=''):
    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    with plt.style.context('bmh'):
        fig = plt.figure(figsize=(10, 8))
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0))

        acf_ax = plt.subplot2grid(layout, (1, 0))
        pacf_ax = plt.subplot2grid(layout, (1, 1))
        qq_ax = plt.subplot2grid(layout, (2, 0))
        pp_ax = plt.subplot2grid(layout, (2, 1))

        data.plot(ax=ts_ax)
        ts_ax.set_title(title+'时序图')
        smt.graphics.plot_acf(data, lags=lags, ax=acf_ax, alpha=0.5)
        acf_ax.set_title('自相关系数')
        smt.graphics.plot_pacf(data, lags=lags, ax=pacf_ax, alpha=0.5)
        pacf_ax.set_title('偏自相关系数')
        sm.qqplot(data, line='s', ax=qq_ax)
        qq_ax.set_title('QQ 图')
        scs.probplot(data, sparams=(data.mean(), data.std()), plot=pp_ax)
        pp_ax.set_title('PP 图')
        plt.tight_layout()
        plt.show()
    return
#Q-Q图的结果与P-P图非常相似，只是P-P图是用分布的累计比，而Q-Q图用的是分布的分位数来做检验
#和P-P图一样，如果数据为正态分布，则在Q-Q正态分布图中，数据点应基本在图中对角线上

# #使用numpy简单模拟白噪声过程
# np.random.seed(1)
# # plot of discrete white noise
# randser = np.random.normal(size=500)
# ts_plot(randser, lags=30,title='白噪声')
#
# #从标准正态分布采样模拟一个随机游走
# np.random.seed(2)
# n_samples = 1000
# x = w = np.random.normal(size=n_samples)
# for t in range(1,n_samples):
#     x[t] = x[t-1] + w[t]
# ts_plot(x, lags=30,title='随机游走')
#
# # First difference of simulated Random Walk series
# ts_plot(np.diff(x), lags=30)

#沪深300近三年价格数据
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
data=pd.DataFrame(df,columns=['close'])
#对数收益率
data['logret']=np.log(data.close/data.close.shift(1))
#普通收益率
data['ret']=data.close/data.close.shift(1)-1
data=data.dropna()

#沪深300股价的平稳性
#观察时序图
# ts_plot(data.close,lags=30,title='沪深300股价')

#沪深300收益率,对数收益率与算术收益率差异不是很大
# ts_plot(data.logret,lags=30,title='沪深300收益率')

#statsmodel和arch包都提供了adf检验的函数
#statsmodel也提供了多种方式使用adfulle单位根检验函数
#这些方法得到的结果是一致的
#使用stats子模块中diagnostic（模型诊断）单位根检验unitroot_adf
# from statsmodels.stats.diagnostic import unitroot_adf

print(sm.tsa.stattools.adfuller(data.close))
