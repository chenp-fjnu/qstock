# 简介

qstock由“Python金融量化”公众号开发，试图打造成个人量化投研分析开源库，目前包括数据获取（data）、可视化(plot)、选股(stock)和量化回测（backtest）四个模块。其中数据模块（data）数据来源于东方财富网、同花顺、新浪财经等网上公开数据，数据爬虫部分参考了现有金融数据包tushare、akshare和efinance。qstock致力于为用户提供更加简洁和规整化的金融市场数据接口。可视化模块基于plotly.express和pyecharts包，为用户提供基于web的交互图形简单操作接口；选股模块提供了同花顺的技术选股和公众号策略选股，包括RPS、MM趋势、财务指标、资金流模型等，回测模块为大家提供向量化（基于pandas）和基于事件驱动的基本框架和模型。
qstock目前在pypi官网上发布，开源版本为1.1.0，意味着读者直接“pip install qstock ”安装即可使用。GitHub地址：https://github.com/tkfy920/qstock。

目前部分策略选股和策略回测功能仅供知识星球会员使用，会员可在知识星球置顶帖子上上获取qstock-1.1.1.tar.gz （强化版）安装包，进行离线安装。

下面为大家介绍qstock数据模块（data）各函数的具体调用方式和应用举例。


```python
#导入qstock模块
import qstock as qs
```

# 行情交易数据接口

## 实时行情数据
获取指定市场所有标的或单个或多个证券最新行情指标
realtime_data(market='沪深A', code=None):

- market表示行情名称或列表，默认'沪深A股',
    '沪深京A':沪深京A股市场行情; '沪深A':沪深A股市场行情;'沪A':沪市A股市场行情
    '深A':深市A股市场行情;北A :北证A股市场行情;'可转债':沪深可转债市场行情;
    '期货':期货市场行情;'创业板':创业板市场行情;'美股':美股市场行情;
    '港股':港股市场行情;'中概股':中国概念股市场行情;'新股':沪深新股市场行情;
    '科创板':科创板市场行情;'沪股通' 沪股通市场行情;'深股通':深股通市场行情;
    '行业板块':行业板块市场行情;'概念板块':概念板块市场行情;
    '沪深指数':沪深系列指数市场行情;'上证指数':上证系列指数市场行情
    '深证指数':深证系列指数市场行情;'ETF' ETF基金市场行情;'LOF' LOF 基金市场行情
- code:输入单个或多个证券的list，不输入参数，默认返回某市场实时指标
  如code='中国平安'，或code='000001'，或code=['中国平安','晓程科技','东方财富']

### 某市场所有标的最新行情


