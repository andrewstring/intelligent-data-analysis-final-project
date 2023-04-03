import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = pd.read_csv("./data/breast-cancer.data")
plt.rcParams["figure.figsize"] = [7.00,3.50]
plt.rcParams["figure.autolayout"] = True
print(data)