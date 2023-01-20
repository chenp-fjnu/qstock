#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode

l1 = (Liquid()
        .add("今日涨停封板率", [0.65],center=["25%", "50%"])
        .set_global_opts(opts.TitleOpts(title="涨停板封板率",pos_left='center')))
l2 = (Liquid()
        .add("昨日涨停封板率", [0.69],center=["70%", "50%"],is_outline_show=False))
grid = (Grid()
        .add(l1, grid_opts=opts.GridOpts())
        .add(l2, grid_opts=opts.GridOpts()))
grid.render("Liquid.html")