```python
#获取沪深A股最新行情指标
df=qs.realtime_data()
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>603052</td>
      <td>N可川</td>
      <td>44.00</td>
      <td>49.94</td>
      <td>49.94</td>
      <td>41.62</td>
      <td>41.62</td>
      <td>7.40</td>
      <td>NaN</td>
      <td>21.89</td>
      <td>12720.0</td>
      <td>6.324105e+07</td>
      <td>34.68</td>
      <td>3.435872e+09</td>
      <td>8.589680e+08</td>
      <td>2022-10-11 15:15:17</td>
    </tr>
    <tr>
      <th>1</th>
      <td>300684</td>
      <td>中石科技</td>
      <td>19.97</td>
      <td>13.94</td>
      <td>13.94</td>
      <td>13.14</td>
      <td>13.44</td>
      <td>7.95</td>
      <td>7.52</td>
      <td>36.21</td>
      <td>140266.0</td>
      <td>1.926492e+08</td>
      <td>11.62</td>
      <td>3.915084e+09</td>
      <td>2.460628e+09</td>
      <td>2022-10-11 15:15:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>301319</td>
      <td>C唯特偶</td>
      <td>15.75</td>
      <td>59.30</td>
      <td>60.00</td>
      <td>49.00</td>
      <td>49.00</td>
      <td>51.89</td>
      <td>1.04</td>
      <td>44.63</td>
      <td>72147.0</td>
      <td>4.030864e+08</td>
      <td>51.23</td>
      <td>3.477352e+09</td>
      <td>8.244411e+08</td>
      <td>2022-10-11 15:15:30</td>
    </tr>
    <tr>
      <th>3</th>
      <td>300586</td>
      <td>美联新材</td>
      <td>14.48</td>
      <td>18.66</td>
      <td>19.20</td>
      <td>16.51</td>
      <td>16.63</td>
      <td>5.83</td>
      <td>2.59</td>
      <td>25.39</td>
      <td>226773.0</td>
      <td>4.088953e+08</td>
      <td>16.30</td>
      <td>9.786986e+09</td>
      <td>7.255585e+09</td>
      <td>2022-10-11 15:14:45</td>
    </tr>
    <tr>
      <th>4</th>
      <td>688248</td>
      <td>南网科技</td>
      <td>13.95</td>
      <td>52.37</td>
      <td>53.80</td>
      <td>45.33</td>
      <td>46.86</td>
      <td>7.88</td>
      <td>1.98</td>
      <td>182.90</td>
      <td>61119.0</td>
      <td>3.078895e+08</td>
      <td>45.96</td>
      <td>2.957334e+10</td>
      <td>4.062169e+09</td>
      <td>2022-10-11 15:15:26</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取可转债最新行情指标
df=qs.realtime_data('可转债')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>127070</td>
      <td>大中转债</td>
      <td>12.30</td>
      <td>112.299</td>
      <td>116.500</td>
      <td>110.202</td>
      <td>111.610</td>
      <td>48.33</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>734618.0</td>
      <td>8.267796e+08</td>
      <td>100.000</td>
      <td>1.706945e+09</td>
      <td>1.706945e+09</td>
      <td>2022-10-11 15:16:36</td>
    </tr>
    <tr>
      <th>1</th>
      <td>113016</td>
      <td>小康转债</td>
      <td>10.06</td>
      <td>326.495</td>
      <td>335.830</td>
      <td>292.000</td>
      <td>292.000</td>
      <td>NaN</td>
      <td>6.48</td>
      <td>NaN</td>
      <td>793065.0</td>
      <td>2.547642e+09</td>
      <td>296.653</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 15:16:52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>123057</td>
      <td>美联转债</td>
      <td>9.04</td>
      <td>205.000</td>
      <td>215.680</td>
      <td>192.551</td>
      <td>193.000</td>
      <td>651.34</td>
      <td>5.06</td>
      <td>NaN</td>
      <td>1344781.0</td>
      <td>2.758636e+09</td>
      <td>187.999</td>
      <td>4.232532e+08</td>
      <td>4.232532e+08</td>
      <td>2022-10-11 15:16:45</td>
    </tr>
    <tr>
      <th>3</th>
      <td>123083</td>
      <td>朗新转债</td>
      <td>7.85</td>
      <td>171.000</td>
      <td>171.076</td>
      <td>157.503</td>
      <td>159.000</td>
      <td>24.00</td>
      <td>3.14</td>
      <td>NaN</td>
      <td>131600.0</td>
      <td>2.187826e+08</td>
      <td>158.557</td>
      <td>9.375214e+08</td>
      <td>9.375214e+08</td>
      <td>2022-10-11 15:16:27</td>
    </tr>
    <tr>
      <th>4</th>
      <td>128046</td>
      <td>利尔转债</td>
      <td>7.69</td>
      <td>159.000</td>
      <td>159.597</td>
      <td>149.001</td>
      <td>149.944</td>
      <td>32.16</td>
      <td>3.94</td>
      <td>NaN</td>
      <td>231242.0</td>
      <td>3.601780e+08</td>
      <td>147.650</td>
      <td>1.143209e+09</td>
      <td>1.143209e+09</td>
      <td>2022-10-11 15:16:24</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取期货最新行情指标
df=qs.realtime_data('期货')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>p2210</td>
      <td>棕榈油2210</td>
      <td>7.61</td>
      <td>8034.0</td>
      <td>8212.0</td>
      <td>7862.0</td>
      <td>8150.0</td>
      <td>NaN</td>
      <td>1.10</td>
      <td>NaN</td>
      <td>378.0</td>
      <td>3.088256e+07</td>
      <td>7770.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 15:09:39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>WHM</td>
      <td>强麦主力</td>
      <td>5.13</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>2.656000e+05</td>
      <td>3158.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 13:56:51</td>
    </tr>
    <tr>
      <th>2</th>
      <td>WH303</td>
      <td>强麦303</td>
      <td>5.13</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>3320.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>2.656000e+05</td>
      <td>3158.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 13:56:51</td>
    </tr>
    <tr>
      <th>3</th>
      <td>lu2309</td>
      <td>低硫燃油2309</td>
      <td>4.39</td>
      <td>4400.0</td>
      <td>4400.0</td>
      <td>4185.0</td>
      <td>4185.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>4.0</td>
      <td>1.717000e+05</td>
      <td>4215.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 15:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>lh2211</td>
      <td>生猪2211</td>
      <td>4.21</td>
      <td>25635.0</td>
      <td>25880.0</td>
      <td>24760.0</td>
      <td>24915.0</td>
      <td>NaN</td>
      <td>2.57</td>
      <td>NaN</td>
      <td>4606.0</td>
      <td>1.861672e+09</td>
      <td>24650.0</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 15:09:39</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取美股最新行情指标
df=qs.realtime_data('美股')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>CTAQW</td>
      <td>Carney Technology Acquisition C</td>
      <td>600.0</td>
      <td>0.07</td>
      <td>0.08</td>
      <td>0.04</td>
      <td>0.04</td>
      <td>NaN</td>
      <td>0.56</td>
      <td>NaN</td>
      <td>13698.0</td>
      <td>1081.0</td>
      <td>0.01</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 04:00:00</td>
    </tr>
    <tr>
      <th>1</th>
      <td>FSRXW</td>
      <td>FinServ Acquisition Corp II Wt</td>
      <td>300.0</td>
      <td>0.08</td>
      <td>0.11</td>
      <td>0.02</td>
      <td>0.02</td>
      <td>NaN</td>
      <td>6.90</td>
      <td>NaN</td>
      <td>105119.0</td>
      <td>2319.0</td>
      <td>0.02</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 04:00:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>FRWAW</td>
      <td>PWP Forward Acquisition Corp I</td>
      <td>200.0</td>
      <td>0.09</td>
      <td>0.11</td>
      <td>0.09</td>
      <td>0.11</td>
      <td>NaN</td>
      <td>0.08</td>
      <td>NaN</td>
      <td>400.0</td>
      <td>37.0</td>
      <td>0.03</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 04:00:00</td>
    </tr>
    <tr>
      <th>3</th>
      <td>DHACW</td>
      <td>Digital Health Acquisition Corp</td>
      <td>200.0</td>
      <td>0.15</td>
      <td>0.15</td>
      <td>0.09</td>
      <td>0.09</td>
      <td>NaN</td>
      <td>1.59</td>
      <td>NaN</td>
      <td>25100.0</td>
      <td>2264.0</td>
      <td>0.05</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 04:00:00</td>
    </tr>
    <tr>
      <th>4</th>
      <td>CFFSW</td>
      <td>CF Acquisition Corp VII Wt</td>
      <td>187.5</td>
      <td>0.23</td>
      <td>0.23</td>
      <td>0.19</td>
      <td>0.23</td>
      <td>NaN</td>
      <td>0.27</td>
      <td>NaN</td>
      <td>1025.0</td>
      <td>210.0</td>
      <td>0.08</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>2022-10-11 04:00:00</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取港股最新行情指标
df=qs.realtime_data('港股')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>08208</td>
      <td>WMCH GLOBAL</td>
      <td>31.58</td>
      <td>0.050</td>
      <td>0.054</td>
      <td>0.050</td>
      <td>0.054</td>
      <td>0.00</td>
      <td>0.08</td>
      <td>-0.55</td>
      <td>6.000000e+03</td>
      <td>324.0</td>
      <td>0.038</td>
      <td>36000000.0</td>
      <td>36000000.0</td>
      <td>2022-10-11 14:57:48</td>
    </tr>
    <tr>
      <th>1</th>
      <td>01282</td>
      <td>宝新金融</td>
      <td>31.25</td>
      <td>0.021</td>
      <td>0.022</td>
      <td>0.017</td>
      <td>0.017</td>
      <td>5.77</td>
      <td>9.94</td>
      <td>-1.11</td>
      <td>1.812420e+09</td>
      <td>36182812.0</td>
      <td>0.016</td>
      <td>659137756.0</td>
      <td>659137756.0</td>
      <td>2022-10-11 15:00:02</td>
    </tr>
    <tr>
      <th>2</th>
      <td>01748</td>
      <td>信源企业集团</td>
      <td>28.83</td>
      <td>2.100</td>
      <td>2.300</td>
      <td>1.990</td>
      <td>1.990</td>
      <td>0.00</td>
      <td>NaN</td>
      <td>24.57</td>
      <td>4.000000e+03</td>
      <td>8580.0</td>
      <td>1.630</td>
      <td>924000000.0</td>
      <td>924000000.0</td>
      <td>2022-10-11 11:26:28</td>
    </tr>
    <tr>
      <th>3</th>
      <td>01640</td>
      <td>瑞诚中国传媒</td>
      <td>28.40</td>
      <td>0.520</td>
      <td>0.680</td>
      <td>0.470</td>
      <td>0.470</td>
      <td>0.00</td>
      <td>0.06</td>
      <td>-20.23</td>
      <td>1.400000e+04</td>
      <td>7580.0</td>
      <td>0.405</td>
      <td>208000000.0</td>
      <td>208000000.0</td>
      <td>2022-10-11 14:48:55</td>
    </tr>
    <tr>
      <th>4</th>
      <td>01166</td>
      <td>星凯控股</td>
      <td>24.53</td>
      <td>0.066</td>
      <td>0.067</td>
      <td>0.058</td>
      <td>0.058</td>
      <td>0.02</td>
      <td>3.42</td>
      <td>-1.53</td>
      <td>3.800000e+05</td>
      <td>22900.0</td>
      <td>0.053</td>
      <td>156719134.0</td>
      <td>156719134.0</td>
      <td>2022-10-11 13:42:15</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取行业板块最新行情指标
df=qs.realtime_data('行业板块')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BK0428</td>
      <td>电力行业</td>
      <td>2.82</td>
      <td>14638.84</td>
      <td>14638.84</td>
      <td>14178.22</td>
      <td>14253.21</td>
      <td>0.83</td>
      <td>1.22</td>
      <td>17.79</td>
      <td>26547940</td>
      <td>1.403612e+10</td>
      <td>14237.25</td>
      <td>2609413904000</td>
      <td>2096579648000</td>
      <td>2022-10-11 15:19:21</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BK0457</td>
      <td>电网设备</td>
      <td>2.28</td>
      <td>19037.06</td>
      <td>19105.01</td>
      <td>18572.64</td>
      <td>18628.91</td>
      <td>1.29</td>
      <td>0.91</td>
      <td>21.90</td>
      <td>10845717</td>
      <td>9.984833e+09</td>
      <td>18612.38</td>
      <td>1058539824000</td>
      <td>904721712000</td>
      <td>2022-10-11 15:19:21</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BK1034</td>
      <td>电源设备</td>
      <td>2.23</td>
      <td>1662.13</td>
      <td>1664.34</td>
      <td>1626.23</td>
      <td>1630.02</td>
      <td>1.67</td>
      <td>1.02</td>
      <td>31.79</td>
      <td>4696812</td>
      <td>5.593384e+09</td>
      <td>1625.95</td>
      <td>335518304000</td>
      <td>253868200000</td>
      <td>2022-10-11 15:19:21</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BK0481</td>
      <td>汽车零部件</td>
      <td>2.18</td>
      <td>25146.96</td>
      <td>25208.44</td>
      <td>24573.34</td>
      <td>24702.99</td>
      <td>1.18</td>
      <td>0.87</td>
      <td>20.36</td>
      <td>10684713</td>
      <td>1.320795e+10</td>
      <td>24610.00</td>
      <td>1397170672000</td>
      <td>1081290128000</td>
      <td>2022-10-11 15:19:21</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BK1030</td>
      <td>电机</td>
      <td>1.91</td>
      <td>1280.29</td>
      <td>1288.04</td>
      <td>1255.24</td>
      <td>1260.93</td>
      <td>1.46</td>
      <td>0.84</td>
      <td>19.82</td>
      <td>1188302</td>
      <td>1.982219e+09</td>
      <td>1256.26</td>
      <td>141875700000</td>
      <td>116320915000</td>
      <td>2022-10-11 15:19:21</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取概念板块最新行情指标
df=qs.realtime_data('概念板块')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>BK0988</td>
      <td>钠离子电池</td>
      <td>3.66</td>
      <td>1493.35</td>
      <td>1501.60</td>
      <td>1443.44</td>
      <td>1448.45</td>
      <td>2.08</td>
      <td>1.13</td>
      <td>31.59</td>
      <td>7086087</td>
      <td>1.993973e+10</td>
      <td>1440.64</td>
      <td>1678123744000</td>
      <td>1280127104000</td>
      <td>2022-10-11 15:19:39</td>
    </tr>
    <tr>
      <th>1</th>
      <td>BK1093</td>
      <td>汽车一体化压铸</td>
      <td>3.21</td>
      <td>1019.38</td>
      <td>1027.66</td>
      <td>990.28</td>
      <td>992.81</td>
      <td>2.06</td>
      <td>1.01</td>
      <td>32.38</td>
      <td>1894441</td>
      <td>2.979196e+09</td>
      <td>987.72</td>
      <td>197455773000</td>
      <td>180536004000</td>
      <td>2022-10-11 15:19:39</td>
    </tr>
    <tr>
      <th>2</th>
      <td>BK0679</td>
      <td>超导概念</td>
      <td>3.08</td>
      <td>2445.23</td>
      <td>2452.50</td>
      <td>2370.19</td>
      <td>2370.19</td>
      <td>1.06</td>
      <td>0.97</td>
      <td>20.66</td>
      <td>1848233</td>
      <td>2.413144e+09</td>
      <td>2372.24</td>
      <td>197008432000</td>
      <td>195816668000</td>
      <td>2022-10-11 15:19:39</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BK0968</td>
      <td>固态电池</td>
      <td>3.04</td>
      <td>1738.23</td>
      <td>1750.01</td>
      <td>1695.63</td>
      <td>1702.12</td>
      <td>1.44</td>
      <td>0.99</td>
      <td>32.04</td>
      <td>3607375</td>
      <td>2.260660e+10</td>
      <td>1686.95</td>
      <td>2575113872000</td>
      <td>1739368192000</td>
      <td>2022-10-11 15:19:39</td>
    </tr>
    <tr>
      <th>4</th>
      <td>BK1103</td>
      <td>熔盐储能</td>
      <td>3.01</td>
      <td>746.33</td>
      <td>749.84</td>
      <td>724.10</td>
      <td>727.17</td>
      <td>2.15</td>
      <td>1.07</td>
      <td>20.76</td>
      <td>2302267</td>
      <td>1.352596e+09</td>
      <td>724.52</td>
      <td>76226145000</td>
      <td>71589487000</td>
      <td>2022-10-11 15:19:39</td>
    </tr>
  </tbody>
</table>
</div>




```python
#获取ETF最新行情指标
df=qs.realtime_data('ETF')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>561160</td>
      <td>锂电池ETF</td>
      <td>3.87</td>
      <td>0.779</td>
      <td>0.781</td>
      <td>0.753</td>
      <td>0.753</td>
      <td>8.43</td>
      <td>1.40</td>
      <td>NaN</td>
      <td>677081.0</td>
      <td>5.250960e+07</td>
      <td>0.750</td>
      <td>625797971</td>
      <td>625797971</td>
      <td>2022-10-11 15:20:53</td>
    </tr>
    <tr>
      <th>1</th>
      <td>516650</td>
      <td>有色50ETF</td>
      <td>3.78</td>
      <td>1.016</td>
      <td>1.016</td>
      <td>0.984</td>
      <td>0.992</td>
      <td>2.50</td>
      <td>0.94</td>
      <td>NaN</td>
      <td>7605.0</td>
      <td>7.550040e+05</td>
      <td>0.979</td>
      <td>30952237</td>
      <td>30952237</td>
      <td>2022-10-11 15:20:52</td>
    </tr>
    <tr>
      <th>2</th>
      <td>159755</td>
      <td>电池ETF</td>
      <td>3.73</td>
      <td>0.945</td>
      <td>0.951</td>
      <td>0.916</td>
      <td>0.916</td>
      <td>7.39</td>
      <td>1.37</td>
      <td>NaN</td>
      <td>1595067.0</td>
      <td>1.500235e+08</td>
      <td>0.911</td>
      <td>2039921181</td>
      <td>2039921181</td>
      <td>2022-10-11 15:20:33</td>
    </tr>
    <tr>
      <th>3</th>
      <td>159611</td>
      <td>电力ETF</td>
      <td>3.54</td>
      <td>0.878</td>
      <td>0.878</td>
      <td>0.845</td>
      <td>0.848</td>
      <td>5.02</td>
      <td>1.12</td>
      <td>NaN</td>
      <td>1012772.0</td>
      <td>8.774135e+07</td>
      <td>0.848</td>
      <td>1772825023</td>
      <td>1772825023</td>
      <td>2022-10-11 15:20:36</td>
    </tr>
    <tr>
      <th>4</th>
      <td>562350</td>
      <td>电力指数ETF</td>
      <td>3.52</td>
      <td>0.942</td>
      <td>0.942</td>
      <td>0.909</td>
      <td>0.909</td>
      <td>22.47</td>
      <td>1.38</td>
      <td>NaN</td>
      <td>113272.0</td>
      <td>1.058836e+07</td>
      <td>0.910</td>
      <td>47487068</td>
      <td>47487068</td>
      <td>2022-10-11 15:20:51</td>
    </tr>
  </tbody>
