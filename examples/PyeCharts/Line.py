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

#不同点位设置不同颜色
des=sh.close.describe()
v1,v2,v3=np.ceil(des['25%']),np.ceil(des['50%']),np.ceil(des['75%'])
pieces=[{"min": v3, "color": "red"},
        {"min": v2, "max": v3, "color": "blue"},
        {"min": v1, "max": v2, "color": "black"},
        {"max": v1, "color": "green"},]
#链式调用作用域()
g = (
    Line({'width':'100%','height':'480px'})#设置画布大小，px像素
    .add_xaxis(xaxis_data=sh.index.strftime('%Y%m%d').tolist())#x数据
    .add_yaxis(
        series_name="",#序列名称
        y_axis=sh.close.values.tolist(),#添加y数据
        is_smooth=True, #平滑曲线
        is_symbol_show=False,#不显示折线的小圆圈
        label_opts=opts.LabelOpts(is_show=False),
        linestyle_opts=opts.LineStyleOpts(width=2),#线宽
        markpoint_opts=opts.MarkPointOpts(data=[#添加标记符
               opts.MarkPointItem(type_='max', name='最大值'),
               opts.MarkPointItem(type_='min', name='最小值'),],symbol_size=[100,30]),
        markline_opts=opts.MarkLineOpts(#添加均值辅助性
                data=[opts.MarkLineItem(type_="average")], ))
    .set_global_opts(#全局参数设置
        title_opts=opts.TitleOpts(title='上证指数走势', subtitle='2000年-2022年',pos_left='center'),
        tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        visualmap_opts=opts.VisualMapOpts(#视觉映射配置
            orient = "horizontal",split_number = 4,
            pos_left='center',is_piecewise=True,
            pieces=pieces,),)
    .set_series_opts(
        markarea_opts=opts.MarkAreaOpts(#标记区域配置项
            data=[
                opts.MarkAreaItem(name="牛市", x=("20050606", "20071016")),
                opts.MarkAreaItem(name="牛市", x=("20140312", "20150612")),],)))
#使用jupyter notebook显示图形
g.render("line.html")
