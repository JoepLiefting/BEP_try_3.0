import read_files
import numpy as np

vehicles = read_files.vehicles
requests = read_files.R
O_check_barge = np.zeros([len(vehicles), len(requests)])
D_check_barge = np.zeros([len(vehicles), len(requests)])
O_check_train = np.zeros([len(vehicles), len(requests)])
D_check_train = np.zeros([len(vehicles), len(requests)])


for v in range(len(vehicles)):
    for r in range(len(requests)):
        vehicle_id = vehicles[v][0]
        vehicle_ap = vehicles[v][10]
        vehicle_bp = vehicles[v][11]
        vehicle_ad = vehicles[v][12]
        vehicle_bd = vehicles[v][13]
        vehicle_type = vehicles[v][7]
        vehicle_origin = vehicles[v][8]
        vehicle_destination = vehicles[v][9]

        request_id = requests[r][7]
        request_ap = requests[r][2]
        request_bp = requests[r][3]
        request_ad = requests[r][4]
        request_bd = requests[r][5]
        request_origin = requests[r][0]
        request_destination = requests[r][1]

        if vehicle_type == 1:
            if vehicle_origin == request_origin:

                O_check_barge[v][r] = 1

        if vehicle_type == 1:
            if vehicle_destination == request_destination:

                D_check_barge[v][r] = 1

        if vehicle_type == 2:
            if vehicle_origin == request_origin:

                O_check_train[v][r] = 1

        if vehicle_type == 2:
            if vehicle_destination == request_destination:

                D_check_train[v][r] = 1