</table>
</div>



### 个股最新行情指标
- code:输入单个或多个证券的list，不输入参数，默认返回某市场实时指标
  如code='中国平安'，或code='000001'，或code=['中国平安','晓程科技','东方财富']


```python
qs.realtime_data(code=['中国平安','300684','锂电池ETF','BK0679','上证指数'])
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>涨幅</th>
      <th>最新</th>
      <th>最高</th>
      <th>最低</th>
      <th>今开</th>
      <th>换手率</th>
      <th>量比</th>
      <th>市盈率</th>
      <th>成交量</th>
      <th>成交额</th>
      <th>昨收</th>
      <th>总市值</th>
      <th>流通市值</th>
      <th>市场</th>
      <th>时间</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>601318</td>
      <td>中国平安</td>
      <td>-0.56</td>
      <td>41.200</td>
      <td>41.870</td>
      <td>41.120</td>
      <td>41.670</td>
      <td>0.25</td>
      <td>0.71</td>
      <td>6.25</td>
      <td>269317</td>
      <td>1.114242e+09</td>
      <td>41.430</td>
      <td>753145946092</td>
      <td>446305777318</td>
      <td>沪A</td>
      <td>2022-10-11 15:25:26</td>
    </tr>
    <tr>
      <th>1</th>
      <td>300684</td>
      <td>中石科技</td>
      <td>19.97</td>
      <td>13.940</td>
      <td>13.940</td>
      <td>13.140</td>
      <td>13.440</td>
      <td>7.95</td>
      <td>7.52</td>
      <td>36.21</td>
      <td>140266</td>
      <td>1.926492e+08</td>
      <td>11.620</td>
      <td>3915083948</td>
      <td>2460628426</td>
      <td>深A</td>
      <td>2022-10-11 15:25:00</td>
    </tr>
    <tr>
      <th>2</th>
      <td>159840</td>
      <td>锂电池ETF</td>
      <td>3.17</td>
      <td>0.748</td>
      <td>0.754</td>
      <td>0.728</td>
      <td>0.728</td>
      <td>11.92</td>
      <td>1.04</td>
      <td>0.00</td>
      <td>1042122</td>
      <td>7.792189e+07</td>
      <td>0.725</td>
      <td>654181986</td>
      <td>654181986</td>
      <td>深A</td>
      <td>2022-10-11 15:24:48</td>
    </tr>
    <tr>
      <th>3</th>
      <td>BK0679</td>
      <td>超导概念</td>
      <td>3.08</td>
      <td>2445.230</td>
      <td>2452.500</td>
      <td>2370.190</td>
      <td>2370.190</td>
      <td>1.06</td>
      <td>0.97</td>
      <td>20.66</td>
      <td>1848233</td>
      <td>2.413144e+09</td>
      <td>2372.240</td>
      <td>197008432000</td>
      <td>195816668000</td>
      <td>板块</td>
      <td>2022-10-11 15:25:34</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000001</td>
      <td>上证指数</td>
      <td>0.19</td>
      <td>2979.790</td>
      <td>2986.910</td>
      <td>2953.500</td>
      <td>2978.060</td>
      <td>0.50</td>
      <td>0.91</td>
      <td>0.00</td>
      <td>208635950</td>
      <td>2.467156e+11</td>
      <td>2974.150</td>
      <td>44091967066770</td>
      <td>37825135460498</td>
      <td>沪A</td>
      <td>2022-10-11 15:25:39</td>
    </tr>
  </tbody>
</table>
</div>



### 日内成交数据
intraday_data(code)
- code可以为股票或债券或期货或基金代码简称或代码，如晓程科技或300139,返回股票、期货、债券等的最新交易日成交情况


```python
#股票日内交易数据
df=qs.intraday_data('中国平安')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名称</th>
      <th>代码</th>
      <th>时间</th>
      <th>昨收</th>
      <th>成交价</th>
      <th>成交量</th>
      <th>单数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>09:15:02</td>
      <td>41.43</td>
      <td>41.43</td>
      <td>52</td>
      <td>0</td>
    </tr>
    <tr>
      <th>1</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>09:15:05</td>
      <td>41.43</td>
      <td>41.43</td>
      <td>99</td>
      <td>0</td>
    </tr>
    <tr>
      <th>2</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>09:15:11</td>
      <td>41.43</td>
      <td>41.43</td>
      <td>98</td>
      <td>0</td>
    </tr>
    <tr>
      <th>3</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>09:15:14</td>
      <td>41.43</td>
      <td>41.43</td>
      <td>101</td>
      <td>0</td>
    </tr>
    <tr>
      <th>4</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>09:15:17</td>
      <td>41.43</td>
      <td>41.43</td>
      <td>103</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>




