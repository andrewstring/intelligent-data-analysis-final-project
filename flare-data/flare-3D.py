import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import SpectralClustering, DBSCAN, KMeans
from sklearn.mixture import GaussianMixture
import os.path

def reorder_data(in_file_path,out_file_path):
    if not os.path.isfile(out_file_path):
        with open(out_file_path, "w+") as write:
            with open(in_file_path, "r") as read:
                file_lines = read.readlines()
                for line in file_lines:
                    if not line[0] == "*":
                        write.write(line.replace(" ",","))

def get_choice():
    choice = 0
    while not (choice == "1" or choice == "2"):
        choice = input("Enter 1 or 2 to run dataset 1 or dataset 2: ")
    choice = int(choice)
    return choice


reorder_data("./flare.data1","./newflare.data1")
reorder_data("./flare.data2","./newflare.data2")

choice = get_choice()

pca = PCA(n_components=3)

if choice == 1:
    df = pd.read_csv("./newflare.data1",header=None,names=["0","1","2","3","4","5","6","7","8","9","10","11","12"])
    pca.fit(df[["3","4","5","6","7","8","9","10","11","12"]])
    transformed_data = pca.transform(df[["3","4","5","6","7","8","9","10","11","12"]])


elif choice == 2:
    df2 = pd.read_csv("./newflare.data2",header=None,names=["0","1","2","3","4","5","6","7","8","9","10","11","12"])
    pca.fit(df2[["3","4","5","6","7","8","9","10","11","12"]])
    transformed_data = pca.transform(df2[["3","4","5","6","7","8","9","10","11","12"]])

print(f"PCA Eigenvalues:\n{pca.components_}")
print(f"Explained Variance:\n{pca.explained_variance_}")
print(f"Singular Values:\n{pca.singular_values_}")

clustering = SpectralClustering(n_clusters=3,assign_labels="cluster_qr").fit(transformed_data)
zipped_data = list(zip(*transformed_data))
zipped_data.append(clustering.labels_)

fig = plt.figure(1,figsize=(5,5))
plt.clf()

ax = fig.add_subplot(projection="3d")
ax.scatter(zipped_data[0],zipped_data[1],zipped_data[2],c=zipped_data[3],cmap="viridis_r")

plt.show()