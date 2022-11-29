import read_files
import numpy as np

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