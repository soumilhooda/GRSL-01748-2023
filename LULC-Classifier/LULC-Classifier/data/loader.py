import numpy as np
import pandas as pd
from utils.default import Split

# ---------- DATA LOADER ----------------

def MergedData(NTL, NDVI, LULC):
    """"
    The function shall take in data in Numpy format and return a new merged dataset.
    Args :
        Raw data.
    Returns:
        Combined data for learning.
    """

    assert len(NTL) == len(NDVI) == len(LULC)
    assert len(NTL.iloc[0]) == len(NDVI.iloc[0]) == len(LULC.iloc[0])

    NTL = NTL.to_numpy()
    NDVI = NDVI.to_numpy()
    LULC = LULC.to_numpy()

    """   
    Return the next few files if ever need only year wise data.
    Also, needs some cleaning code-wise.
    """

    data2013 = np.append(NTL[:,0:3],NDVI[:,2:3], axis=1)
    target2013 = LULC[:,2:3]
    data2014 = np.append(NTL[:,0:2],NTL[:,3:4], axis=1)
    data2014 = np.append(data2014,NDVI[:,3:4], axis=1) 
    target2014 = LULC[:,2:3] 
    data2015 = np.append(NTL[:,0:2],NTL[:,4:5], axis=1)
    data2015 = np.append(data2015,NDVI[:,4:5], axis=1) 
    target2015 = LULC[:,2:3]
    data2016 = np.append(NTL[:,0:2],NTL[:,5:6], axis=1)
    data2016 = np.append(data2016,NDVI[:,5:6], axis=1) 
    target2016 = LULC[:,2:3]
    data2017 = np.append(NTL[:,0:2],NTL[:,6:7], axis=1)
    data2017 = np.append(data2017,NDVI[:,6:7], axis=1)
    target2017 = LULC[:,2:3]
    data2018 = np.append(NTL[:,0:2],NTL[:,7:8], axis=1)
    data2018 = np.append(data2018,NDVI[:,7:8], axis=1)
    target2018 = LULC[:,2:3]
    data2019 = np.append(NTL[:,0:2],NTL[:,8:9], axis=1)
    data2019 = np.append(data2019,NDVI[:,8:9], axis=1)
    target2019 = LULC[:,2:3]
    data2020 = np.append(NTL[:,0:2],NTL[:,9:10], axis=1)
    data2020 = np.append(data2020,NDVI[:,9:10], axis=1)
    target2020 = LULC[:,2:3]

    """   
    Final files to return. Should probably concat faster.
    """

    data = np.append(data2013,data2014,axis=0)
    data = np.append(data,data2015,axis=0)
    data = np.append(data,data2016,axis=0)
    data = np.append(data,data2017,axis=0)
    data = np.append(data,data2018,axis=0)
    data = np.append(data,data2019,axis=0)
    data = np.append(data,data2020,axis=0)

    target = np.append(target2013,target2014,axis=0)
    target = np.append(target,target2015,axis=0)
    target = np.append(target,target2016,axis=0)
    target = np.append(target,target2017,axis=0)
    target = np.append(target,target2018,axis=0)
    target = np.append(target,target2019,axis=0)
    target = np.append(target,target2020,axis=0)

    trainDATA, testDATA, trainTARGET, testTARGET = Split(data, target)

    combined = np.append(data,target,axis=1)

    return data, target, trainDATA, testDATA, trainTARGET, testTARGET, combined