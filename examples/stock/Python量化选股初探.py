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

print(basics_data.head())