# AR模型全称为Autoregressive Models，即自回归模型，用于刻画因变量能由它的多个滞后项表示

import pandas as pd
import numpy as np
import statsmodels.tsa.api as smt
import statsmodels.tsa.ar_model
import statsmodels.tsa.ar_model as smta
#tsa为Time Series analysis缩写
import statsmodels.api as sm
import scipy.stats as scs
from arch import arch_model
#画图
import matplotlib.pyplot as plt
import matplotlib as mpl
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#先定义一个画图函数，后面都会用到

def ts_plot(data, lags=None,title=''):

    if not isinstance(data, pd.Series):
        data = pd.Series(data)
    #matplotlib官方提供了五种不同的图形风格，
    #包括bmh、ggplot、dark_background、fivethirtyeight和grayscale
    with plt.style.context('ggplot'):
        fig = plt.figure(figsize=(10, 8))
        layout = (3, 2)
        ts_ax = plt.subplot2grid(layout, (0, 0), colspan=2)
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
        scs.probplot(data, sparams=(data.mean(),
                     data.std()), plot=pp_ax)
        pp_ax.set_title('PP 图')
        plt.tight_layout()
        plt.show()
    return

# 模拟AR(1) 过程
#设置随机种子（括号里数字无意义）
np.random.seed(1)
#模拟次数
n=5000
#AR模型的参数
a = 0.8
#扰动项为正态分布
x = w = np.random.normal(size=n)
for t in range(1,n):
    x[t] = a*x[t-1] + w[t]
# #画图
# ts_plot(x, lags=30)

#估计数据的AR模型参数和滞后阶数
def simu_ar(data,a,maxlag=30,true_order = 1):
    '''data:要拟合的数据；a为参数,可以为列表；maxlag:最大滞后阶数'''
    # 拟合AR(p)模型
    result = smt.AR(data).fit(maxlag=maxlag, ic='aic', trend='nc')
    #选择滞后阶数
    est_order = smt.AR(data).select_order(maxlag=maxlag,
                ic='aic', trend='nc')
    #参数选择标准ic : 有四个选择 {‘aic’,’bic’,’hqic’,’t-stat’}
    #趋势项：trend：c是指包含常数项，nc为不含常数项
    #打印结果
    print(f'参数估计值：{result.params.round(2)}，估计的滞后阶数：{est_order}')
    print(f'真实参数值：{a}，真实滞后阶数 {true_order}')
simu_ar(x,a=0.8)