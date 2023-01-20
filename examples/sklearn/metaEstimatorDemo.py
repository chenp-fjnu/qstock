# 本节讨论五大元估计器，分别带集成功能的 ensemble，多分类和多标签的 multiclass，
# 多输出的 multioutput，选择模型的 model_selection，和流水线的 pipeline。
#
# ensemble.BaggingClassifier
# ensemble.VotingClassifier
# multiclass.OneVsOneClassifier
# multiclass.OneVsRestClassifier
# multioutput.MultiOutputClassifier
# model_selection.GridSearchCV
# model_selection.RandomizedSearchCV
# pipeline.Pipeline

import numpy as np
import pandas as pd
from sklearn.datasets import load_iris
iris = load_iris()

from sklearn.model_selection import train_test_split
from sklearn import metrics

X_train, X_test, y_train, y_test = train_test_split( iris['data'],
                    iris['target'],
                    test_size=0.2 )


from sklearn.ensemble import RandomForestClassifier

RF = RandomForestClassifier( n_estimators=4, max_depth=5 )
RF.fit( X_train, y_train )

print( RF.estimators_ )

print ( "RF - Accuracy (Train):  %.4g" %
        metrics.accuracy_score(y_train, RF.predict(X_train)) )
print ( "RF - Accuracy (Test):  %.4g" %
        metrics.accuracy_score(y_test, RF.predict(X_test)) )



from sklearn.datasets import load_digits

digits = load_digits()
print(digits.keys())

X_train, X_test, y_train, y_test = train_test_split( digits['data'],
                    digits['target'],
                    test_size=0.2 )
from sklearn.multiclass import OneVsOneClassifier
from sklearn.linear_model import LogisticRegression


print( 'The size of X_train is ', X_train.shape )
print( 'The size of y_train is ', y_train.shape )
print( 'The size of X_test is ', X_test.shape )
print( 'The size of y_test is ', y_test.shape )

ovo_lr=OneVsOneClassifier(LogisticRegression(solver='lbfgs',max_iter=200))
ovo_lr.fit(X_train,y_train)

print( len(ovo_lr.estimators_) )
print ( "OVO LR - Accuracy (Train):  %.4g" %
        metrics.accuracy_score(y_train, ovo_lr.predict(X_train)) )
print ( "OVO LR - Accuracy (Test):  %.4g" %
        metrics.accuracy_score(y_test, ovo_lr.predict(X_test)) )

from sklearn.multiclass import OneVsRestClassifier
ovr_lr=OneVsRestClassifier(LogisticRegression(solver='lbfgs',max_iter=800))
ovr_lr.fit(X_train,y_train)
print( len(ovr_lr.estimators_) )
print ( "OVR LR - Accuracy (Train):  %.4g" %
        metrics.accuracy_score(y_train, ovr_lr.predict(X_train)) )
print ( "OVR LR - Accuracy (Test):  %.4g" %
        metrics.accuracy_score(y_test, ovr_lr.predict(X_test)) )


y_train_multilabel = np.c_[ y_train%2==0, y_train<=4 ]
print(y_train_multilabel)
ovr_ml=OneVsRestClassifier(LogisticRegression(solver='lbfgs',max_iter=800))
ovr_ml.fit(X_train,y_train_multilabel)

print( len(ovr_ml.estimators_) )

print( y_test[:1] )
print( ovr_ml.predict(X_test[:1,:]) )