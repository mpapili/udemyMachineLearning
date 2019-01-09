#! /usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# importing the dataset
dataset = pd.read_csv('Data.csv')

# separating FEATURES from DEPENDENT VARIABLE
X = dataset.iloc[:, :-1].values   # everything but last column
print(X)
y = dataset.iloc[:, 3]
print(y)
