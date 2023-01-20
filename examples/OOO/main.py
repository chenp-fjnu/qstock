#导入需要用到的模块
import numpy as np
import pandas as pd
from dateutil.parser import parse
from datetime import datetime,timedelta
from Data import Data
import qstock as qs
import matplotlib as mpl
import matplotlib.pyplot as plt

#实例类
data=Data()

# #获取沪深A股最新行情指标
# df=qs.realtime_data()
# print(df.head())
# data.saveToDB(df,'realtime_data')
#
# df=qs.realtime_data(code=['中国平安','300684','锂电池ETF','BK0679','上证指数'])
# print(df.head())

#股票日内交易数据
sh=qs.intraday_data('中国平安')
#将数据列表中的第0列'date'设置为索引
sh.index=sh['时间']
#画出上证指数收盘价的走势
sh['成交价'].plot(figsize=(12,6))
plt.title('中国平安分时图')
plt.xlabel('时间')
plt.show()
# data.saveToDB(df,'intraday_data')
#
# df=qs.stock_snapshot('中国平安')
# data.saveToDB(df,'stock_snapshot')
#
# df=qs.realtime_change('60日新高')
# data.saveToDB(df,'realtime_change')
#
#
# #默认日频率、前复权所有历史数据
# #open：开盘价，high：最高价，low：最低价，close：收盘价
# #vol：成交量，turnover：成交金额，turnover_rate:换手率
# #在notebook上输入"qs.get_data?"可查看数据接口的相应参数
# code_list=['sh','sz','cyb','zxb','hs300','sz50','zz500','601318']
# df=qs.get_data(code_list)
# data.saveToDB(df,'get_data')
#
# code_list=['中国平安','300684','锂电池ETF','BK0679','上证指数']
# df=qs.get_price(code_list)
# data.saveToDB(df,'get_price')
# df=qs.stock_billboard('20230119','20230120')
#
# data.saveToDB(df,'stock_billboard')
