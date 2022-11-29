import read_files
import numpy as np

def time_matrix_barge(requests):

    vehicles = read_files.vehicles
    time_window_check_barge = np.zeros([len(vehicles), len(requests)])
    requests = requests

    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_bp = vehicles[v][11]
            vehicle_ad = vehicles[v][12]
            vehicle_type = vehicles[v][7]

            request_ap = requests[r][2]
            request_bd = requests[r][5]

            if vehicle_type == 1:
                if vehicle_bp > request_ap and vehicle_ad < request_bd:

                    time_window_check_barge[v][r] = 1

    return time_window_check_barge

def time_matrix_train(requests):

    vehicles = read_files.vehicles
    time_window_check_train = np.zeros([len(vehicles), len(requests)])
    requests = requests

    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_bp = vehicles[v][11]
            vehicle_ad = vehicles[v][12]
            vehicle_type = vehicles[v][7]

            request_ap = requests[r][2]
            request_bd = requests[r][5]

            if vehicle_type == 2:
                if vehicle_bp > request_ap and vehicle_ad < request_bd:

                    time_window_check_train[v][r] = 1

    return time_window_check_train