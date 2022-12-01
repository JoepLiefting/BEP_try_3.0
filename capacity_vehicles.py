import pandas as pd
import numpy as np
import read_files
import time_windows_3

vehicles = read_files.vehicles
current_cap = np.zeros([len(vehicles), 2])

for k in range(len(current_cap)):
    current_cap[k][0] = vehicles[k][1]
    current_cap[k][1] = vehicles[k][2]

def capacity_check(requests):

    requests = requests
    capacity_check = np.zeros([len(vehicles), len(requests)])

    for v in range(len(vehicles)):
        for r in range(len(requests)):
            curcap = current_cap[v][1]
            request_qr = requests[r][6]

            if request_qr <= curcap:
                capacity_check[v][r] = 1

    return  capacity_check



