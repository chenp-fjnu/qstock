import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

from datetime import datetime

nd=np.datetime64('2019-01-10')
print(nd)
print(np.datetime_as_string(nd))
print(np.datetime64('1901'))
print(nd.astype(datetime))
#生成时间序列
#默认以日为间隔，算头不算尾
print(np.arange('2019-01-05', '2019-01-10', dtype='datetime64'))
#以月为间隔，生成2018年12个月
print(np.arange('2018-01-01', '2019-01-01', dtype='datetime64[M]'))
#以年为间隔
print(np.arange('2015-01-01', '2019-01-20', dtype='datetime64[Y]'))
#以周为间隔
print(np.arange('2018-12-01', '2018-12-20', dtype='datetime64[W]'))

#设定随机种子（括号里的数字只是起标记作用）
np.random.seed(1)
#h:小时，m:分，s：秒，ms微秒
#生成分时
x=np.arange('2019-01-10T00:00:00',
'2019-01-10T23:00:00',dtype='datetime64[m]')
#生成标准正态分布时间序列
y=np.random.standard_normal(len(x))
#设置图片大小
fig=plt.figure(figsize=(12,6))
#将x的np.datetime转换为datetime.datetime
plt.plot(x.astype(datetime),y)
fig.autofmt_xdate()
plt.title('模拟23小时内每分钟正态分布的随机数分布')
# 将右边 上边的两条边颜色设置为空 其实就相当于抹掉这两条边
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
plt.show()