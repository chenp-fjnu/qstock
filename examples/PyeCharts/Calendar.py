#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

#获取A股交易数据
def get_price(code='sh',start='2000-01-01',end='2022-03-25'):
    df=ts.get_k_data(code,start,end)
    df.index=pd.to_datetime(df.date)
    #将成交量单位改为10000手并取整数
    df['volume']=(df['volume']/10000).apply(int)
    return df[['open','close','high','low','volume']]
#以2021年3月份以来创业板指数的日收益率数据为例
cyb=get_price('cyb',start='2021-03-01')
data0=(cyb.close/cyb.close.shift(1)-1)*100
data=[[i.strftime('%Y-%m-%d'),round(data0[i],2)] for i in data0.index]
g = (Calendar(init_opts=opts.InitOpts(width="900px", height="250px"))
    .add("",
        data,#添加数据
        calendar_opts=opts.CalendarOpts(
            range_=["2021-3-1","2022-3-25"],
            daylabel_opts=opts.CalendarDayLabelOpts(name_map="cn"),
            monthlabel_opts=opts.CalendarMonthLabelOpts(name_map="cn"),),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="创业板指数日收益率",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(is_show=False,
            max_=5.5,min_=-5,
            orient="horizontal",
            is_piecewise=False,)))
g.render("calendar.html")

