import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

from datetime import datetime

df=pd.read_csv('000001.SZ.csv')
print(df.head())

# #设置时间作为索引
# df=df.set_index(df['trade_date'])
# #画图，pandas数据表自动将索引作为x轴
# df['close'].plot(figsize=(16,6),label='成交价格')
# plt.title('000001日线图',fontsize=15)
# ax = plt.gca()
# ax.spines['right'].set_color('none')
# ax.spines['top'].set_color('none')
# plt.show()

#由于时间索引列只有时分秒，是object格式，加入年月日再进行样本变换
dd=[str(t) for t in df['trade_date'].values]
dt=pd.to_datetime(dd,format='%Y%m%d')

#构建新的数据框
ts=pd.DataFrame(df['close'].values,columns=['close'],index=dt)

#5日线样本,取最后一个数，标志默认左侧，
print(ts.resample('W').mean())


#将其转换为每小时样本,默认closed='left',label='left'
#可以使用均值mean(),或取第一个数first(),或最后一个last()
print(ts.resample('M').mean())

#frq='W'代表周
df=pd.DataFrame(np.random.randn(5,4),
            index=pd.date_range('1/4/2019',periods=5,freq='W'),
            columns=['GZ','BJ','SH','SZ'])
print(df)
#将上述样本转换为日序列,缺失值使用前值补上
#如使用后值则用bfill()
df_daily=df.resample('D').ffill()
print(df_daily.head())

#根据period来重采样
df1=pd.DataFrame(np.random.randn(2,4),
            index=pd.period_range('1-2017','12-2018',freq='A'),
            columns=['GZ','BJ','SH','SZ'])
print(df1.head())

#Q-DEC: Quarterly, decenber
print(df1.resample('Q-DEC').ffill())

date=pd.date_range('1/1/2018', periods=500, freq='D')
ts=pd.Series(np.random.standard_normal(500),index=date)
print(ts.head())
#按月显示，不统计
#按年是A，季度是Q
tsp=ts.to_period('D')
print(tsp.head())

#根据不同时期显示索引值
#按季度频率Q，月度M，年度A
print(tsp.index.asfreq('Q'))
#按工作日统计
print(tsp.index.asfreq('B'))
#按周进行显示，求和汇总
#月：M，年：A，季度：Q
#sum()、mean（）,first(),last()
print(ts.resample('W').sum().head())

print(ts.resample('AS').sum())
# "AS"是每年第一天为开始日期, "A是每年最后一天

# 按年统计并显示
print(ts.resample('AS').sum().to_period('A'))

# 按季度统计并显示
print(ts.resample('Q').sum().to_period('Q'))
#根据groupby进行resampling
#按月进行汇总求平均值
print(ts.groupby(lambda x: x.year).mean())
#按周进行汇总求平均值
print(ts.groupby(lambda x: x.weekday).mean())