```python
#基金日内交易数据
df=qs.intraday_data('有色50ETF')
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>名称</th>
      <th>代码</th>
      <th>时间</th>
      <th>昨收</th>
      <th>成交价</th>
      <th>成交量</th>
      <th>单数</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>有色50ETF</td>
      <td>516650</td>
      <td>09:44:08</td>
      <td>0.979</td>
      <td>0.992</td>
      <td>110</td>
      <td>1</td>
    </tr>
    <tr>
      <th>1</th>
      <td>有色50ETF</td>
      <td>516650</td>
      <td>09:44:11</td>
      <td>0.979</td>
      <td>0.992</td>
      <td>465</td>
      <td>1</td>
    </tr>
    <tr>
      <th>2</th>
      <td>有色50ETF</td>
      <td>516650</td>
      <td>09:45:17</td>
      <td>0.979</td>
      <td>0.991</td>
      <td>100</td>
      <td>1</td>
    </tr>
    <tr>
      <th>3</th>
      <td>有色50ETF</td>
      <td>516650</td>
      <td>09:45:41</td>
      <td>0.979</td>
      <td>0.992</td>
      <td>20</td>
      <td>1</td>
    </tr>
    <tr>
      <th>4</th>
      <td>有色50ETF</td>
      <td>516650</td>
      <td>09:50:17</td>
      <td>0.979</td>
      <td>0.991</td>
      <td>54</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



### 获取个股实时交易快照
stock_snapshot(code):
- 获取沪深市场股票最新行情快照，code:股票代码


```python
qs.stock_snapshot('中国平安')
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>代码</th>
      <th>名称</th>
      <th>时间</th>
      <th>涨跌额</th>
      <th>涨跌幅</th>
      <th>最新价</th>
      <th>昨收</th>
      <th>今开</th>
      <th>开盘</th>
      <th>最高</th>
      <th>...</th>
      <th>卖1数量</th>
      <th>卖2数量</th>
      <th>卖3数量</th>
      <th>卖4数量</th>
      <th>卖5数量</th>
      <th>买1数量</th>
      <th>买2数量</th>
      <th>买3数量</th>
      <th>买4数量</th>
      <th>买5数量</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>601318</td>
      <td>中国平安</td>
      <td>15:32:57</td>
      <td>-0.23</td>
      <td>-0.56</td>
      <td>41.2</td>
      <td>41.43</td>
      <td>41.67</td>
      <td>41.67</td>
      <td>41.87</td>
      <td>...</td>
      <td>26</td>
      <td>100</td>
      <td>20</td>
      <td>128</td>
      <td>69</td>
      <td>199</td>
      <td>248</td>
      <td>537</td>
      <td>356</td>
      <td>708</td>
    </tr>
  </tbody>
