import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA

data_file = pd.read_csv("./car-data/imports-85.data")
data = df(data=data_file)
column_names = [
    "Symboling",
    "Normalized-Losses",
    "Make",
    "Fuel-Type",
    "Aspiration",
    "Num-Of-Doors",
    "Body-Style",
    "Drive-Wheels",
    "Engine-Location",
    "Wheel-Base",
    "Length",
    "Width",
    "Height",
    "Curb-Weight",
    "Engine-Type",
    "Num-Of-Cylinders",
    "Engine-Size",
    "Fuel-System",
    "Bore",
    "Stroke",
    "Compression-Ratio",
    "Horsepower",
    "Peak-RPM",
    "City-MPG",
    "Highway-MPG",
    "Price"
]
data.set_axis(column_names,axis=1,inplace=True)
plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True
# # print(data)

# pca = PCA(n_components=7)
# pca.fit(data[["MYCT","MMIN","MMAX","CACH","CHMIN","CHMAX","PRP"]])
# print(pca.explained_variance_ratio_)
# print(pca.singular_values_)
# city_mpg = data["City-MPG"]
# highway_mpg = data["Highway-MPG"]
# horsepower = data["Horsepower"]
# combined_cols = [[elem[0],elem[1],elem[2]] for elem in [city_mpg,highway_mpg,horsepower]]
# combined_cols = [[int(entry[0]),int(entry[1]),int(entry[2])] for entry in np.dstack((city_mpg,highway_mpg,horsepower))]
# pre_combined_cols = np.dstack((city_mpg,highway_mpg,horsepower))

# for entry in combined_cols:
#     print(entry)

# print(combined_cols)

selected_cols = data[["City-MPG","Highway-MPG","Horsepower"]]
print(selected_cols.head())
# for row in selected_cols:
#     print(row)

# plt.scatter(combined_cols[0],combined_cols[1],combined_cols[2])
# plt.scatter(pre_combined_cols[0],pre_combined_cols[])
# plt.show()