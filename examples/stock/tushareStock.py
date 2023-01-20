#先引入后面分析、可视化等可能用到的库
import tushare as ts

import pandas as pd
import matplotlib.pyplot as plt
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#设置token
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
#ts.set_token(token)
pro = ts.pro_api(token)

#获取当前上市的股票代码、简称、注册地、行业、上市时间等数据
basic=pro.stock_basic(list_status='L')
#查看前五行数据
#basic.head(5)

#获取平安银行日行情数据
pa=pro.daily(ts_code='000001.SZ', start_date='20220101',
               end_date='202301019')
#pa.head()

#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

pa.index=pd.to_datetime(pa.trade_date)
pa=pa.sort_index()

kline = (Kline()
        .add_xaxis(pa.index.strftime('%Y%m%d').tolist())
        #y轴数据，默认open、close、high、low，转为list格式
        .add_yaxis(series_name="",
            y_axis=pa[['open', 'close', 'low', 'high']].values.tolist(),
            markpoint_opts=opts.MarkPointOpts(data=[#添加标记符
                opts.MarkPointItem(type_='max', name='最大值'),
                opts.MarkPointItem(type_='min', name='最小值'),]),
            #添加辅助性，如某期间内最大max最小值min均值average
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average",
                                        value_dim="close")], ),)
        .set_global_opts(
            datazoom_opts=[opts.DataZoomOpts()],#滑动模块选择
            title_opts=opts.TitleOpts(title="平安银行K线图",pos_left='center'),))

kline.render("tushareStock.html")