</table>
<p>1 rows × 37 columns</p>
</div>



### 实时交易盘口异动数据
获取交易日实时盘口异动数据，相当于盯盘小精灵。
realtime_change(flag=None):
- flag：盘口异动类型，默认输出全部类型的异动情况。可选：['火箭发射', '快速反弹','加速下跌', '高台跳水', '大笔买入', '大笔卖出', 
 '封涨停板','封跌停板', '打开跌停板','打开涨停板','有大买盘','有大卖盘', 
 '竞价上涨', '竞价下跌','高开5日线','低开5日线',  '向上缺口','向下缺口', 
 '60日新高','60日新低','60日大幅上涨', '60日大幅下跌']
 上述异动类型分别可使用1-22数字代替。


```python
df=qs.realtime_change('60日新高')
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>时间</th>
      <th>代码</th>
      <th>名称</th>
      <th>板块</th>
      <th>相关信息</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14:44:35</td>
      <td>301153</td>
      <td>中科江南</td>
      <td>60日新高</td>
      <td>64.100000,64.10000,0.070117</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14:16:31</td>
      <td>002246</td>
      <td>北化股份</td>
      <td>60日新高</td>
      <td>11.160000,11.16000,0.089844</td>
    </tr>
    <tr>
      <th>2</th>
      <td>13:33:13</td>
      <td>002279</td>
      <td>久其软件</td>
      <td>60日新高</td>
      <td>5.390000,5.38000,0.054902</td>
    </tr>
    <tr>
      <th>3</th>
      <td>13:19:46</td>
      <td>603318</td>
      <td>水发燃气</td>
      <td>60日新高</td>
      <td>11.400000,11.40000,0.076487</td>
    </tr>
    <tr>
      <th>4</th>
      <td>13:06:01</td>
      <td>002393</td>
      <td>力生制药</td>
      <td>60日新高</td>
      <td>23.950000,23.94000,0.000418</td>
    </tr>
  </tbody>
</table>
</div>




```python
#异动类型：火箭发射
df=qs.realtime_change(1)
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>时间</th>
      <th>代码</th>
      <th>名称</th>
      <th>板块</th>
      <th>相关信息</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14:55:08</td>
      <td>838171</td>
      <td>邦德股份</td>
      <td>火箭发射</td>
      <td>0.183973,10.49000,0.183973</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14:53:13</td>
      <td>300262</td>
      <td>巴安水务</td>
      <td>火箭发射</td>
      <td>0.104651,2.85000,0.104651</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14:52:10</td>
      <td>300262</td>
      <td>巴安水务</td>
      <td>火箭发射</td>
      <td>0.069767,2.76000,0.069767</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14:51:27</td>
      <td>605056</td>
      <td>咸亨国际</td>
      <td>火箭发射</td>
      <td>0.066038,12.43000,0.066038</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14:50:40</td>
      <td>000593</td>
      <td>德龙汇能</td>
      <td>火箭发射</td>
      <td>0.044487,10.80000,0.044487</td>
    </tr>
  </tbody>
</table>
</div>




