import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pandas import DataFrame as df
from sklearn.decomposition import PCA

data_file = pd.read_csv("./car-data/imports-85.data")
data = df(data=data_file)
column_names = [
    "Symboling",
    "NormalizedLosses",
    "Make",
    "FuelType",
    "Aspiration",
    "NumOfDoors",
    "BodyStyle",
    "DriveWheels",
    "EngineLocation",
    "WheelBase",
    "Length",
    "Width",
    "Height",
    "CurbWeight",
    "EngineType",
    "NumOfCylinders",
    "EngineSize",
    "FuelSystem",
    "Bore",
    "Stroke",
    "CompressionRatio",
    "Horsepower",
    "PeakRPM",
    "CityMPG",
    "HighwayMPG",
    "Price"
]
data.set_axis(column_names,axis=1,inplace=True)

# DROP INVALID COLUMNS
data = data[
    (data.NormalizedLosses != "?") &
    (data.NumOfDoors != "?") &
    (data.Bore != "?") &
    (data.Stroke != "?") &
    (data.Horsepower != "?") &
    (data.PeakRPM != "?") &
    (data.Price != "?")
    ]

plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True
print(data.to_string())
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

# selected_cols = data[["City-MPG","Highway-MPG","Horsepower"]]
# string_data = selected_cols.to_string()
# print(string_data)

# plt.scatter(data["City-MPG"],data["Highway-MPG"],data["Horsepower"])
# plt.scatter(selected_cols[0],selected_cols[1])
# plt.show()

# plt.scatter(combined_cols[0],combined_cols[1],combined_cols[2])
# plt.scatter(pre_combined_cols[0],pre_combined_cols[])
# plt.show()