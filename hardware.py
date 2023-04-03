import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA

data = pd.read_csv("./data/breast-cancer.data")
dataframe = df(data=data)
column_names = [
    "Class",
    "Age",
    "Menopause",
    "Tumor-Size",
    "Inv-Nodes",
    "Node-Caps",
    "Deg-Malig",
    "Breast",
    "Breast-Quad",
    "Irradiat"
]
dataframe.set_axis(column_names,axis=1,inplace=True)
plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True
# print(data)

pca = PCA(n_components=2)
pca.fit([dataframe["Age"],dataframe["Tumor-Size"]])