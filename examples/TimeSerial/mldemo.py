#先引入后面可能用到的包（package）
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set()
#正常显示画图时出现的中文和负号
from pylab import mpl
mpl.rcParams['font.sans-serif']=['SimHei']
mpl.rcParams['axes.unicode_minus']=False
import tushare as ts
def get_price(code,start,end):
    df=ts.get_k_data(code,start,end)
    df.index=pd.to_datetime(df.date)
    return df.close

codes=['sh','sz','cyb','zxb','hs300']
names=['上证综指','深证综指','创业板指','中小板指','沪深300']
end_day = pd.to_datetime('2023-1-29')
start_day = end_day - 10 * 252 * pd.tseries.offsets.BDay()
start=start_day.strftime('%Y-%m-%d')
end=end_day.strftime('%Y-%m-%d')
#指数收盘价数据
df = pd.DataFrame({name:get_price(code, start, end) for name,code in zip(names,codes)})
# (df/df.iloc[0]-1).plot(figsize=(12,7))
# plt.title('指数累计收益率\n2011-2023',size=15)


rs=(np.log(df/df.shift(1))).dropna()
# rs.plot(figsize=(12,5))
# plt.title('指数日对数收益率',size=15)



import scipy.stats as stats

def add_mean_std_text(x, **kwargs):
    mean, std = x.mean(), x.std()
    mean_tx = f"均值: {mean:.4%}\n标准差: {std:.4%}"

    txkw = dict(size=14, fontweight='demi', color='red', rotation=0)
    ymin, ymax = plt.gca().get_ylim()
    plt.text(mean+0.025, 0.8*ymax, mean_tx, **txkw)
    return

def plot_dist(rs, ex):
    plt.rcParams['font.size'] = 14
    g = (rs
         .pipe(sns.FacetGrid, height=5,aspect=1.5)
         .map(sns.distplot, ex, kde=False, fit=stats.norm,
              fit_kws={ 'lw':2.5, 'color':'red','label':'正态分布'})
         .map(sns.distplot, ex, kde=False, fit=stats.laplace,
              fit_kws={'linestyle':'--','color':'blue', 'lw':2.5, 'label':'拉普拉斯分布'})
         .map(sns.distplot, ex, kde=False, fit=stats.johnsonsu,
              fit_kws={'linestyle':'-','color':'green','lw':2.5, 'label':'约翰逊分布'})
         .map(add_mean_std_text, ex))
    g.add_legend()
    sns.despine(offset=1)
    plt.title(f'{ex}收益率',size=15)
    return
# plot_dist(rs, '上证综指')


def quantile_plot(x, **kwargs):
    res = stats.probplot(x, fit=True, plot=plt)
    _slope, _int, _r = res[-1]

    ax = plt.gca()
    ax.get_lines()[0].set_marker('s')
    ax.get_lines()[0].set_markerfacecolor('r')
    ax.get_lines()[0].set_markersize(13.0)
    ax.get_children()[-2].set_fontsize(22.)

    txkw = dict(size=14, fontweight='demi', color='r')
    r2_tx = "r^2 = {:.2%}\nslope = {:.4f}".format(_r, _slope)

    ymin, ymax = ax.get_ylim()
    xmin, xmax = ax.get_xlim()
    ax.text(0.5*xmax, .8*ymin, r2_tx, **txkw)

    return
# plt.rcParams['figure.figsize'] = 10,7
# quantile_plot(rs['上证综指'])

def plot_facet_hist(rs, ex):
    plt.rcParams['font.size'] = 12
    df = rs.assign(year=lambda df: df.index.year)
    g = (sns.FacetGrid(df, col='year',col_wrap=2, height=4, aspect=1.2)
         .map(sns.distplot, ex, kde=False, fit=stats.norm,
              fit_kws={ 'lw':2.5,'color':'red', 'label':'正态分布'})
         .map(sns.distplot, ex, kde=False, fit=stats.laplace,
              fit_kws={'linestyle':'--','color':'blue', 'lw':2.5, 'label':'拉普拉斯分布'})
         .map(sns.distplot, ex, kde=False, fit=stats.johnsonsu,
              fit_kws={'linestyle':'-', 'color':'green','lw':2.5, 'label':'约翰逊分布'})
         .map(add_mean_std_text, ex))
    g.add_legend()
    g.fig.subplots_adjust(hspace=.20)
    sns.despine(offset=1)

    return
# plot_facet_hist(rs, '上证综指')

# (rs.groupby(rs.index.year)['上证综指']
#  .agg(['mean', 'std'])
#  .plot(marker='o', subplots=True))


