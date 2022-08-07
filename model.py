import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import funcs as f

X,Y = f.read_file()
X = f.prep_input(X)
# Splitting into train and test for calculating the accuracy
X_train, X_test, y_train, y_test = train_test_split(X,Y,test_size=0.25,random_state=10,stratify=Y)

#Standardize the training and testing data
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

#Store the standard scaler function in pickle file
pickle.dump(sc, open('sc.pkl', 'wb'))

# Training the model
classifier_rfg=RandomForestClassifier(random_state=33, n_estimators=40)
parameters=[{'min_samples_split':[2,3,4,5],'criterion':['gini','entropy'],'min_samples_leaf':[1,2,3]}]

model_gridrf=GridSearchCV(estimator=classifier_rfg, param_grid=parameters, scoring='accuracy',cv=10)
model_gridrf.fit(X_train,y_train)

#Store the model in pickle file
pickle.dump(model_gridrf, open('model_gridrf.pkl', 'wb'))

print("Done training model")
