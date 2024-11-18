from sklearn import tree

#[height, weight, shoe size]
x = [[181,80,44], [177,70,43], [160, 60, 38], [154, 54, 37], [166, 65, 40], [190,90, 47],
     [175, 64, 39], [177, 70, 40],[159, 55, 39], [171, 75, 42], [181, 85, 43], [180, 75, 42]]  # Added one more sample

y = ['male', 'female', 'female', 'female', 'female', 'male', 'male',
     'male', 'female', 'male', 'female', 'male']  # Made sure there are 12 labels

classifier = tree.DecisionTreeClassifier()

classifier = classifier.fit(x, y)

# Ensure input is wrapped inside a list to form a 2D array
prediction = classifier.predict([[220, 90, 41]])

print(prediction)
