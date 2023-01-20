#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

#模拟连接
links=[{'source':'股票'+str(np.random.randint(1,21)),'target':'股票'+str(np.random.randint(1,21))} for i in range(20*18)]
l=[]
for i in links:
    l.extend(list(i.values()))
d={}
for w in l:
    d[w]=l.count(w)
#节点连接边数越多，节点size越大
nodes=[{'name':k,'symbolSize':v} for k,v in d.items()]

g = (Graph()
    .add("", nodes, links, repulsion=8000)
    .set_global_opts(title_opts=opts.TitleOpts(title="模拟股票关系图")))
g.width = "100%"
g.render("graph.html")

