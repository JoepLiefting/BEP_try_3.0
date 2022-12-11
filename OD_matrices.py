import read_files
import numpy as np
import time_windows_3
import capacity_vehicles

def O_matrix_barge(requests):

    vehicles = read_files.vehicles
    requests = requests
    O_check_barge = np.zeros([len(vehicles), len(requests)])


    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_type = vehicles[v][7]
            vehicle_origin = vehicles[v][8]

            request_origin = requests[r][0]

            if vehicle_type == 1:
                if vehicle_origin == request_origin:

                    O_check_barge[v][r] = 1

    return O_check_barge


def D_matrix_barge(requests):

    vehicles = read_files.vehicles
    requests = requests
    D_check_barge = np.zeros([len(vehicles), len(requests)])


    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_type = vehicles[v][7]
            vehicle_destination = vehicles[v][9]

            request_destination = requests[r][1]

            if vehicle_type == 1:
                if vehicle_destination == request_destination:

                    D_check_barge[v][r] = 1

    return D_check_barge


def O_matrix_train(requests):

    vehicles = read_files.vehicles
    requests = requests
    O_check_train = np.zeros([len(vehicles), len(requests)])


    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_type = vehicles[v][7]
            vehicle_origin = vehicles[v][8]

            request_origin = requests[r][0]

            if vehicle_type == 2:
                if vehicle_origin == request_origin:

                    O_check_train[v][r] = 1

    return O_check_train


def D_matrix_train(requests):

    vehicles = read_files.vehicles
    requests = requests
    D_check_train = np.zeros([len(vehicles), len(requests)])


    for v in range(len(vehicles)):
        for r in range(len(requests)):
            vehicle_type = vehicles[v][7]
            vehicle_destination = vehicles[v][9]

            request_destination = requests[r][1]

            if vehicle_type == 2:
                if vehicle_destination == request_destination:

                    D_check_train[v][r] = 1

    return D_check_train


def available_routes_matrix(E_matrix, vehicles, time_window_matrix, request_id, capacity_check):
    available_barges = []
    available_trains = []
    T_E_matrix = E_matrix.copy()

# T_E_matrix voor barges
    for v in range(len(vehicles)):
        if vehicles[v][7] == 1:
            if time_window_matrix[v][request_id] == 1 and capacity_check[v][request_id] == 1:
                available_barges.append(v)

    barge_origins = []
    barge_destinations = []

    for v in range(len(available_barges)):
        vehicle_id = available_barges[v]
        barge_O = vehicles[vehicle_id][8]
        barge_D = vehicles[vehicle_id][9]
        barge_origins.append(int(barge_O))
        barge_destinations.append(int(barge_D))

    for i in range(9):
        for j in range(9):
            if i != j:
                T_E_matrix[i][j] = 0

    for i in range(len(barge_origins)):
        if len(barge_origins) != 0:
            barge_origin = int(barge_origins[i])
            barge_destination = int(barge_destinations[i])
            T_E_matrix[barge_origin][barge_destination] = E_matrix[barge_origin][barge_destination]
            T_E_matrix[barge_destination][barge_origin] = E_matrix[barge_destination][barge_origin]

# T_E_matrix voor trains
    for v in range(len(vehicles)):
        if vehicles[v][7] == 2:
            if time_window_matrix[v][request_id] == 1 and capacity_check[v][request_id] == 1:
                available_trains.append(v)

    train_origins = []
    train_destinations = []

    for v in range(len(available_trains)):
        vehicle_id = available_trains[v]
        train_O = vehicles[vehicle_id][8]
        train_D = vehicles[vehicle_id][9]
        train_origins.append(int(train_O))
        train_destinations.append(int(train_D))

    for i in range(9):
        for j in range(9):
            if i != j:
                T_E_matrix[i + 10][j + 10] = 0

    for i in range(len(train_origins)):
        if len(train_origins) != 0:
            train_origin = int(train_origins[i])
            train_destination = int(train_destinations[i])
            T_E_matrix[train_origin][train_destination] = E_matrix[train_origin][train_destination]
            T_E_matrix[train_destination][train_origin] = E_matrix[train_destination][train_origin]

    return T_E_matrix





E_matrix = read_files.E_matrix_All
vehicles = read_files.vehicles
requests = read_files.R
time_window_matrix = time_windows_3.time_matrix_barge(requests= requests)+time_windows_3.time_matrix_train(requests= requests)
capacities = capacity_vehicles.capacity_matrix(vehicles= vehicles)
capacity_check = capacity_vehicles.capacity_check(requests= requests, capacities= capacities, vehicles= vehicles)

T_E_matrix = available_routes_matrix(E_matrix= E_matrix,
                                     vehicles= vehicles,
                                     time_window_matrix= time_window_matrix,
                                     request_id= 4,
                                     capacity_check= capacity_check)

