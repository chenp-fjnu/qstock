#先引入后面可能用到的包（package）
import pandas as pd
import numpy as np
from scipy import stats
import tushare as ts
import matplotlib.pyplot as plt

#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
#调取股票基本面数据和行情数据
#基本面数据
#设置token
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
#ts.set_token(token)
pro = ts.pro_api(token)
basics_data=pro.stock_basic(list_status='L')
#保存数据到本地
# basics_data.to_csv("basics_data.csv",encoding='gbk')
#查看前三行前8列数据
print(basics_data.iloc[:3])
#使用groupby对上市公司归属地进行汇总，
#统计每个省份（直辖市）上市公司的总数
area=basics_data.groupby('area')['name'].count()
#从大到小进行排序，取出前十名
print(area.sort_values(ascending=False)[:10])

#将“广东”与深圳数据合并成新的广东
area['广东']=area['广东']+area['深圳']
area.drop(['深圳'],inplace=True)
print(area.sort_values(ascending=False)[:10])


#导入作图包
from pyecharts.charts import *
from pyecharts import options as opts
# 将数据转化为字典，不转也可以
data_pair=[list(z) for z in zip(area.index, area)]
# province=list(data_pair.keys())
# value=list(data_pair.values())

#maptype='china' 只显示全国直辖市和省级
#数据只能是省名和直辖市的名称
g = (Map()
    .add("", data_pair, "china",is_map_symbol_show=False)
    .set_global_opts(
        title_opts=opts.TitleOpts(title="中国上市公司分布",pos_left='center'),
        visualmap_opts=opts.VisualMapOpts(max_=int(area.max()/100+1)*100,
            orient = "horizontal",pos_left='center',)))
g.width = "100%"
g.render("中国上市公司分布.html")

#定义显示数值标签函数
def autolabel(fig):
    for f in fig:
        height = f.get_height()
        plt.text(f.get_x()+f.get_width()/2.-0.2,
                 1.03*height, '%s' % int(height))
area_top=area.sort_values(ascending=False)[:10]
d=dict(area_top)
plt.figure(figsize=(8,5))
fig=plt.bar(d.keys(), d.values())
autolabel(fig)
plt.title("上市公司总数排名前十省份",fontsize=15)
plt.ylim(0,1000)
plt.show()
#注意，数据不包含港澳台

#考察上市公司分布的集中度情况
top5=(area.sort_values(ascending=False)[:5].sum()/area.sum())*100
top10=(area.sort_values(ascending=False)[:10].sum()/area.sum())*100
print("前五个省份上市公司总数占比{:.2f}%".format(top5))
print("前十个省份上市公司总数占比{:.2f}%".format(top10))

#对上市公司的总资产根据地区分类汇总
totalAssets=basics_data.groupby('area')['totalAssets'].sum()
#单位转换为万亿元，保留四位小数
totalAssets=round(totalAssets/10**8,4)
#排序选出前十大省市
print(totalAssets.sort_values(ascending=False)[:10])