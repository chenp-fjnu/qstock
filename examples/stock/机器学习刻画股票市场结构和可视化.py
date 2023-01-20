import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection
from sklearn import cluster, covariance, manifold
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus']=False

import tushare as ts
token='a03cdee7026cbae830bbbb9b618b5b5d9fc99d525dee2aaf1969d36b'
pro=ts.pro_api(token)
#获取上证50成分股票代码和名称
def get_50_code():
    #获取上证50成分股代码
    dd=pro.index_weight(index_code='000016.SH')
    dd=dd[dd.trade_date=='20201130']
    codes50=dd.con_code.values
    #获取全市场股票基本信息
    df = pro.stock_basic(exchange='', list_status='L')
    df=df[df.ts_code.isin(codes50)]
    codes=df.ts_code.values
    names=df.name.values
    stocks=dict(zip(codes,names))
    return stocks

def get_data(code,start='20191210',end='20201210'):
    df=ts.pro_bar(ts_code=code,adj='qfq',
                  start_date=start, end_date=end)
    df.index=pd.to_datetime(df.trade_date)
    df=df.sort_index()
    return df

codes, names = np.array(sorted(get_50_code().items())).T
data=pd.DataFrame({name:(get_data(code).close-get_data(code).open)
                   for code,name in zip(codes,names)})
variation=data.dropna().values

print(data.head())

# 相关系数
edge_model = covariance.GraphicalLassoCV()
X = variation.copy()
X /= X.std(axis=0)
edge_model.fit(X)
_, labels = cluster.affinity_propagation(edge_model.covariance_)
n_labels = labels.max()

for i in range(n_labels + 1):
    print('Cluster %i: %s' % ((i + 1), ', '.join(names[labels == i])))

node_position_model = manifold.LocallyLinearEmbedding(
    n_components=2, eigen_solver='dense', n_neighbors=6)

embedding = node_position_model.fit_transform(X.T).T

# 可视化
plt.figure(1, facecolor='w', figsize=(10, 8))
plt.clf()
ax = plt.axes([0., 0., 1., 1.])
plt.axis('off')

# 计算偏相关系数
partial_correlations = edge_model.precision_.copy()
d = 1 / np.sqrt(np.diag(partial_correlations))
partial_correlations *= d
partial_correlations *= d[:, np.newaxis]
non_zero = (np.abs(np.triu(partial_correlations, k=1)) > 0.02)

# 使用嵌入的坐标绘制节点
plt.scatter(embedding[0], embedding[1], s=100 * d ** 2, c=labels,
            cmap=plt.cm.nipy_spectral)

# 画相互关联的边
start_idx, end_idx = np.where(non_zero)
segments = [[embedding[:, start], embedding[:, stop]]
            for start, stop in zip(start_idx, end_idx)]
values = np.abs(partial_correlations[non_zero])
lc = LineCollection(segments,
                    zorder=0, cmap=plt.cm.hot_r,
                    norm=plt.Normalize(0, .7 * values.max()))
lc.set_array(values)
lc.set_linewidths(15 * values)
ax.add_collection(lc)

#向每个节点添加一个标签，难点在于定位标签，以避免与其他标签重叠
for index, (name, label, (x, y)) in enumerate(
        zip(names, labels, embedding.T)):

    dx = x - embedding[0]
    dx[index] = 1
    dy = y - embedding[1]
    dy[index] = 1
    this_dx = dx[np.argmin(np.abs(dy))]
    this_dy = dy[np.argmin(np.abs(dx))]
    if this_dx > 0:
        horizontalalignment = 'left'
        x = x + .002
    else:
        horizontalalignment = 'right'
        x = x - .002
    if this_dy > 0:
        verticalalignment = 'bottom'
        y = y + .002
    else:
        verticalalignment = 'top'
        y = y - .002
    plt.text(x, y, name, size=10,
             horizontalalignment=horizontalalignment,
             verticalalignment=verticalalignment,
             bbox=dict(facecolor='w',
                       edgecolor=plt.cm.nipy_spectral(label / float(n_labels)),
                       alpha=.6))

plt.xlim(embedding[0].min() - .15 * embedding[0].ptp(),
         embedding[0].max() + .10 * embedding[0].ptp(),)
plt.ylim(embedding[1].min() - .03 * embedding[1].ptp(),
         embedding[1].max() + .03 * embedding[1].ptp())

plt.show()
