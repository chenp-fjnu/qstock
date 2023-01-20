# 定义：转换器也是一种估计器，两者都带拟合功能，但估计器做完拟合来预测，而转换器做完拟合来转换。
# 核心点：估计器里 fit + predict，转换器里 fit + transform。
# 本节介绍两大类转换器
# 将分类型变量 (categorical) 编码成数值型变量 (numerical)
# 规范化 (normalize) 或标准化 (standardize) 数值型变量
import numpy as np
import pandas as pd

enc = ['win','draw','lose','win']
dec = ['draw','draw','win']

from sklearn.preprocessing import LabelEncoder
LE = LabelEncoder()
print( LE.fit(enc) )
print( LE.classes_ )
print( LE.transform(dec) )


from sklearn.preprocessing import OrdinalEncoder
OE = OrdinalEncoder()
enc_DF = pd.DataFrame(enc)
dec_DF = pd.DataFrame(dec)
print( OE.fit(enc_DF) )
print( OE.categories_ )
print( OE.transform(dec_DF) )



from sklearn.preprocessing import OneHotEncoder
OHE = OneHotEncoder()

num = LE.fit_transform(enc)
print( num )
OHE_y = OHE.fit_transform( num.reshape(-1,1) )
print(OHE_y)
print(OHE_y.toarray())

OHE = OneHotEncoder()
print(OHE.fit_transform( enc_DF ).toarray())


from sklearn.preprocessing import MinMaxScaler

X = np.array( [0, 0.5, 1, 1.5, 2, 100] )

X_scale = MinMaxScaler().fit_transform( X.reshape(-1,1) )
print(X_scale)

from sklearn.preprocessing import StandardScaler

X_scale = StandardScaler().fit_transform( X.reshape(-1,1) )
print(X_scale)