# 两个核心点：1. 基于学到的参数预测，2. 预测有很多指标。最常见的就是 predict() 函数：
# model.predict(X_test)：评估模型在新数据上的表现
# model.predict(X_train)：确认模型在老数据上的表现
import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split( iris['data'],
                    iris['target'],
                    test_size=0.2 )

print( 'The size of X_train is ', X_train.shape )
print( 'The size of y_train is ', y_train.shape )
print( 'The size of X_test is ', X_test.shape )
print( 'The size of y_test is ', y_test.shape )

from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs',multi_class='multinomial')
model.fit(X_train,y_train)
print(model)


y_pred = model.predict( X_test )
p_pred = model.predict_proba( X_test )
print( y_test, '\n' )
print( y_pred, '\n' )
print( p_pred )

s = ['Class 1 Prob', 'Class 2 Prob', 'Class 3 Prob']
prob_DF = pd.DataFrame( p_pred, columns=s )
prob_DF['Predicted Class'] = y_pred
print(prob_DF.head())
# score() 返回的是分类准确率

print( model.score( X_test, y_test ) )
print( np.sum(y_pred==y_test)/len(y_test) )
# decision_function() 返回的是每个样例在每个类下的分数值
decision_score = model.decision_function( X_test )
print( decision_score )


s = ['Class 1 Score', 'Class 2 Score', 'Class 3 Score']
decision_DF = pd.DataFrame( decision_score, columns=s )
decision_DF['Predicted Class'] = y_pred
print(decision_DF.tail())


from sklearn.cluster import KMeans
model=KMeans(n_clusters=3)
model.fit(X_train[:,0:2])

idx_pred = model.predict( X_test[:,0:2] )
print( idx_pred )
print( y_test )
print(model.score( X_test[:,0:2] ))