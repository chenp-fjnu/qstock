#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

#股票数据可视化分析实例
#获取A股交易数据
def get_price(code='sh',start='2000-01-01',end='2022-03-07'):
    df=ts.get_k_data(code,start,end)
    df.index=pd.to_datetime(df.date)
    #将成交量单位改为10000手并取整数
    df['volume']=(df['volume']/10000).apply(int)
    return df[['open','close','high','low','volume']]
sh=get_price()
#计算指标
def get_data(code,start='2021-01-01',end=''):
    df=get_price(code,start,end)
    df['ma5']=df.close.rolling(5).mean()
    df['ma20']=df.close.rolling(20).mean()
    df['macd'],df['macdsignal'],df['macdhist']=ta.MACD(df.close,fastperiod=12,slowperiod=26,signalperiod=9)
    return df.dropna().round(2)
df=get_data('sh')
def draw_kline(data):
    g = (Kline()
        .add_xaxis(data.index.strftime('%Y%m%d').tolist())
        #y轴数据，默认open、close、high、low，转为list格式
        .add_yaxis(series_name="",
            y_axis=df[['open', 'close', 'low', 'high']].values.tolist(),
            itemstyle_opts=opts.ItemStyleOpts(
                color="red",#阳线红色
                color0="green",#阴线绿色
                border_color="red",
                border_color0="green",),
            markpoint_opts=opts.MarkPointOpts(data=[#添加标记符
                opts.MarkPointItem(type_='max', name='最大值'),
                opts.MarkPointItem(type_='min', name='最小值'),]),
            #添加辅助性，如某期间内最大max最小值min均值average
            markline_opts=opts.MarkLineOpts(
                data=[opts.MarkLineItem(type_="average",
                                        value_dim="close")], ),)
        .set_global_opts(
            datazoom_opts=[opts.DataZoomOpts()],#滑动模块选择
            title_opts=opts.TitleOpts(title="股票K线图",pos_left='center'),))
    return g
draw_kline(df).render("kline.html")