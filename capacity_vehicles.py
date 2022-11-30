import pandas as pd
import numpy as np
import read_files
import time_windows_2
import main

suitable_routes_barge = main.suitable_routes_barge
suitable_routes_train = main.suitable_routes_train


def current_capacity(requests):

    vehicles = read_files.vehicles
    current_cap = np.zeros([len(vehicles), 1])
    # current_cap = pd.read_excel(Vehicles, 'K', usecols=['curcap'])
    # current_cap = current_cap.values
    requests = requests

    for v in range(len(vehicles)):
        for r in range(len(requests)):
            curcap = vehicles[v][2]
            maxcap = vehicles[v][1]

            request_qr = requests[r][6]

            if vehicle gekozen dan
                if (curcap - request_qr) > maxcap

                        current_cap = curcap - request_qr
                        print(waggie nr... is gegaan)
                else
                    andere vehicle vinden

    return current_cap




