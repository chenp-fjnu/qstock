import pandas as pd  
import numpy as np
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

from datetime import datetime
now=datetime.now()
print(f'当前时间：{now}')
print(f'{now.year}年{now.month}月{now.day}日')
print(now.strftime('%Y-%m-%d'))
delta=datetime(2019,1,10)-datetime(2019,1,1,12,30)
print(delta)

from datetime import timedelta
start=datetime(2018,1,1)
#计算50天后是哪一天
print((start + timedelta(50)))
datestr=['12/20/2018','12/11/2018']
new_date=[datetime.strptime(d,'%m/%d/%Y') for d in datestr]
print((new_date[0] - new_date[1]))
print([date.strftime('%Y-%m-%d') for date in new_date])


from dateutil.parser import parse
datestr=['12/20/2018','20180210','2019-01-10']
#转换成datetime格式
new_d=[parse(d) for d in datestr]
#统一为12/20/2018格式
d1=[d.strftime('%m/%d/%Y') for d in new_d]
d2=[d.strftime('%Y%m%d') for d in new_d]
d3=[d.strftime('%Y-%m-%d') for d in new_d]
d4=[d.strftime('%y-%m-%d') for d in new_d]
print(f'datetime格式：\n{new_d}')
print(f'"月/日/年"格式：\n {d1}')
print(f'"年月日"格式：\n{d2}')
print(f'"年-月-日格式"：\n{d3}')
print(f'"年（后两位）-月-日"格式：\n{d4}')
