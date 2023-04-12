import matplotlib.pyplot as plt
import matplotlib.cm as cm
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import SpectralClustering, DBSCAN
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


reorder_data("./flare.data1","./newflare.data1")

df = pd.read_csv("./newflare.data1",header=None,names=["0","1","2","3","4","5","6","7","8","9","10","11","12"])


pca = PCA(n_components=3)
pca.fit(df[["3","4","5","6","7","8","9","10","11","12"]])
transformed_data = pca.transform(df[["3","4","5","6","7","8","9","10","11","12"]])
print(f"PCA Eigenvalues:\n{pca.components_}")
print(f"Explained Variance:\n{pca.explained_variance_}")
print(f"Singular Values:\n{pca.singular_values_}")

# print(transformed_data)

#NOTE: Try different assign labels args
clustering = SpectralClustering(n_clusters=3,assign_labels="cluster_qr").fit(transformed_data)
# clustering = DBSCAN(min_samples=3).fit(transformed_data)
# clustering = GaussianMixture(n_components=3).fit(transformed_data)
zipped_data = list(zip(*transformed_data))
zipped_data.append(clustering.labels_)
# zipped_data.append(clustering.means_) # FOR GAUSSIAN
# zipped_data_w_labels = list(zip(zipped_data,clustering.labels_))
# print(clustering)
# print(clustering.labels_)
# for entry in zipped_data_w_labels:
#     print(entry)
print(len(zipped_data[0]))
print(len(zipped_data[1]))
print(len(zipped_data[2]))

fig = plt.figure(1,figsize=(5,5))
plt.clf()

ax = fig.add_subplot(projection="3d")
ax.scatter(zipped_data[0],zipped_data[1],zipped_data[2],c=zipped_data[3],cmap="viridis_r")

# plt.show()