import numpy as np
import read_files

def capacity_matrix(vehicles):

    vehicles = vehicles
    capacities = np.zeros([len(vehicles), 2])

    for k in range(len(capacities)):
        capacities[k][0] = vehicles[k][1]
        capacities[k][1] = vehicles[k][2]

    return capacities

def capacity_check(requests, capacities, vehicles):

    requests = requests
    capacities = capacities
    capacity_check = np.zeros([len(vehicles), len(requests)])
    vehicles = vehicles

    for v in range(len(vehicles)):
        for r in range(len(requests)):
            curcap = capacities[v][1]
            request_qr = requests[r][6]

            if request_qr <= curcap:
                capacity_check[v][r] = 1

    return  capacity_check


def update_curcap(requests, capacities, request_id, vehicle_id):
    requests = requests
    capacities = capacities
    request_id = request_id
    vehicle_id = vehicle_id
    request_index = request_id-100000

    quantity = requests[request_index][6]

    capacities[vehicle_id][1] = capacities[vehicle_id][1]-quantity

    return capacities

