import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split
from collections import Counter
import math

# ---------- UTILITIES ----------------

def Normaliser(data):
    return MinMaxScaler(data)

def TargetEncoder(target):
    """
    Slow but needed as categories are changing across splits, need a better solution in the future.
    """
    newtarget = np.empty((len(target),17))
    for idx in range(len(target)):
        if target[idx] == 1:
            newtarget = np.append(newtarget,[[1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 2:
            newtarget = np.append(newtarget,[[0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 3:
            newtarget = np.append(newtarget,[[0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 4:
            newtarget = np.append(newtarget,[[0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 5:
            newtarget = np.append(newtarget,[[0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 6:
            newtarget = np.append(newtarget,[[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 7:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 8:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 9:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 10:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 11:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,0]], axis=0)
        elif target[idx] == 12:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0]], axis=0)
        elif target[idx] == 13:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0]], axis=0)
        elif target[idx] == 14:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0]], axis=0)
        elif target[idx] == 15:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0]], axis=0)
        elif target[idx] == 16:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0]], axis=0)
        elif target[idx] == 17:
            newtarget = np.append(newtarget,[[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]], axis=0)
    return newtarget

def Accuracy(data1, data2):
    return accuracy_score(data1, data2)

def Split(data, target):
    return train_test_split(data, target)
