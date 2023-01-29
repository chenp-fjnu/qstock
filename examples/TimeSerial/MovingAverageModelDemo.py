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

#这里使用arma模型进行模拟，设定ar阶数为0，即得到ma模型
alphas = np.array([0.])
betas = np.array([0.6])
ar = np.r_[1, -alphas]
ma = np.r_[1, betas]
#模拟MA的样本数据
ma_sample = smt.arma_generate_sample(ar=ar, ma=ma, nsample=1000)
# ts_plot(ma_sample, lags=30,title='MA(1)模型')

# 对上述模拟数据进行ARMA模型拟合
max_lag = 30
result = smt.ARIMA(ma, order=(0, 1)).fit(maxlag=max_lag,
             method='mle', trend='nc')
print(result.summary())