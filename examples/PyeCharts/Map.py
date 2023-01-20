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
print(stock_basic.head())
#A股上市公司各省分布，将‘深圳’与‘广东’数据合并
areas=stock_basic.groupby('area')['ts_code'].count()
areas['广东']=areas['广东']+areas['深圳']
areas.drop(['深圳'],inplace=True)

data_pair=[list(z) for z in zip(areas.index, areas)]
name_map={'上海市':'上海'} #地图中省份是全称， 获取的数据是简称，需要通过name_map映射才能正常显示数字
g = (Map()
    .add("", data_pair, "china",is_map_symbol_show=False,name_map=name_map)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="A股上市公司各省分布",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(max_=int(areas.max()/100+1)*100,
            orient = "horizontal",pos_left='center',)))
g.width = "100%"
g.render("map.html")

