import numpy as np
import pandas as pd
import csv
import matplotlib.pyplot as plt
from io import BytesIO
from PIL import Image
from mpl_toolkits.basemap import Basemap

# import seaborn as sns
# from descartes import PolygonPatch
import matplotlib.pyplot as plt
# import shapefile
import pandas as pd

import os

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))
df = pd.read_excel('all_features_2020.xlsx')

print(df.head())
print(df.describe())