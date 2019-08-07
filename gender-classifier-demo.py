
#The goal is to clssify anyone as 'male' or 'female' given just their 'height', 'weight' and 'shoe size'
#we use scikit-learn package to train a decision tree with already existing data set to make it able to predict on it's own

#USING DECISION TREE CLASSIFIER

from sklearn import tree

# data set x [height, weight, shoe size]

X = [[181, 80, 44], [177, 70, 43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190, 90, 47], [175, 64, 39], [177, 70, 40], [159, 55, 37], [171, 75, 42], [181, 85, 43]]

#data set Y [Gender labels]
Y = ['male', 'female', 'female', 'female', 'male', 'male', 'male', 'female', 'male', 'female', 'male']

#storing classifier in variable clf calling the Decision Tree Classifier from tree submodule of sklearn
clf = tree.DecisionTreeClassifier()

#training the classifier with our data set x and y
clf = clf.fit(X, Y)

#testing prediction
prediction = clf.predict([[250, 70, 45]])

print (prediction)

