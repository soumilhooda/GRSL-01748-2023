import numpy as np
import pandas as pd
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.layers import Dense
from utils.default import Accuracy, 
from collections import Counter
import math
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt

def ANN(activationstring, trainDATA, trainTARGET_Encoded, testDATA, trainTARGET_NonEncoded, testTarget_NonEncoded):

    layer = Dense(500, activation=activationstring, input_dim=4)
    layer = Dense(250, activation=activationstring)(layer)
    output = Dense(17, activation='softmax')(layer)
    model = keras.Model(inputs=input, outputs=output, name="ANN")

    opt = keras.optimizers.Adam(learning_rate=0.005)
    model.compile(loss='categorical_crossentropy', optimizer=opt, metrics=['mae','mse'])

    history = model.fit(trainDATA, trainTARGET_Encoded, batch_size = 100, epochs=100, validation_split=0.05)
    predictions_tr = model.predict(trainDATA)
    predictions_te = model.predict(testDATA)
    predictions_tr = np.argmax(predictions_tr, axis = 1)
    predictions_te = np.argmax(predictions_te, axis = 1)

    print("Train accuracy : ", Accuracy(trainTARGET_NonEncoded, predictions_tr))
    print("Test accuracy : ", Accuracy(testTarget_NonEncoded, predictions_te))

    conf = confusion_matrix(testTarget_NonEncoded, predictions_te)
    sns.heatmap(conf, annot=True, cmap='Blues')
    plt.show()


# def KNN(data, query, k, distance_fn=euclidean_distance, choice_fn=mode):
#     neighbor_distances_and_indices = []
    
    
#     for index, example in enumerate(data):
#         """
#         Calculate the distance between the query example and the current example from the data.
#         """
#         distance = distance_fn(example[:-1], query)
        
#         """
#         Add the distance and the index of the example to an ordered collection
#         """
#         neighbor_distances_and_indices.append((distance, index))
    
#     """
#     Sort the ordered collection of distances and indices from smallest to largest (in ascending order) by the distances
#     """
#     sorted_neighbor_distances_and_indices = sorted(neighbor_distances_and_indices)
    
#     k_nearest_distances_and_indices = sorted_neighbor_distances_and_indices[:k]
    
#     k_nearest_labels = [data[i][-1] for distance, i in k_nearest_distances_and_indices]

#     """
#     Return the mode of the K labels
#     """
#     return k_nearest_distances_and_indices , choice_fn(k_nearest_labels)