def plot_facet_qq(rs, ex):
    df = rs.assign(year=lambda df: df.index.year)
    g = (df
         .pipe(sns.FacetGrid, col='year',col_wrap=2,
               height=7,aspect=1.3)
         .map(quantile_plot, ex)
         .fig.subplots_adjust(hspace=0.2))
    sns.despine(offset=1, trim=True)

    return
# plot_facet_qq(rs, '上证综指')

norm = stats.norm
RANDOM_STATE=888
def generate_norm_rvs(ser, N=None):
    if not N: N = ser.shape[0]
    return norm.rvs(ser.mean(), ser.std(), size=N, random_state=RANDOM_STATE)

def generate_norm_pdf(ser, N=None):
    if not N: N = ser.shape[0]
    _min, _max = ser.min(), ser.max()
    x = np.linspace(_min, _max, N)
    y = norm.pdf(x, ser.mean(), ser.std())
    return x, y

def generate_norm_cdf(ser, N=None):
    if not N: N = ser.shape[0]
    _min, _max = ser.min(), ser.max()
    x = np.linspace(_min, _max, N)
    y = norm.cdf(x, ser.mean(), ser.std())
    return x, y

def plot_cdf(ser, **kwds):
    g = sns.kdeplot(ser, cumulative=True, lw=3, color='blue')
    x, y = generate_norm_cdf(ser) # 生成正态分布CDF
    g.plot(x, y, color='red', lw=3, label='fitted normal CDF')
    ks, p = stats.kstest(ser, 'norm', args=(ser.mean(), ser.std()))
    xmin,xmax=plt.gca().get_xlim()
    ymin,ymax=plt.gca().get_ylim()
    txkw = dict(size=14, fontweight='demi', color='red', rotation=0)
    tx_N = ser.shape[0]
    tx_args = (ks, p, tx_N, ser.shape[0])
    tx = 'ks 2 sample test\nks: {:.4f}, p: {:.4f}\nrvs sample N: {:.0f}\nreturn sample N: {:.0f}'.format(*tx_args)
    plt.text(xmax*0.2, 0.2*ymax, tx, **txkw)
    sns.despine(offset=1)
    (plt.legend(frameon=True, prop={'weight':'demi', 'size':12})
     .get_frame())

    return
# plot_cdf(rs['上证综指'])


def plot_facet_cdf(rs, ex, **kwds):
    df=rs.assign(year=lambda df:df.index.year)
    g = (df
         .pipe(sns.FacetGrid,
               col='year',
               col_wrap=2,
               height=5,
               aspect=1.3)
         .map(plot_cdf, ex, **kwds))
    g.add_legend()
    g.fig.subplots_adjust(hspace=.20)
    sns.despine(offset=1)
    return
# plot_facet_cdf(rs, '上证综指')
# from sklearn.model_selection import TimeSeriesSplit
# xx = rs['上证综指'].copy()
# _base = 252 # 1年测试样本
# _max_train_sizes = [_base*1, _base*2, _base*3, _base*5]
# _n_split=5
# gs = Grid.GridSpec(_n_split, len(_max_train_sizes), wspace=0.0)
# fig = plt.figure(figsize=(20,25))
# rows = []
# for j, max_size in enumerate(_max_train_sizes):
#     tscv = TimeSeriesSplit(n_splits=_n_split, max_train_size=max_size)
#     for i, (train, test) in enumerate(tscv.split(xx)):
#         tmp_train = xx.iloc[train]
#         tmp_test = xx.iloc[test]
#         min_train_dt, max_train_dt = tmp_train.index.min(), tmp_train.index.max()
#         min_test_dt, max_test_dt = tmp_test.index.min(), tmp_test.index.max()
#         ks, p = stats.ks_2samp(tmp_train, tmp_test) # 获得ks检验统计指标
#         df_row = (max_size, ks, p,
#                   min_train_dt.date(), max_train_dt.date(),
#                   min_test_dt.date(), max_test_dt.date())
#         rows.append(df_row)
#         tmp_ax = plt.subplot(gs[i, j])
#
#         if i in [0,1,2,3,4] and j != 0: tmp_ax.set_yticks([])
#         sns.kdeplot(tmp_train, cumulative=True, lw=3, color='blue', ax=tmp_ax, label='train')
#         sns.kdeplot(tmp_test, cumulative=True, lw=3, color='red', ax=tmp_ax, label='test')
#         plt.title('max train size: {}, ks: {:.4f}, p: {:.4f}\ntrain dates: {}_{}\ntest dates: {}_{}'
#                   .format(max_size, ks, p,
#                           min_train_dt.date(), max_train_dt.date(),
#                           min_test_dt.date(), max_test_dt.date()),
#                   fontsize=11.)
#         plt.subplots_adjust(top=1.03)
#         plt.tight_layout()


plt.show()