import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as datasets
from matplotlib import patches
from scipy.spatial import ConvexHull
from sklearn.datasets import load_iris
iris = load_iris()
print(iris.keys())

n_samples, n_features = iris.data.shape
print((n_samples, n_features))
print(iris.feature_names)
print(iris.data[0:5])
print(iris.target.shape)
print(iris.target_names)
print(iris.target)


iris_data = pd.DataFrame( iris.data,
                          columns=iris.feature_names )
iris_data['species'] = iris.target_names[iris.target]
print(iris_data.head(3).append(iris_data.tail(3)))
sns.pairplot( iris_data, hue='species', palette='husl' );
plt.show()
