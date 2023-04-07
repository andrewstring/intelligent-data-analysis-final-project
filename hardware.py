import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler

data_file = pd.read_csv("./hardware-data/machine.data")
data = df(data=data_file)
column_names = [
    "Vendor-Name",
    "Model-Name",
    "MYCT",
    "MMIN",
    "MMAX",
    "CACH",
    "CHMIN",
    "CHMAX",
    "PRP",
    "ERP",
]
data.set_axis(column_names,axis=1,inplace=True)

# scaled_data = StandardScaler().fit_transform(data)
scaled_data = StandardScaler().fit_transform(data[["MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP"]])
# print(scaled_data)
pca = PCA(n_components=2)
pca.fit(scaled_data)
print(pca.components_)


# plt.rcParams["figure.figsize"] = [7.00,3.50]
# plt.rcParams["figure.autolayout"] = True
# # print(data)

# pca = PCA(n_components=2)
# pca.fit(data[["MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP"]])
# print(pca.components_)
