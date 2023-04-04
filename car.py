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

print(data[["CityMPG","HighwayMPG","PeakRPM"]])

plt.scatter(data["CityMPG"],data["HighwayMPG"],data["DriveWheels"])
plt.show()