# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 17:39:06 2019

@author: Jinyi Zhang
"""

import pandas as pd
from tqdm import tqdm
import matplotlib.pyplot as plt
from qstock.data.money import stock_money

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False

#计算数据在系列时间周期内的收益率
def ret_date(data,w_list=[1,5,20,60,120]):
    df=pd.DataFrame()
    for w in w_list:
        df[str(w)+'日收益率%']=(((data/data.shift(w)-1)*100)
                            .round(2)
                            .iloc[w:]
                            .fillna(0)
                            .T
                            .iloc[:,-1])
    return df

#计算某期间动量排名
def ret_rank(data,w_list=[1,5,20,60,120],c=4):
    #c为w_list里第几个
    rets=ret_date(data,w_list)
    col=rets.columns[c]
    rank_ret=rets.sort_values(col,ascending=False)
    return rank_ret

#同花顺概念动量排名
def ret_top(ths_rets,n=10):
    ths_top=pd.DataFrame()
    for c in ths_rets.columns:
        ths_top[c]=ths_rets.sort_values(c,ascending=False)[:n].index
    return ths_top

#获取同花顺概念指数动量排名名称列表
def ret_top_list(ths_top):
    alist=ths_top.values.tolist()
    words=' '.join([' '.join(s) for s in alist])
    word_list=words.split(' ')
    w_set=set(word_list)
    w_data=[]
    for w in w_set:
       w_data.append([w,word_list.count(w)/len(word_list)])
    return w_data

#rps选股
class RPS(object):
    pass
    print('仅供知识星球会员使用')
        
#量价选股（参考欧奈尔的带柄茶杯形态）
#筛选价格和成交量突破N日阈值的个股
def find_price_vol_stock(data,n=120,rr=0.5):
    pass
    print('仅供知识星球会员使用')

#MM趋势选股（Mark Minervini’s Trend Template）
#参考文章https://zhuanlan.zhihu.com/p/165379657
#股票价格高于150天均线和200天均线
#1、150日均线高于200日均线
#2、200日均线上升至少1个月
#3、50日均线高于150日均线和200日均线
#4、股票价格高于50日均线
#5、股票价格比52周低点高30%
#6、股票价格在52周高点的25%以内
#7、相对强弱指数(RS)大于等于70，这里的相对强弱指的是股票与大盘对比，RS = 股票1年收益率 / 基准指数1年收益率
#这里将第七条RS改为欧奈尔的相对强弱指标，与RPS选股结合选择大于90值的股票

def MM_trend(close,sma=50,mma=150,lma=200):
    pass
    print('仅供知识星球会员使用')

def tscode(code):
    return code+'.SH'if code.startswith('6') else code+'.SZ'

#资金流选股
def moneyflow_stock(codes,w_list=[3,5,10,20,60]):
    pass
    print('仅供知识星球会员使用')

