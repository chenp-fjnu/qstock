# 8 相关图 （Correllogram）
# 相关图用于直观地查看给定数据框（或二维数组）中所有可能的数值变量对之间的相关度量。
import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import patches
from scipy.spatial import ConvexHull
import warnings; warnings.simplefilter('ignore')
# Load Dataset
df = sns.load_dataset('iris')
# Plot

sns.pairplot(df, kind="scatter", hue="species", plot_kws=dict(s=80, edgecolor="white", linewidth=2.5))

sns.pairplot(df, kind="reg", hue="species")

plt.show()