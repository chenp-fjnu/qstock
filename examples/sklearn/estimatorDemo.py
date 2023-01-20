# 定义：任何可以基于数据集对一些参数进行估计的对象都被称为估计器。
# 两个核心点：1. 需要输入数据，2. 可以估计参数。估计器首先被创建，然后被拟合。
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression #有监督学习
from sklearn.cluster import KMeans  #无监督学习
from sklearn.datasets import load_iris
model = LinearRegression()

x = np.arange(10)
y = 2 * x + 1
plt.plot( x, y, 'o' );

X = x[:, np.newaxis]
model.fit( X, y )

print(model.coef_)
print(model.intercept_)


model = KMeans( n_clusters=3 )
iris = load_iris()
X = iris.data[:,0:2]
model.fit(X)
print( model.cluster_centers_, '\n')
print( model.labels_, '\n' )
print( model.inertia_, '\n')
print( iris.target )
plt.plot( x, 'o' );
plt.show()
