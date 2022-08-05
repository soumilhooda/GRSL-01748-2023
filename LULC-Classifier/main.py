from turtle import clear
import numpy as np
import pandas as pd
from data.loader import MergedData
from utils.default import Normaliser, TargetEncoder
from models.models import ANN, KNN


# ---------- IMPORTS ----------------
columnNTL = ['LAT', 'LON', '2013NTL', '2014NTL', '2015NTL', '2016NTL', '2017NTL', '2018NTL', '2019NTL', '2020NTL']
columnNDVI = ['LAT', 'LON', '2013NDVI', '2014NDVI', '2015NDVI', '2016NDVI', '2017NDVI', '2018NDVI', '2019NDVI', '2020NDVI']
columnLULC = ['LAT', 'LON', '2013LULC', '2014LULC', '2015LULC', '2016LULC', '2017LULC', '2018LULC', '2019LULC', '2020LULC']

NTL = pd.read_csv("ALL-YEARS-2013-2020/light2013-2020.ascii", delim_whitespace=" ", header=None)
NTL.columns = columnNTL

NDVI = pd.read_csv("ALL-YEARS-2013-2020/ndvi2013-2020.ascii", delim_whitespace=" ", header=None)
NDVI.columns = columnNDVI 

LULC = pd.read_csv("ALL-YEARS-2013-2020/lulc2013-2020.ascii", delim_whitespace=" ", header=None)
LULC.columns = columnLULC 

# ---------- DATA PREPARATION ----------------
DATA, TARGET, trainDATA, testDATA, trainTARGET, testTARGET, COMBINED = MergedData(NTL,NDVI,LULC)

DATA_Normalised = Normaliser(DATA)
trainDATA = Normaliser(trainDATA)
testDATA = Normaliser(testDATA)
trainTARGET_NonEncoded = trainTARGET
testTarget_NonEncoded = testTARGET  
trainTARGET_Encoded = TargetEncoder(trainTARGET)

# ---------- EXPERIMENTS ----------------
"""
Un-Comment whatever model is to be run.
"""

ANN('relu',  trainDATA, trainTARGET_Encoded, testDATA, trainTARGET_NonEncoded, testTarget_NonEncoded) # Specify activation needed for Dense layers.

