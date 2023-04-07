import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
import os.path

def reorder_data(in_file_path,out_file_path):
    if not os.path.isfile(out_file_path):
        with open(out_file_path, "w+") as write:
            with open(in_file_path, "r") as read:
                file_lines = read.readlines()
                for line in file_lines:
                    if not line[0] == "*":
                        write.write(line.replace(" ",","))


reorder_data("./flare-data/flare.data1","./flare-data/newflare.data1")

df = pd.read_csv("./flare-data/newflare.data1",header=None,names=["0","1","2","3","4","5","6","7","8","9","10","11","12"])

pca = PCA(n_components=2)
pca.fit(df[["3","4","5","6","7","8","9","10","11","12"]])
transformed_data = pca.transform(df[["3","4","5","6","7","8","9","10","11","12"]])
zipped_data = list(zip(*transformed_data))
# print(transformed_data)

fig = plt.figure(1,figsize=(5,5))
plt.clf()

ax = fig.add_subplot()
ax.scatter(zipped_data[0],zipped_data[1])

# plt.scatter(transformed_data[0],transformed_data[1])
plt.show()