```python
#快速反弹
df=qs.realtime_change(2)
#查看前几行
df.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>时间</th>
      <th>代码</th>
      <th>名称</th>
      <th>板块</th>
      <th>相关信息</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>14:55:43</td>
      <td>002707</td>
      <td>众信旅游</td>
      <td>快速反弹</td>
      <td>-0.029412,6.60000,-0.029412</td>
    </tr>
    <tr>
      <th>1</th>
      <td>14:55:02</td>
      <td>836892</td>
      <td>广咨国际</td>
      <td>快速反弹</td>
      <td>0.004440,9.05000,0.004440</td>
    </tr>
    <tr>
      <th>2</th>
      <td>14:54:58</td>
      <td>600803</td>
      <td>新奥股份</td>
      <td>快速反弹</td>
      <td>-0.002013,19.83000,-0.002013</td>
    </tr>
    <tr>
      <th>3</th>
      <td>14:54:44</td>
      <td>301331</td>
      <td>恩威医药</td>
      <td>快速反弹</td>
      <td>-0.109229,45.75000,-0.109229</td>
    </tr>
    <tr>
      <th>4</th>
      <td>14:54:00</td>
      <td>603057</td>
      <td>紫燕食品</td>
      <td>快速反弹</td>
      <td>0.019381,29.98000,0.019381</td>
    </tr>
  </tbody>
</table>
</div>



## 历史行情数据

### 历史K线

获取单只或多只证券（股票、基金、债券、期货)的历史K线数据。可以根据realtime_data实时行情接口获取相应金融市场交易标的的代码或简称，用于获取其历史K线数据。
- get_data(code_list, start='19000101', end=None, freq='d', fqt=1)
    
获取股票、指数、债券、期货、基金等历史K线行情。参数说明：
- code_list输入股票list列表，如code_list=['中国平安','贵州茅台','工业富联']
，返回多只股票多期时间的面板数据
- start和end为起始和结束日期，年月日
- freq:时间频率，默认日，1 : 分钟；5 : 5 分钟；15 : 15 分钟；30 : 30 分钟；
    60 : 60 分钟；101或'D'或'd'：日；102或‘w’或'W'：周; 103或'm'或'M': 月
    注意1分钟只能获取最近5个交易日一分钟数据
- fqt:复权类型，0：不复权，1：前复权；2：后复权，默认前复权

#### 个股数据


```python
#默认日频率、前复权所有历史数据
#open：开盘价，high：最高价，low：最低价，close：收盘价
#vol：成交量，turnover：成交金额，turnover_rate:换手率
#在notebook上输入"qs.get_data?"可查看数据接口的相应参数
df=qs.get_data('601318')
df.tail()
```

    100%|████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<?, ?it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-09-28</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>42.20</td>
      <td>42.50</td>
      <td>41.85</td>
      <td>41.89</td>
      <td>422044</td>
      <td>1.776629e+09</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>2022-09-29</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>42.23</td>
      <td>42.34</td>
      <td>41.15</td>
      <td>41.32</td>
      <td>426558</td>
      <td>1.779042e+09</td>
      <td>0.39</td>
    </tr>
    <tr>
      <th>2022-09-30</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.35</td>
      <td>41.98</td>
      <td>41.35</td>
      <td>41.58</td>
      <td>331619</td>
      <td>1.383519e+09</td>
      <td>0.31</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.58</td>
      <td>42.18</td>
      <td>41.38</td>
      <td>41.43</td>
      <td>413876</td>
      <td>1.727385e+09</td>
      <td>0.38</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.67</td>
      <td>41.87</td>
      <td>41.12</td>
      <td>41.20</td>
      <td>269317</td>
      <td>1.114242e+09</td>
      <td>0.25</td>
    </tr>
  </tbody>
</table>
</div>




```python
#个股code_list可以输入代码或简称或多个股票的list
#获取中国平安2022年9月28日至今的5分钟数据，默认前复权
df=qs.get_data('中国平安',start='20220928',freq=5)
df.tail()
```

    100%|███████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 996.75it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-10-11 14:40:00</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.24</td>
      <td>41.31</td>
      <td>41.23</td>
      <td>41.25</td>
      <td>5657</td>
      <td>23351059.0</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2022-10-11 14:45:00</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.25</td>
      <td>41.29</td>
      <td>41.25</td>
      <td>41.25</td>
      <td>3096</td>
      <td>12772796.0</td>
      <td>0.00</td>
    </tr>
    <tr>
      <th>2022-10-11 14:50:00</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.27</td>
      <td>41.31</td>
      <td>41.22</td>
      <td>41.28</td>
      <td>10398</td>
      <td>42899924.0</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2022-10-11 14:55:00</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.28</td>
      <td>41.30</td>
      <td>41.25</td>
      <td>41.29</td>
      <td>5450</td>
      <td>22493409.0</td>
      <td>0.01</td>
    </tr>
    <tr>
      <th>2022-10-11 15:00:00</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>41.29</td>
      <td>41.29</td>
      <td>41.20</td>
      <td>41.20</td>
      <td>8632</td>
      <td>35584890.0</td>
      <td>0.01</td>
    </tr>
  </tbody>
</table>
</div>




```python
#后复权数据,频率为周
df=qs.get_data('中国平安',fqt=2,freq='w')
df.tail()
```

    100%|███████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 499.44it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-09-09</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>114.03</td>
      <td>116.59</td>
      <td>113.07</td>
      <td>116.41</td>
      <td>2142838</td>
      <td>9.417109e+09</td>
      <td>1.98</td>
    </tr>
    <tr>
      <th>2022-09-16</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>116.39</td>
      <td>118.23</td>
      <td>114.77</td>
      <td>114.89</td>
      <td>2104109</td>
      <td>9.421170e+09</td>
      <td>1.94</td>
    </tr>
    <tr>
      <th>2022-09-23</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>114.87</td>
      <td>115.99</td>
      <td>111.85</td>
      <td>113.07</td>
      <td>1818125</td>
      <td>7.865799e+09</td>
      <td>1.68</td>
    </tr>
    <tr>
      <th>2022-09-30</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>112.51</td>
      <td>113.67</td>
      <td>109.33</td>
      <td>110.19</td>
      <td>1799637</td>
      <td>7.579131e+09</td>
      <td>1.66</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>中国平安</td>
      <td>601318</td>
      <td>110.19</td>
      <td>111.39</td>
      <td>109.27</td>
      <td>109.43</td>
      <td>683194</td>
      <td>2.841626e+09</td>
      <td>0.63</td>
    </tr>
  </tbody>
</table>
</div>



#### 获取美股数据


```python
#获取苹果公司股票数据
df=qs.get_data('AAPL')
df.tail()
```

    100%|████████████████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<?, ?it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-10-04</th>
      <td>苹果</td>
      <td>AAPL</td>
      <td>145.03</td>
      <td>146.22</td>
      <td>144.26</td>
      <td>146.10</td>
      <td>87830064</td>
      <td>1.277751e+10</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>2022-10-05</th>
      <td>苹果</td>
      <td>AAPL</td>
      <td>144.08</td>
      <td>147.38</td>
      <td>143.01</td>
      <td>146.40</td>
      <td>79470968</td>
      <td>1.154359e+10</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>2022-10-06</th>
      <td>苹果</td>
      <td>AAPL</td>
      <td>145.81</td>
      <td>147.54</td>
      <td>145.22</td>
      <td>145.43</td>
      <td>68402169</td>
      <td>9.991762e+09</td>
      <td>0.43</td>
    </tr>
    <tr>
      <th>2022-10-07</th>
      <td>苹果</td>
      <td>AAPL</td>
      <td>142.54</td>
      <td>143.10</td>
      <td>139.45</td>
      <td>140.09</td>
      <td>85925559</td>
      <td>1.209460e+10</td>
      <td>0.53</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>苹果</td>
      <td>AAPL</td>
      <td>140.42</td>
      <td>141.89</td>
      <td>138.57</td>
      <td>140.42</td>
      <td>74899002</td>
      <td>1.050082e+10</td>
      <td>0.47</td>
    </tr>
  </tbody>
</table>
</div>



#### 获取期货历史K线数据


```python
df=qs.get_data('棕榈油2210')
df.tail()
```

    100%|███████████████████████████████████████████████████████████████████████████████████| 1/1 [00:00<00:00, 999.60it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-10-03</th>
      <td>棕榈油2210</td>
      <td>MPM22V</td>
      <td>3347.0</td>
      <td>3490.0</td>
      <td>3345.0</td>
      <td>3490.0</td>
      <td>406</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-04</th>
      <td>棕榈油2210</td>
      <td>MPM22V</td>
      <td>3620.0</td>
      <td>3620.0</td>
      <td>3509.0</td>
      <td>3550.0</td>
      <td>126</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-05</th>
      <td>棕榈油2210</td>
      <td>MPM22V</td>
      <td>3625.0</td>
      <td>3650.0</td>
      <td>3585.0</td>
      <td>3586.0</td>
      <td>76</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-06</th>
      <td>棕榈油2210</td>
      <td>MPM22V</td>
      <td>3593.0</td>
      <td>3631.0</td>
      <td>3560.0</td>
      <td>3630.0</td>
      <td>13</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-07</th>
      <td>棕榈油2210</td>
      <td>MPM22V</td>
      <td>3593.0</td>
      <td>3631.0</td>
      <td>3560.0</td>
      <td>0.0</td>
      <td>13</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
</div>



#### 指数
注意上证指数代码'000001'与平安银行股票代码相同，
为避免代码相同引起的混乱，获取指数数据，要输入指数的中文简称或拼音缩写。
如'sh'代表'上证指数'，'sz'代表'深证综指'，'cyb'代表‘创业板指'，'zxb'代表'中小100'（原来的中小板指数），'hs300'代表'沪深300'，'sz50'代表
'上证50','zz500'代表'中证500'等等


```python
code_list=['sh','sz','cyb','zxb','hs300','sz50','zz500']
df=qs.get_data(code_list)
df
```

    100%|███████████████████████████████████████████████████████████████████████████████████| 7/7 [00:00<00:00, 538.57it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2006-01-24</th>
      <td>中小100</td>
      <td>399005</td>
      <td>1457.22</td>
      <td>1471.20</td>
      <td>1446.44</td>
      <td>1459.20</td>
      <td>906549</td>
      <td>7.880290e+08</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>2006-01-25</th>
      <td>中小100</td>
      <td>399005</td>
      <td>1456.09</td>
      <td>1463.72</td>
      <td>1414.45</td>
      <td>1430.02</td>
      <td>1156780</td>
      <td>9.247792e+08</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>2006-02-06</th>
      <td>中小100</td>
      <td>399005</td>
      <td>1433.44</td>
      <td>1482.33</td>
      <td>1433.44</td>
      <td>1482.33</td>
      <td>812891</td>
      <td>7.310323e+08</td>
      <td>0.03</td>
    </tr>
    <tr>
      <th>2006-02-07</th>
      <td>中小100</td>
      <td>399005</td>
      <td>1483.45</td>
      <td>1485.69</td>
      <td>1450.15</td>
      <td>1463.92</td>
      <td>1026231</td>
      <td>9.353850e+08</td>
      <td>0.04</td>
    </tr>
    <tr>
      <th>2006-02-08</th>
      <td>中小100</td>
      <td>399005</td>
      <td>1459.67</td>
      <td>1469.49</td>
      <td>1446.54</td>
      <td>1469.49</td>
      <td>609552</td>
      <td>5.371687e+08</td>
      <td>0.02</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-09-28</th>
      <td>上证指数</td>
      <td>000001</td>
      <td>3089.10</td>
      <td>3089.10</td>
      <td>3044.86</td>
      <td>3045.07</td>
      <td>230098650</td>
      <td>2.760397e+11</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>2022-09-29</th>
      <td>上证指数</td>
      <td>000001</td>
      <td>3067.47</td>
      <td>3076.76</td>
      <td>3026.08</td>
      <td>3041.20</td>
      <td>230030416</td>
      <td>2.764411e+11</td>
      <td>0.55</td>
    </tr>
    <tr>
      <th>2022-09-30</th>
      <td>上证指数</td>
      <td>000001</td>
      <td>3042.17</td>
      <td>3054.61</td>
      <td>3021.93</td>
      <td>3024.39</td>
      <td>204115336</td>
      <td>2.402628e+11</td>
      <td>0.49</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>上证指数</td>
      <td>000001</td>
      <td>3026.94</td>
      <td>3029.45</td>
      <td>2968.28</td>
      <td>2974.15</td>
      <td>243404828</td>
      <td>2.901200e+11</td>
      <td>0.58</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>上证指数</td>
      <td>000001</td>
      <td>2978.06</td>
      <td>2986.91</td>
      <td>2953.50</td>
      <td>2979.79</td>
      <td>208635950</td>
      <td>2.467156e+11</td>
      <td>0.50</td>
    </tr>
  </tbody>
</table>
<p>34431 rows × 9 columns</p>
</div>




```python
#全球指数可参见：https://quote.eastmoney.com/center/qqzs.html
global_indexs=['道琼斯','标普500','纳斯达克','恒生指数','英国富时','法国CAC40','德国DAX',
              '日经225','韩国KOSPI','澳大利亚标普200','印度孟买SENSEX','俄罗斯RTS','加拿大S&P',
               '台湾加权','美元指数','路透CRB商品指数']
