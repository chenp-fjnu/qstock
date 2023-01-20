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
indexs={'上证综指':'sh','创业板':'cyb'}
index_price=pd.DataFrame({index:get_price(code).close for index,code in indexs.items()}).dropna()
#index_price.head()
#指数年度收益率柱状图
index_ret=index_price/index_price.shift(1)-1
ss=index_ret.to_period('Y')
sss=(ss.groupby(ss.index).apply(lambda x: ((1+x).cumprod()-1).iloc[-1])*100).round(2)

heat_data=(index_price/index_price.shift(1)-1).to_period('M')
heat_data=heat_data.groupby(heat_data.index).apply(lambda x: ((((1+x).cumprod()-1).iloc[-1])*100).round(2))
heat_data=heat_data['2011':'2021']
value = [[i,j,heat_data['上证综指'][str(2011+i)+'-'+str(1+j)]] for i in range(11) for j in range(12)]
year=[str(i) for i in range(2011,2022)]
month=[str(i)+'月' for i in range(1,13)]
g = (HeatMap()
    .add_xaxis(year)
    .add_yaxis("", month, value,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="上证综指月收益率(%)"),
        visualmap_opts=opts.VisualMapOpts(is_show=False,min_=-30,max_=30,)))
g.render("heatmap.html")

