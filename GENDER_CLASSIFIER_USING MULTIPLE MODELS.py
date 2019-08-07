
# IN THIS SCRIPT
# I USED 4 DIFFERENT CLASSIFIER MODELS ALONG WITH A DECISION TREE CLASSIFIER
# TO TRAIN A KNOWN DATA SET OF 'HEIGHT', 'WEIGHT' AND 'SHOE SIZE' OF TWO GENDERS
# THEN TEST AND PREDICT WHETHER IF CERTAIN MEASUREMENTS BELONG TO A MALE OR A FEMALE
# THEN I USE ACCURACY METRICS TO DETERMINE WHICH OF THE 5 CLASSIFIER MODELS
# HAVE THE BEST ACCURACY SCORE
# ALL USING SCIKIT-LEARN PACKAGES

from sklearn import tree #-decision tree classifier
from sklearn.svm import SVC #-Support Vector Classification (SVC classifier)
from sklearn.linear_model import Perceptron #-perception classifier
from sklearn.neighbors import KNeighborsClassifier #-KNeighbors classifier
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score #-to determine accuracy
import numpy as np

# Data set (X) and gender labels (Y)
X = [[185, 82, 45], [166, 62, 37], [175, 72, 41], [155, 53, 38], [165, 63, 41], [192, 92, 45], [177, 65, 33],
     [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

Y = ['MALE', 'FEMALE', 'MALE', 'FEMALE', 'MALE', 'MALE', 'FEMALE', 'FEMALE', 'FEMALE', 'MALE', 'MALE']

# CALLING CLASSIFIERS
class_tree = tree.DecisionTreeClassifier()
class_SVC = SVC()
class_perc = Perceptron()
class_KNN = KNeighborsClassifier()
class_GSNB = GaussianNB()


# TRAINING THE MODELS USING X, Y DATA SET
class_tree = class_tree.fit(X, Y)
class_SVC = class_SVC.fit(X, Y)
class_perc = class_perc.fit(X, Y)
class_KNN = class_KNN.fit(X, Y)
class_GSNB = class_GSNB.fit(X, Y)

# TESTING PREDICTION USING SAME DATA SET
predict_tree = class_tree.predict(X)
predict_SVC = class_SVC.predict(X)
predict_perc = class_perc.predict(X)
predict_KNN = class_KNN.predict(X)

# TESTING ACCURACY OF THOSE PREDICTION

