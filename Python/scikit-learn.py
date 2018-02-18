# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 11:12:00 2016

@author: mgs
"""

from sklearn.linear_model import LogisticRegression
from sklearn.cross_validation import KFold
from matplotlib import pyplot as plt
from sklearn.datasets import load_iris
import numpy as np

data = load_iris()
features = data['data']
feature_names = data['feature_names']
target = data['target']
print(feature_names)

# Normalizacion
## features -= np.mean(features, axis=0)
## features /= np.std(features, axis=0)

#Etiquetado binario
is_versicolor = target == 1
binary_target = np.zeros(len(target))
binary_target[is_versicolor] = 1

# Entrenamiento con Logistic Regression
lr = LogisticRegression()
lr.fit(features, binary_target)

# Medir exactitud del ajuste
accuracy = np.mean(lr.predict(features) == binary_target)
print ("Trainig Accuracy: %f" % accuracy)

cad = []
cad2 = []

ax = plt.subplot(111)
for t,marker, c in zip(range(3), ">ox", "rgb") :
    aux = ax.scatter(features[target == t, 0],
                features[target == t, 1],
                marker = marker,
                c=c,
                s=100)
    cad.append(aux)
    cad2.append(data.target_names[t])
ax.legend(cad, cad2, ncol=1, loc='upper right')
ax.set_xlabel(u'long.sépalo')
ax.set_ylabel(u'ancho sépalo')
plt.savefig("dataset_iris.jpg")
plt.show()