```


```python
qs.get_data(global_indexs)
```

    100%|█████████████████████████████████████████████████████████████████████████████████| 16/16 [00:00<00:00, 526.62it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>code</th>
      <th>open</th>
      <th>high</th>
      <th>low</th>
      <th>close</th>
      <th>volume</th>
      <th>turnover</th>
      <th>turnover_rate</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2012-05-11</th>
      <td>路透CRB商品指数</td>
      <td>CRB</td>
      <td>292.64</td>
      <td>293.63</td>
      <td>291.55</td>
      <td>291.80</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2012-05-14</th>
      <td>路透CRB商品指数</td>
      <td>CRB</td>
      <td>289.30</td>
      <td>289.52</td>
      <td>287.79</td>
      <td>288.45</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2012-05-15</th>
      <td>路透CRB商品指数</td>
      <td>CRB</td>
      <td>288.78</td>
      <td>289.76</td>
      <td>287.98</td>
      <td>289.14</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2012-05-16</th>
      <td>路透CRB商品指数</td>
      <td>CRB</td>
      <td>287.99</td>
      <td>289.88</td>
      <td>287.71</td>
      <td>289.35</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2012-05-17</th>
      <td>路透CRB商品指数</td>
      <td>CRB</td>
      <td>289.53</td>
      <td>290.17</td>
      <td>288.80</td>
      <td>289.55</td>
      <td>0</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>2022-10-05</th>
      <td>法国CAC40</td>
      <td>FCHI</td>
      <td>6006.12</td>
      <td>6034.93</td>
      <td>5953.55</td>
      <td>5985.46</td>
      <td>75121637</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-06</th>
      <td>法国CAC40</td>
      <td>FCHI</td>
      <td>6004.11</td>
      <td>6018.47</td>
      <td>5917.27</td>
      <td>5936.42</td>
      <td>63735243</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-07</th>
      <td>法国CAC40</td>
      <td>FCHI</td>
      <td>5911.96</td>
      <td>5956.95</td>
      <td>5855.66</td>
      <td>5866.94</td>
      <td>65700262</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>法国CAC40</td>
      <td>FCHI</td>
      <td>5806.57</td>
      <td>5883.85</td>
      <td>5796.31</td>
      <td>5840.55</td>
      <td>64916714</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>法国CAC40</td>
      <td>FCHI</td>
      <td>5839.21</td>
      <td>5835.22</td>
      <td>5777.66</td>
      <td>5813.09</td>
      <td>8097976</td>
      <td>0.0</td>
      <td>0.0</td>
    </tr>
  </tbody>
</table>
<p>112427 rows × 9 columns</p>
</div>



### 多只证券的历史价格数据
获取单只或多只证券（股票、基金、债券、期货)的收盘价格dataframe

- get_price(code_list, start='19000101', end='20500101', freq='d', fqt=1)

code_list输入股票list列表
 如code_list=['中国平安','贵州茅台','工业富联']


```python
code_list=['中国平安','300684','锂电池ETF','BK0679','上证指数']
df=qs.get_price(code_list)
df.tail()
```

    100%|███████████████████████████████████████████████████████████████████████████████████| 5/5 [00:00<00:00, 623.04it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>锂电池ETF</th>
      <th>中石科技</th>
      <th>中国平安</th>
      <th>超导概念</th>
      <th>上证指数</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-09-28</th>
      <td>0.767</td>
      <td>12.14</td>
      <td>41.89</td>
      <td>2534.49</td>
      <td>3045.07</td>
    </tr>
    <tr>
      <th>2022-09-29</th>
      <td>0.775</td>
      <td>11.91</td>
      <td>41.32</td>
      <td>2539.64</td>
      <td>3041.20</td>
    </tr>
    <tr>
      <th>2022-09-30</th>
      <td>0.745</td>
      <td>11.83</td>
      <td>41.58</td>
      <td>2456.69</td>
      <td>3024.39</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>0.725</td>
      <td>11.62</td>
      <td>41.43</td>
      <td>2372.24</td>
      <td>2974.15</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>0.748</td>
      <td>13.94</td>
      <td>41.20</td>
      <td>2445.23</td>
      <td>2979.79</td>
    </tr>
  </tbody>
</table>
</div>




```python
global_indexs=['道琼斯','标普500','纳斯达克','恒生指数','英国富时','法国CAC40','德国DAX',
              '日经225','韩国KOSPI','澳大利亚标普200','印度孟买SENSEX','俄罗斯RTS','加拿大S&P',
               '台湾加权','美元指数','路透CRB商品指数']
