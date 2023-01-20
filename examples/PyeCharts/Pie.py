#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

#tushare pro 120积分（注册后修改个人信息）即可免费调取 11191162@qq.com/7760152
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)
ts.set_token(token)
stock_basic=pro.stock_basic(list_status='L')
#stock_basic.head()
#CDR一般指中国存托凭证Chinese Depository Receipt，CDR）
#是指由存托人签发、以境外证券为基础在中国境内发行、代表境外基础证券权益的证券。
market=stock_basic.groupby('market')['market'].count()
data_pair=[list(z) for z in zip(market.index,market)]
g = (Pie()
    .add("",data_pair,)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="A股各交易所上市公司数量"),
        legend_opts=opts.LegendOpts(is_show=False),)
    .set_series_opts(tooltip_opts=opts.TooltipOpts(
            trigger="item", formatter="{b}: {c} ({d}%)"
        ),
        label_opts=opts.LabelOpts(formatter="{b}: {c}({d}%)")))
g.width = "100%"
g.render("pie.html")

