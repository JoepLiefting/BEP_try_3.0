import pandas as pd
import numpy as np
import read_files
import time_windows_3


# suitable_routes_barge = time_window_barge * (time_window_barge + O_matrix_barge * D_matrix_barge)
# suitable_routes_train = time_window_train * (time_window_train + O_matrix_train * D_matrix_train)


# def current_capacity(requests):

vehicles = read_files.vehicles
requests = read_files.R
current_cap = np.zeros([len(vehicles), 2])

capacity_check = np.zeros([len(vehicles), len(requests)])

for k in range(len(current_cap)):
    current_cap[k][0] = vehicles[k][1]
    current_cap[k][1] = vehicles[k][2]


for v in range(len(vehicles)):
    for r in range(len(requests)):
        curcap = vehicles[v][2]
        maxcap = vehicles[v][1]

        request_qr = requests[r][6]

        if request_qr <= curcap:
            curcap = curcap - request_qr
            capacity_check[v][r] = 1




