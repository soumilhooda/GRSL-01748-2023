import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_predict, cross_val_score
from sklearn.metrics import confusion_matrix, accuracy_score, fbeta_score, recall_score, f1_score
from sklearn.svm import SVC

# Read data
lulc = pd.read_csv("lulc2013-2020.ascii", delim_whitespace=" ", header=None)
NDVI = pd.read_csv("ndvi2013-2020.ascii", delim_whitespace=" ", header=None)
NTL = pd.read_csv("light2013-2020.ascii", delim_whitespace=" ", header=None)
NLST = pd.read_csv("NLST_WinterHalf_13to20.txt", delim_whitespace=" ", header=None)

years = ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
# Set column names
features = ['LAT', 'LON', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']
lulc.columns = features
NDVI.columns = features
NTL.columns = features
NLST.columns = features

# Create label column
label = [0] * len(lulc)

# Assign label columns using the assign method
NDVI = NDVI.assign(**{f'LABEL{year}': label for year in features[2:]})
NTL = NTL.assign(**{f'LABEL{year}': label for year in features[2:]})
NLST = NLST.assign(**{f'LABEL{year}': label for year in features[2:]})

# Create lulc5class dataframe
lulc5class = lulc[['LAT', 'LON']].copy()
lulc5class = lulc5class.assign(**{year: label for year in features[2:]})

NDVI2013_Stats = np.array([0.006310,0.329295,0.368230,0.406575,0.428990,0.451680,0.497855,0.549734,0.676060])
NDVI2014_Stats = np.array([0.01534,0.31944,0.35232,0.39562,0.42403,0.45191,0.50575,0.57044,0.68919])
NDVI2015_Stats = np.array([0.001440,0.313796,0.339270,0.377435,0.404515,0.433180,0.487600,0.553323,0.690870])
NDVI2016_Stats = np.array([0.084000,0.298626,0.326649,0.360650,0.382765,0.406303,0.459164,0.522264,0.68354])
NDVI2017_Stats = np.array([0.016320,0.314050,0.354115,0.394945,0.423150,0.453055,0.505440,0.562915,0.692900])
NDVI2018_Stats = np.array([0.028490,0.290248,0.325766,0.366240,0.390020,0.414450,0.466064,0.539572,0.693560])
NDVI2019_Stats = np.array([0.034230,0.283785,0.322558,0.362320,0.385895,0.410930,0.464591,0.532113,0.701080])
NDVI2020_Stats = np.array([0.124510,0.317275,0.369860,0.416120,0.443110,0.470660,0.526102,0.578686,0.701330])

NTL2013_Stats = np.array([0.052080,0.117029,0.220620,0.474755,0.898780,1.922630,6.962390,15.433894,166.173920])
NTL2014_Stats = np.array([0.121830,0.189728,0.316550,0.615650,1.086410,2.250460,8.168370,18.230936,139.583240])
NTL2015_Stats = np.array([0.120000,0.226231,0.338837,0.617167,1.059640,2.221200,8.209082,18.110648,116.407750])
NTL2016_Stats = np.array([0.065810,0.145933,0.262828,0.538498,0.980750,2.151752,8.469348,19.178180,133.405980])
NTL2017_Stats = np.array([0.266930,0.339335,0.459495,0.765120,1.249190,2.520820,9.396260,20.549545,113.043390])
NTL2018_Stats = np.array([0.288410,0.383675,0.505946,0.819290,1.309870,2.593840,9.207640,19.376706,79.393230])
NTL2019_Stats = np.array([0.264740,0.361753,0.562240,0.945805,1.563625,3.146050,10.597157,21.035070,104.566140])
NTL2020_Stats = np.array([0.324180,0.436717,0.591118,0.958160,1.515770,2.978240,10.412932,20.602327,106.105190])

NLST2013_Stats = np.array([287.285110,288.048590,288.656923,289.372720,289.908410,290.732959,291.660587,292.370998,294.589492])
NLST2014_Stats = np.array([287.704293,288.619973,289.154898,289.895568,290.460287,291.238315,292.223480,292.973070,295.166597])
NLST2015_Stats = np.array([287.714853,288.427444,288.867664,289.549443,290.218842,290.890540,291.775363,292.491522,294.795607])
NLST2016_Stats = np.array([287.127640,287.982581,288.652156,289.380648,290.043414,290.859635,291.870475,292.733057,295.083667])
NLST2017_Stats = np.array([287.135442,288.091897,288.781463,289.498207,290.071140,290.849413,291.895694,292.797523,295.047878])
NLST2018_Stats = np.array([241.472825,289.383476,289.920992,290.616288,291.038900,291.675645,292.504277,293.060004,294.953475])
NLST2019_Stats = np.array([288.702422,289.265219,289.739503,290.377565,290.835513,291.485930,292.262664,292.898314,294.806772])
NLST2020_Stats = np.array([288.064313,288.709629,289.291594,290.011147,290.526907,291.117690,291.991338,293.069216,296.132568])

for i in range(26458):
    for year in ['2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020']:
        value = lulc[year].loc[i]
        if value in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
            lulc5class[year].loc[i] = 1
        elif value == 10:
            lulc5class[year].loc[i] = 2
        elif value in [11, 15, 17]:
            lulc5class[year].loc[i] = 3
            NDVI['LABEL'+year].loc[i] = 1
            NTL['LABEL'+year].loc[i] = 1
            NLST['LABEL'+year].loc[i] = 1
        elif value == 12 or value == 14:
            lulc5class[year].loc[i] = 4
        elif value == 13:
            lulc5class[year].loc[i] = 5
            NDVI['LABEL'+year].loc[i] = 4
            NTL['LABEL'+year].loc[i] = 4
            NLST['LABEL'+year].loc[i] = 4
        elif value == 16:
            lulc5class[year].loc[i] = 6

for year in years:
    suffix = str(year)

    globals()[f'NDVI_{suffix}'] = NDVI[['LAT', 'LON', suffix, f'LABEL{suffix}']].copy()
    globals()[f'NTL_{suffix}'] = NTL[['LAT', 'LON', suffix, f'LABEL{suffix}']].copy()
    globals()[f'NLST_{suffix}'] = NLST[['LAT', 'LON', suffix, f'LABEL{suffix}']].copy()

    globals()[f'NDVI_{suffix}_Urban'] = globals()[f'NDVI_{suffix}'][(globals()[f'NDVI_{suffix}'][f'LABEL{suffix}'] == 4)]
    globals()[f'NTL_{suffix}_Urban'] = globals()[f'NTL_{suffix}'][(globals()[f'NTL_{suffix}'][f'LABEL{suffix}'] == 4)]
    globals()[f'NLST_{suffix}_Urban'] = globals()[f'NLST_{suffix}'][(globals()[f'NLST_{suffix}'][f'LABEL{suffix}'] == 4)]

    globals()[f'NDVI_{suffix}_Water'] = globals()[f'NDVI_{suffix}'][(globals()[f'NDVI_{suffix}'][f'LABEL{suffix}'] == 1)]
    globals()[f'NTL_{suffix}_Water'] = globals()[f'NTL_{suffix}'][(globals()[f'NTL_{suffix}'][f'LABEL{suffix}'] == 1)]
    globals()[f'NLST_{suffix}_Water'] = globals()[f'NLST_{suffix}'][(globals()[f'NLST_{suffix}'][f'LABEL{suffix}'] == 1)]

    globals()[f'NDVI_{suffix}_NotUrban'] = globals()[f'NDVI_{suffix}'][(globals()[f'NDVI_{suffix}'][f'LABEL{suffix}'] != 4)]
    globals()[f'NTL_{suffix}_NotUrban'] = globals()[f'NTL_{suffix}'][(globals()[f'NTL_{suffix}'][f'LABEL{suffix}'] != 4)]
    globals()[f'NLST_{suffix}_NotUrban'] = globals()[f'NLST_{suffix}'][(globals()[f'NLST_{suffix}'][f'LABEL{suffix}'] != 4)]

    globals()[f'NDVI_{suffix}_NotUrbanNotWater'] = globals()[f'NDVI_{suffix}_NotUrban'][(globals()[f'NDVI_{suffix}_NotUrban'][f'LABEL{suffix}'] != 1)]
    globals()[f'NTL_{suffix}_NotUrbanNotWater'] = globals()[f'NTL_{suffix}_NotUrban'][(globals()[f'NTL_{suffix}_NotUrban'][f'LABEL{suffix}'] != 1)]
    globals()[f'NLST_{suffix}_NotUrbanNotWater'] = globals()[f'NLST_{suffix}_NotUrban'][(globals()[f'NLST_{suffix}_NotUrban'][f'LABEL{suffix}'] != 1)]

for year in years:
    suffix_not_urban_not_water = f'_{year}_NotUrbanNotWater'
    suffix_urban = f'_{year}_Urban'
    suffix_water = f'_{year}_Water'
    
    globals()[f'Rule{suffix_not_urban_not_water}'] = globals()[f'NTL_{year}_NotUrbanNotWater'][['LAT', 'LON']].copy()
    globals()[f'Rule{suffix_not_urban_not_water}']['NTL'] = globals()[f'NTL_{year}_NotUrbanNotWater'][year].values
    globals()[f'Rule{suffix_not_urban_not_water}']['NLST'] = globals()[f'NLST_{year}_NotUrbanNotWater'][year].values
    globals()[f'Rule{suffix_not_urban_not_water}']['NDVI'] = globals()[f'NDVI_{year}_NotUrbanNotWater'][year].values
    globals()[f'Rule{suffix_not_urban_not_water}']['LABEL'] = globals()[f'NTL_{year}_NotUrbanNotWater'][f'LABEL{year}'].values
    
    globals()[f'Rule{suffix_urban}'] = globals()[f'NTL_{year}_Urban'][['LAT', 'LON']].copy()
    globals()[f'Rule{suffix_urban}']['NTL'] = globals()[f'NTL_{year}_Urban'][year].values
    globals()[f'Rule{suffix_urban}']['NLST'] = globals()[f'NLST_{year}_Urban'][year].values
    globals()[f'Rule{suffix_urban}']['NDVI'] = globals()[f'NDVI_{year}_Urban'][year].values
    globals()[f'Rule{suffix_urban}']['LABEL'] = globals()[f'NTL_{year}_Urban'][f'LABEL{year}'].values
    
    globals()[f'Rule{suffix_water}'] = globals()[f'NTL_{year}_Water'][['LAT', 'LON']].copy()
    globals()[f'Rule{suffix_water}']['NTL'] = globals()[f'NTL_{year}_Water'][year].values
    globals()[f'Rule{suffix_water}']['NLST'] = globals()[f'NLST_{year}_Water'][year].values
    globals()[f'Rule{suffix_water}']['NDVI'] = globals()[f'NDVI_{year}_Water'][year].values
    globals()[f'Rule{suffix_water}']['LABEL'] = globals()[f'NTL_{year}_Water'][f'LABEL{year}'].values


def process_data(dataframe, NLST_stats, NTL_stats, NDVI_stats):
    for i in range(len(dataframe)):
        if (dataframe['NLST'].iloc[i] >= NLST_stats[6]) and (dataframe['NTL'].iloc[i] >= NTL_stats[6]) and (NDVI_stats[3] <= dataframe['NDVI'].iloc[i] <= NDVI_stats[6]):
            dataframe['LABEL'].iloc[i] = 3
        elif (dataframe['NLST'].iloc[i] <= NLST_stats[2]) and (dataframe['NTL'].iloc[i] <= NTL_stats[2]) and ((NDVI_stats[3] <= dataframe['NDVI'].iloc[i]) or (dataframe['NDVI'].iloc[i] >= NDVI_stats[6])):
            dataframe['LABEL'].iloc[i] = 2

with_none_dfs = []

for year in years:
    rule_df = globals()[f'Rule_{year}_NotUrbanNotWater']
    nlst_stats = globals()[f'NLST{year}_Stats']
    ntl_stats = globals()[f'NTL{year}_Stats']
    ndvi_stats = globals()[f'NDVI{year}_Stats']

    process_data(rule_df, nlst_stats, ntl_stats, ndvi_stats)
    
    urban_df = globals()[f'Rule_{year}_Urban']
    water_df = globals()[f'Rule_{year}_Water']
    with_none_pre = rule_df.append(urban_df, ignore_index=True)
    with_none = with_none_pre.append(water_df, ignore_index=True)
    
    model_plot = with_none[with_none['LABEL'] != 0]
    model = with_none[(with_none['LABEL'] != 0) & (with_none['LABEL'] != 4) & (with_none['LABEL'] != 1)]
    predict = with_none[with_none['LABEL'] == 0]
    
    globals()[f'Rule_{year}_WithNone_Model_Plot'] = model_plot
    globals()[f'Rule_{year}_WithNone_Model'] = model
    globals()[f'Rule_{year}_WithNone_Predict'] = predict
    
    with_none_dfs.append(model)

Rule_Combined_PandR = pd.concat(with_none_dfs, ignore_index=True)
Rule_Combined_PandR_np = np.array(Rule_Combined_PandR)

features = Rule_Combined_PandR_np[:, :-1]
labels = Rule_Combined_PandR_np[:, -1]

# Split the data into training, validation, and testing sets (60% training, 20% validation, 20% testing)
features_train, features_temp, labels_train, labels_temp = train_test_split(features, labels, test_size=0.4, random_state=42)
features_val, features_test, labels_val, labels_test = train_test_split(features_temp, labels_temp, test_size=0.5, random_state=42)

clf = SVC(kernel="rbf")


clf.fit(features_train, labels_train)
val_predictions = clf.predict(features_val)

f2_score_val = f1_score(labels_val, val_predictions, average='macro')
accuracy_val = accuracy_score(labels_val, val_predictions)
recall_val = recall_score(labels_val, val_predictions, pos_label=2)

print("F2 score on validation set:", f2_score_val)
print("Accuracy on validation set:", accuracy_val)
print("Recall on validation set:", recall_val)


combined_features_train = np.concatenate((features_train, features_val))
combined_labels_train = np.concatenate((labels_train, labels_val))
clf.fit(combined_features_train, combined_labels_train)

test_predictions = clf.predict(features_test)

f2_score_test = f1_score(labels_test, test_predictions, average='macro')
accuracy_test = accuracy_score(labels_test, test_predictions)
recall_test = recall_score(labels_test, test_predictions, pos_label=2)

print("F2 score on test set:", f2_score_test)
print("Accuracy on test set:", accuracy_test)
print("Recall on test set:", recall_test)

conf_matrix = confusion_matrix(labels_test, test_predictions)
print("Confusion Matrix:")
print(conf_matrix)

features = Rule_2013_WithNone_Predict[['LAT', 'LON', 'NTL', 'NLST', 'NDVI']]
predictions_2013 = clf.predict(features)
predictions_2013_df = Rule_2013_WithNone_Predict[['LAT', 'LON', 'NTL', 'NLST', 'NDVI']].copy()
predictions_2013_df['LABEL'] = predictions_2013
label_frequency = predictions_2013_df.groupby('LABEL').size()
print(label_frequency)

features = Rule_2020_WithNone_Predict[['LAT', 'LON', 'NTL', 'NLST', 'NDVI']]
predictions_2020 = clf.predict(features)
predictions_2020_df = Rule_2020_WithNone_Predict[['LAT', 'LON', 'NTL', 'NLST', 'NDVI']].copy()
predictions_2020_df['LABEL'] = predictions_2020
label_frequency = predictions_2020_df.groupby('LABEL').size()
print(label_frequency)
