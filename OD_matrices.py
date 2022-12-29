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


def CTE_matrix(E_matrix, vehicles, time_window_matrix, request_id, capacity_check):
    available_barges = []
    available_trains = []
    T_E_matrix = E_matrix.copy()

    for i in range(30):
        for j in range(30):
            if i == j:
                T_E_matrix[i][j] = 0

    # T_E_matrix voor barges met capacites
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

    for i in range(10):
        for j in range(10):
            T_E_matrix[i][j] = 0
            T_E_matrix[i][j + 10] = 0
            T_E_matrix[i][j + 20] = 0
            T_E_matrix[i + 10][j] = 0
            T_E_matrix[i + 20][j] = 0

    for i in range(len(barge_origins)):
        if len(barge_origins) != 0:
            barge_origin = int(barge_origins[i])
            barge_destination = int(barge_destinations[i])
            T_E_matrix[barge_origin][barge_destination] = E_matrix[barge_origin][barge_destination]
            T_E_matrix[barge_destination][barge_origin] = E_matrix[barge_destination][barge_origin]

    C_T_E_matrix = T_E_matrix.copy()
    # T_E_matrix voor trains met capacities
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

    for i in range(10):
        for j in range(10):
            C_T_E_matrix[i + 10][j + 10] = 0
            C_T_E_matrix[i + 10][j + 20] = 0
            C_T_E_matrix[i + 20][j + 10] = 0

    for i in range(len(train_origins)):
        if len(train_origins) != 0:
            train_origin = int(train_origins[i] + 10)
            train_destination = int(train_destinations[i] + 10)
            C_T_E_matrix[train_origin][train_destination] = T_E_matrix[train_origin][train_destination]
            C_T_E_matrix[train_destination][train_origin] = T_E_matrix[train_destination][train_origin]

    # Train barge connections
    for i in range(10):
        C_T_E_matrix[i + 10][i] = 0.1
        C_T_E_matrix[i + 20][i] = 0.1
        C_T_E_matrix[i][i + 10] = 0.1
        C_T_E_matrix[i][i + 20] = 0.1
        C_T_E_matrix[i + 10][i + 20] = 0.1
        C_T_E_matrix[i + 20][i + 10] = 0.1

    return C_T_E_matrix


def CTE2_matrix(E_matrix, vehicles, time_window_matrix, request_id, capacity_check):
    available_barges = []
    available_trains = []
    T_E_matrix = E_matrix.copy()

    for i in range(30):
        for j in range(30):
            if i == j:
                T_E_matrix[i][j] = 0

    # T_E_matrix voor barges met capacites
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

    for i in range(10):
        for j in range(10):
            T_E_matrix[i][j] = 0
            T_E_matrix[i][j + 10] = 0
            T_E_matrix[i][j + 20] = 0
            T_E_matrix[i + 10][j] = 0
            T_E_matrix[i + 20][j] = 0

    for i in range(len(barge_origins)):
        if len(barge_origins) != 0:
            barge_origin = int(barge_origins[i])
            barge_destination = int(barge_destinations[i])
            T_E_matrix[barge_origin][barge_destination] = E_matrix[barge_origin][barge_destination]
            T_E_matrix[barge_destination][barge_origin] = E_matrix[barge_destination][barge_origin]

            T_E_matrix[barge_origin + 20][barge_origin] = 0.1
            T_E_matrix[barge_origin][barge_origin + 20] = 0.1
            T_E_matrix[barge_destination][barge_destination + 20] = 0.1
            T_E_matrix[barge_destination + 20][barge_destination] = 0.1

    C_T_E_matrix = T_E_matrix.copy()
    # T_E_matrix voor trains met capacities
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

    for i in range(10):
        for j in range(10):
            C_T_E_matrix[i + 10][j + 10] = 0
            C_T_E_matrix[i + 10][j + 20] = 0
            C_T_E_matrix[i + 20][j + 10] = 0

    for i in range(len(train_origins)):
        if len(train_origins) != 0:
            train_origin = int(train_origins[i] + 10)
            train_destination = int(train_destinations[i] + 10)
            C_T_E_matrix[train_origin][train_destination] = T_E_matrix[train_origin][train_destination]
            C_T_E_matrix[train_destination][train_origin] = T_E_matrix[train_destination][train_origin]

            C_T_E_matrix[train_origin + 10][train_origin] = 0.1
            C_T_E_matrix[train_origin][train_origin + 10] = 0.1
            C_T_E_matrix[train_destination][train_destination + 10] = 0.1
            C_T_E_matrix[train_destination + 10][train_destination] = 0.1

    # Train barge connections
    for i in range(10):
        if C_T_E_matrix[i + 20][i] == 0.1 and C_T_E_matrix[i + 20][i + 10] == 0.1:
            C_T_E_matrix[i + 10][i] = 0.1
            C_T_E_matrix[i][i + 10] = 0.1

    return C_T_E_matrix


def CTE_matrix_update(CTE_matrix, vehicles, current_time):
    CTE_updated = CTE_matrix.copy()

    # Barges
    for i in range(10):
        for j in range(10):
            if CTE_matrix[i][j] != 0:
                k = 0
                while k < len(vehicles):
                    if vehicles[k][8] == i and vehicles[k][9] == j and vehicles[k][7] == 1 and vehicles[k][
                        10] >= current_time:
                        CTE_updated[i][j] = CTE_matrix[i][j]
                        CTE_updated[j][i] = CTE_matrix[j][i]
                        k = len(vehicles) + 1
                    else:
                        CTE_updated[i][j] = 0
                        CTE_updated[j][i] = 0
                        k += 1

        # Trains
        for i in range(10):
            for j in range(10):
                if CTE_matrix[i + 10][j + 10] != 0:
                    k = 0
                    while k < len(vehicles):
                        if vehicles[k][8] == i and vehicles[k][9] == j and vehicles[k][7] == 1 and vehicles[k][
                            10] >= current_time:
                            CTE_updated[i + 10][j + 10] = CTE_matrix[i + 10][j + 10]
                            CTE_updated[j + 10][i + 10] = CTE_matrix[j + 10][i + 10]
                            k = len(vehicles) + 1
                        else:
                            CTE_updated[i + 10][j + 10] = 0
                            CTE_updated[j + 10][i + 10] = 0
                            k += 1

    return CTE_updated


