import pandas as pd
import numpy as np
import copy

vehicles_path = "Instances/Vehicles.xlsx"
Vehicles = pd.ExcelFile(vehicles_path)
curcap = pd.read_excel(Vehicles, 'K', usecols=['curcap'])
curcap = curcap.values
print(curcap)

# Voor het oproepen van