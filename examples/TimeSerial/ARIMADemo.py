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

# Select best lag order for hs300 returns
import tushare as ts
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)
df=pro.index_daily(ts_code='000300.SH')
df.index=pd.to_datetime(df.trade_date)

df=df.sort_index()
df['ret']=np.log(df.close/df.close.shift(1))
max_lag = 30
Y=df.ret.dropna()
#原理与拟合ARMA模型类似
best_aic = np.inf
best_order = None
best_mdl = None
#假定最多滞后4阶
pq_rng = range(5)
#假定最多差分一次
d_rng = range(2)
for i in pq_rng:
    for d in d_rng:
        for j in pq_rng:
            try:
                tmp_mdl = smt.ARIMA(Y.values, order=(i,d,j), trend='n').fit(method='innovations_mle')
                tmp_aic = tmp_mdl.aic
                if tmp_aic < best_aic:
                    best_aic = tmp_aic
                    best_order = (i, d, j)
                    best_mdl = tmp_mdl
            except Exception as e:
                # # 访问异常的错误编号和详细信息
                # print(e.args)
                # print(str(e))
                # print(repr(e))
                continue
print(f'ARIMA模型最佳阶数选择：{best_order}')
# 对拟合残差进行可视化
print(best_mdl.summary())
resid=pd.Series(best_mdl.resid,index=Y.index)
# _ = ts_plot(resid, lags=30,title='沪深300指数ARIMA残差')

# 对沪深300收益率未来20天进行预测
n_steps = 20
#分别设置95%和99%的置信度
f, err95, ci95 = best_mdl.forecast(steps=n_steps)
_, err99, ci99 = best_mdl.forecast(steps=n_steps, alpha=0.01)
date=(df.index[-1]).strftime('%Y%m%d')
cal=pro.trade_cal(exchange='', start_date=date)
idx = cal[cal.is_open==1][:20]['cal_date'].values
fc_95 = pd.DataFrame(np.column_stack([f, ci95]),
index=idx,columns=['forecast', 'lower_ci_95', 'upper_ci_95'])
fc_99 = pd.DataFrame(np.column_stack([ci99]),
      index=idx, columns=['lower_ci_99', 'upper_ci_99'])
fc_all = fc_95.combine_first(fc_99)
#fc_all.head()

# 对预测的20日收益率数据进行可视化
plt.style.use('ggplot')
fig = plt.figure(figsize=(12,7))
ax = plt.gca()
ts = df['ret'][-500:].copy()
ts.plot(ax=ax, label='HS300收益率')
# 样本内预测
pred=best_mdl.predict(np.arange(len(ts)) [0], np.arange(len(ts))[-1])
pf=pd.Series(pred,index=ts.index)
pf.plot(ax=ax, style='r-', label='样本内预测')
fc_all.index=pd.to_datetime(fc_all.index)
fc_all.plot(ax=ax)
plt.fill_between(fc_all.index, fc_all.lower_ci_95,
     fc_all.upper_ci_95, color='gray', alpha=0.7)
plt.fill_between(fc_all.index, fc_all.lower_ci_99,
     fc_all.upper_ci_99, color='gray', alpha=0.2)
plt.title('{} 天HS300收益率预测\nARIMA{}'.format(n_steps,
     best_order))
plt.legend(loc='best', fontsize=10)
plt.show()