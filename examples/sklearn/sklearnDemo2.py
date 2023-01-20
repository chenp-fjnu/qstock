import numpy as np
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets as datasets
from matplotlib import patches
from scipy.spatial import ConvexHull
from sklearn.datasets import load_iris

digits = datasets.load_digits()
print(digits.keys())

# california_housing = datasets.fetch_california_housing()
# print(california_housing.keys())

gaussian_quantiles = datasets.make_gaussian_quantiles()
print(type(gaussian_quantiles), len(gaussian_quantiles))