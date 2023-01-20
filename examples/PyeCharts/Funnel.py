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

codes=['sh','sz','cyb','zxb','hs300']
names=['上证指数','深证综指','创业板指','中小板指','沪深300']
name_code=dict(zip(names,codes))
index_data=pd.DataFrame({name:get_price(code).close for name,code in name_code.items()}).dropna()
#index_data.head()

#2010年6月2日至2022年3月24日各指数累计收益率
rets=(index_data/index_data.iloc[0]-1).iloc[-1]*100
from pyecharts.faker import Faker
g = (Funnel()
    .add("",
        [list(z) for z in zip(rets.index,rets.round(2))],
        label_opts=opts.LabelOpts(position="inside"),)
    .set_global_opts(title_opts=opts.TitleOpts(title="指数累计收益率（%)",subtitle='2010.06-2022.03')))

g.render("funnel.html")

