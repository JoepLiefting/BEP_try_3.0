import read_files
import numpy as np
import time_windows_3

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


def available_routes_matrix(E_matrix, vehicles, time_window_matrix, request_id):
    available_vehicles = []
    T_E_matrix = E_matrix


    for v in range(len(vehicles)):
        if time_window_matrix[v][request_id] == 1:
            available_vehicles.append(v)

    origins = []
    destinations = []

    for v in range(len(available_vehicles)):
        vehicle_id = available_vehicles[v]
        vehicle_O = vehicles[vehicle_id][8]
        vehicle_D = vehicles[vehicle_id][9]
        origins.append(int(vehicle_O))
        destinations.append(int(vehicle_D))

    print(E_matrix[0][3])
    for i in range(0, 9):
        for j in range(0, 9):
            if i != j:
                T_E_matrix[i][j] = 0

    print(E_matrix[0][3])

    for i in range(len(origins)):
        if len(origins) != 0:
            origin = int(origins[i])
            destination = int(destinations[i])
            T_E_matrix[origin][destination] = E_matrix[origin][destination]

    return T_E_matrix

E_matrix = read_files.E_matrix_All
vehicles = read_files.vehicles
requests = read_files.R
time_window_matrix = time_windows_3.time_matrix_barge(requests= requests)


T_E_matrix = available_routes_matrix(E_matrix= E_matrix,
                                     vehicles= vehicles,
                                     time_window_matrix= time_window_matrix,
                                     request_id= 4)