#全球指数价格数据
df=qs.get_price(global_indexs)
df.tail()
```

    100%|█████████████████████████████████████████████████████████████████████████████████| 16/16 [00:00<00:00, 484.79it/s]
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>英国富时全股</th>
      <th>法国CAC40</th>
      <th>纳斯达克</th>
      <th>路透CRB商品指数</th>
      <th>印度孟买SENSEX</th>
      <th>加拿大S&amp;P/TSX</th>
      <th>德国DAX30</th>
      <th>标普500</th>
      <th>澳大利亚标普200</th>
      <th>韩国KOSPI</th>
      <th>俄罗斯RTS</th>
      <th>日经225</th>
      <th>恒生指数</th>
      <th>美元指数</th>
      <th>道琼斯</th>
      <th>台湾加权</th>
    </tr>
    <tr>
      <th>date</th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
      <th></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>2022-10-05</th>
      <td>3848.67</td>
      <td>5985.46</td>
      <td>11148.64</td>
      <td>281.89</td>
      <td>NaN</td>
      <td>19235.09</td>
      <td>12517.18</td>
      <td>3783.28</td>
      <td>6815.7</td>
      <td>2215.22</td>
      <td>1061.97</td>
      <td>27120.53</td>
      <td>18087.97</td>
      <td>111.21</td>
      <td>30273.87</td>
      <td>13801.43</td>
    </tr>
    <tr>
      <th>2022-10-06</th>
      <td>3826.39</td>
      <td>5936.42</td>
      <td>11073.31</td>
      <td>282.26</td>
      <td>58222.10</td>
      <td>18979.01</td>
      <td>12470.78</td>
      <td>3744.52</td>
      <td>6817.5</td>
      <td>2237.86</td>
      <td>1044.82</td>
      <td>27311.30</td>
      <td>18012.15</td>
      <td>112.24</td>
      <td>29926.94</td>
      <td>13892.05</td>
    </tr>
    <tr>
      <th>2022-10-07</th>
      <td>3814.26</td>
      <td>5866.94</td>
      <td>10652.40</td>
      <td>285.62</td>
      <td>58191.29</td>
      <td>18583.13</td>
      <td>12273.00</td>
      <td>3639.66</td>
      <td>6762.8</td>
      <td>2232.84</td>
      <td>1005.04</td>
      <td>27116.11</td>
      <td>17740.05</td>
      <td>112.78</td>
      <td>29296.79</td>
      <td>13702.28</td>
    </tr>
    <tr>
      <th>2022-10-10</th>
      <td>3791.94</td>
      <td>5840.55</td>
      <td>10542.10</td>
      <td>283.06</td>
      <td>57991.11</td>
      <td>NaN</td>
      <td>12272.94</td>
      <td>3612.39</td>
      <td>6667.8</td>
      <td>NaN</td>
      <td>963.88</td>
      <td>NaN</td>
      <td>17216.66</td>
      <td>113.15</td>
      <td>29202.88</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>2022-10-11</th>
      <td>3770.68</td>
      <td>5820.44</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>57606.04</td>
      <td>NaN</td>
      <td>12219.07</td>
      <td>NaN</td>
      <td>6645.0</td>
      <td>2192.07</td>
      <td>947.62</td>
      <td>26401.25</td>
      <td>16801.24</td>
      <td>113.15</td>
      <td>NaN</td>
      <td>13106.03</td>
    </tr>
  </tbody>
</table>
</div>



## 股票龙虎榜数据
- stock_billboard(start=None, end=None)

起始和结束日期默认为None，表示最新，日期格式'2021-08-21'
  


```python
df=qs.stock_billboard('20220901','20221011')
df
```

    4it [00:01,  3.98it/s]                                                                                                 
    




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>股票代码</th>
      <th>股票名称</th>
      <th>上榜日期</th>
      <th>收盘价</th>
      <th>涨跌幅</th>
      <th>换手率</th>
      <th>龙虎榜净买额</th>
      <th>流通市值</th>
      <th>上榜原因</th>
      <th>解读</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>000407</td>
      <td>胜利股份</td>
      <td>2022-10-10</td>
      <td>4.90</td>
      <td>0.6160</td>
      <td>30.6832</td>
      <td>-4.839300e+07</td>
      <td>4.291260e+09</td>
      <td>日换手率达到20%的前5只证券</td>
      <td>西藏自治区资金买入，成功率40.98%</td>
    </tr>
    <tr>
      <th>1</th>
      <td>000560</td>
      <td>我爱我家</td>
      <td>2022-10-10</td>
      <td>2.72</td>
      <td>-9.9338</td>
      <td>7.1263</td>
      <td>-1.398103e+08</td>
      <td>6.119485e+09</td>
      <td>日跌幅偏离值达到7%的前5只证券</td>
      <td>主力做T，成功率27.21%</td>
    </tr>
    <tr>
      <th>2</th>
      <td>000620</td>
      <td>新华联</td>
      <td>2022-10-10</td>
      <td>3.24</td>
      <td>-10.0000</td>
      <td>10.9653</td>
      <td>3.471077e+07</td>
      <td>6.145062e+09</td>
      <td>日跌幅偏离值达到7%的前5只证券</td>
      <td>西藏自治区资金卖出，成功率19.29%</td>
    </tr>
    <tr>
      <th>4</th>
      <td>000756</td>
      <td>新华制药</td>
      <td>2022-10-10</td>
      <td>19.10</td>
      <td>6.0522</td>
      <td>16.9006</td>
      <td>-6.694814e+07</td>
      <td>8.333955e+09</td>
      <td>连续三个交易日内，涨幅偏离值累计达到20%的证券</td>
      <td>主力做T，成功率6.03%</td>
    </tr>
    <tr>
      <th>5</th>
      <td>000801</td>
      <td>四川九洲</td>
      <td>2022-10-10</td>
      <td>7.94</td>
      <td>9.9723</td>
      <td>5.4170</td>
      <td>5.948126e+07</td>
      <td>8.121085e+09</td>
      <td>日涨幅偏离值达到7%的前5只证券</td>
      <td>买一主买，成功率45.67%</td>
    </tr>
    <tr>
      <th>...</th>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
      <td>...</td>
    </tr>
    <tr>
      <th>1164</th>
      <td>603719</td>
      <td>良品铺子</td>
      <td>2022-09-01</td>
      <td>31.00</td>
      <td>2.3440</td>
      <td>8.0772</td>
      <td>-4.730051e+05</td>
      <td>6.934596e+09</td>
      <td>有价格涨跌幅限制的日价格振幅达到15%的前五只证券</td>
      <td>1家机构买入，成功率43.69%</td>
    </tr>
    <tr>
      <th>1165</th>
      <td>603789</td>
      <td>星光农机</td>
      <td>2022-09-01</td>
      <td>8.98</td>
      <td>10.0490</td>
      <td>1.4611</td>
      <td>1.744118e+07</td>
      <td>2.334800e+09</td>
      <td>有价格涨跌幅限制的日收盘价格涨幅偏离值达到7%的前五只证券</td>
      <td>普通席位买入，成功率52.49%</td>
    </tr>
    <tr>
      <th>1166</th>
      <td>603798</td>
      <td>康普顿</td>
      <td>2022-09-01</td>
      <td>11.30</td>
      <td>10.0292</td>
      <td>1.3280</td>
      <td>8.096509e+06</td>
      <td>2.260000e+09</td>
      <td>有价格涨跌幅限制的日收盘价格涨幅偏离值达到7%的前五只证券</td>
      <td>1家机构买入，成功率28.82%</td>
    </tr>
    <tr>
      <th>1167</th>
      <td>605567</td>
      <td>春雪食品</td>
      <td>2022-09-01</td>
      <td>16.43</td>
      <td>-3.1250</td>
      <td>23.0978</td>
      <td>-1.419265e+06</td>
      <td>8.215000e+08</td>
      <td>有价格涨跌幅限制的日换手率达到20%的前五只证券</td>
      <td>西藏自治区资金卖出，成功率23.34%</td>
    </tr>
    <tr>
      <th>1168</th>
      <td>688268</td>
      <td>华特气体</td>
      <td>2022-09-01</td>
      <td>101.96</td>
      <td>16.0483</td>
      <td>13.8121</td>
      <td>5.651519e+07</td>
      <td>3.591029e+09</td>
      <td>有价格涨跌幅限制的日收盘价格涨幅达到15%的前五只证券</td>
      <td>4家机构买入，成功率46.11%</td>
    </tr>
  </tbody>
</table>
<p>985 rows × 10 columns</p>
</div>


