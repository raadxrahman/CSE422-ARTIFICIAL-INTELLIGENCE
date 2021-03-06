# -*- coding: utf-8 -*-
"""5_19101069_MdMahbuburRahman.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lqA5wqE7dBCtyrgkNGBqmQ99GDovfjG8
"""

import pandas as pd
import numpy as np

from sklearn.impute import SimpleImputer
from sklearn.preprocessing import MinMaxScaler

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

x = volunteer.iloc[:,2:]
x

y = volunteer.iloc[:,0:2]
y

y1 = volunteer[['Class(species)']]
y1

scaler = MinMaxScaler()

scaler.fit(x)

X_scaled = scaler.transform(x)

X_scaled