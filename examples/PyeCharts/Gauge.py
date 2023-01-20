#导入数据分析和量化常用库
import pandas as pd
import numpy as np
import talib as ta
import tushare as ts
#导入pyecharts
from pyecharts.charts import *
from pyecharts import options as opts
from pyecharts.commons.utils import JsCode


g = (Gauge()
     .add('', [['上涨占比', 75]],
          title_label_opts=opts.LabelOpts(
            font_size=20, color="blue", font_family="Microsoft YaHei"),
          detail_label_opts=opts.GaugeDetailOpts(formatter='{value}%',offset_center=[0,80])))

g.render("gauge.html")

