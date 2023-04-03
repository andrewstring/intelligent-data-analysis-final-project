import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA

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
plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True
print(data)

pca = PCA(n_components=3)
pca.fit(data[["MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP"]])
# pca.fit(data["MYCT"],data["MMIN"],data["MMAX"],)