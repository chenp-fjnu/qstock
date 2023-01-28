import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

from datetime import datetime

#定义timestamp
t1=pd.Timestamp('2019-01-10')
t2=pd.Timestamp('2018-12-10')
print(f't1= {t1}')
print(f't2= {t2}')
print(f't1与t2时间间隔：{(t1-t2).days}天')


#时间间隔
print(pd.Timedelta(days=5, minutes=50, seconds=20,
                   milliseconds=10, microseconds=10, nanoseconds=10))

#计算当前时间往后100天的日期
dt=datetime.now()+pd.Timedelta(days=100)
#只显示年月日
print(dt.strftime('%Y-%m-%d'))

#定义时期period，默认是A-DEC，代表年份，以12月作为最后一个月
p1=pd.Period('2019')
p2=pd.Period('2018')
print(f'p1={p1}年')
print(f'p2={p2}年')
print(f'p1和p2间隔{p1-p2}年')
#可以直接+、-整数（代表年）
print(f'十年前是{p1-10}年')

#通过asfreq转换时期频率
#以第一个月算,p1前面已赋值为2019年
print(p1.asfreq('M', 'start'))

#以最后一个月算
print(p1.asfreq('M', 'end'))

#财报季度
p=pd.Period('2019Q3',freq='Q-DEC')
#起始月日
print(p.asfreq('D','start'))
#结束月日
print(p.asfreq('D','end'))

#时间戳和时期相互转换
print(p1.to_timestamp(how='end'))
print(p1.to_timestamp(how='start'))

#t1前面赋值为'2019-1-10'
#转换为月时期
print(t1.to_period('M'))
#转换为日时期
print(t1.to_period('D'))
print(t1.to_period('W'))

#使用date_range生成日期序列
#如要详细了解该函数，可以使用help(pd.date_range)
#参数四选三：起始时间，结束时间，freq，periods
#freq='M'月，'D'天，'W'，周，'Y'年
#生成月时间序列
dm = pd.date_range('2018/01/01', freq='M', periods=12)
print(f'生成月时间序列：\n{dm}')
#算头不算尾
#生成年时间序列,默认是以12月结尾，freq='Y-DEC'
dy=pd.date_range('2008-01-01','2019-01-10',freq='Y')
print(f'生成年时间序列：\n{dy}')
#生成日时间序列
dd=pd.date_range('2018-01-01',freq='D',periods=10)
print(f'生成日时间序列：\n{dd}')
#生成周时间序列,默认以sunday周日作为一周最后一日
#如要改成周一作为第一天，freq='W-SAT'
dw=pd.date_range('2018-01-01',freq='W',periods=10)
print(f'生成周时间序列：\n{dw}')

#使用period_range生成日期序列
#参数四选三：起始时间，结束时间，freq，periods
#freq='M'月，'D'天，'W'，周，'Y'年
#生成月时期序列
dpm = pd.period_range('2019/01/01', freq='M', periods=12)
print(f'生成月时间序列：\n{dpm}')
#生成年时期序列,默认是以12月结尾，freq='Y-DEC'
dpy=pd.period_range('2008-01-01','2019-01-10',freq='Y')
print(f'生成年时间序列：\n{dpy}')
#生成日时期序列
dpd=pd.period_range('2018-01-01',freq='D',periods=10)
print(f'生成日时间序列：\n{dpd}')
#生成周时期序列,默认以sunday周日作为一周最后一日
#如要改成周一作为第一天，freq='W-SAT'
dpw=pd.period_range('2018-01-01',freq='W-SUN',periods=10)
print(f'生成周时间序列：\n{dpw}')

#画以时间为x轴的图,pandas的DataFrame自动将index列作为x轴
np.random.seed(2)
#生成日期序列
x=pd.date_range('2018/01/01','2019/12/31', freq='d')
#x=pd.period_range('2018/01/01','2019/12/31', freq='d')
#标准正态分布时间序列
y=np.random.standard_normal(len(x))
#将二者转换为pandas的数据格式
df=pd.DataFrame(y,columns=['标准正态分布'],index=x)
df.plot(figsize=(12,6))
plt.title('模拟标准正态分布随机数')
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()