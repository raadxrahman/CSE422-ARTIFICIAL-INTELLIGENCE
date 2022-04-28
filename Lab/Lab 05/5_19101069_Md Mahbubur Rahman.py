# -*- coding: utf-8 -*-
"""5_19101069_MdMahbuburRahman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NSHHX8XAuESsk8N3IeA2YJ2hnbK9QbDa
"""

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split

volunteer = pd.read_csv('/content/leaf_dataset.csv')
volunteer.head(6)

type(volunteer)

volunteer.isnull().sum()

volunteer[['Elongation', 'Maximal Indentation Depth', 'Lobedness', 'Average Contrast', 'Entropy']]

impute = SimpleImputer(missing_values = np.nan, strategy = 'mean')

impute.fit(volunteer[['Elongation']])
volunteer['Elongation'] = impute.transform(volunteer[['Elongation']])


impute.fit(volunteer[['Maximal Indentation Depth']])
volunteer['Maximal Indentation Depth'] = impute.transform(volunteer[['Maximal Indentation Depth']])


impute.fit(volunteer[['Lobedness']])
volunteer['Lobedness'] = impute.transform(volunteer[['Lobedness']])


impute.fit(volunteer[['Average Contrast']])
volunteer['Average Contrast'] = impute.transform(volunteer[['Average Contrast']])

impute.fit(volunteer[['Entropy']])
volunteer['Entropy'] = impute.transform(volunteer[['Entropy']])


volunteer.isnull().sum()

x = volunteer.iloc[:, :-1]
x

y = volunteer.iloc[:, -1]
y

y1 = volunteer[['Class(species)']]
y1

scaler = MinMaxScaler()

scaler.fit(x)

X_scaled = scaler.transform(x)

from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, y1, test_size = 0.25, random_state = 45, stratify = y1)

model = LogisticRegression()
model.fit(X_train, Y_train)
predictions = model.predict(X_test)

logisticreg = accuracy_score(Y_test, predictions)
print("Logistic Regression accuracy: {:.3f}".format(logisticreg))

from sklearn.tree import DecisionTreeClassifier

model_decision_tree = DecisionTreeClassifier(criterion = 'entropy', random_state=1)
model_decision_tree.fit(X_train, Y_train)
predictions = model_decision_tree.predict(X_test)

decisiontree = accuracy_score(Y_test, predictions)
print("Decision Tree accuracy: {:.3f}".format(decisiontree))

import matplotlib.pyplot as plt

data = {'Logistic Regression':logisticreg, 'Decision Tree Classifier':decisiontree}
plt.bar(list(data.keys()), list(data.values()), color = 'blue')

plt.xlabel("Model")
plt.ylabel("Accuracy Score")
plt.title("Logistic Regression vs Decision Tree")
plt.show()