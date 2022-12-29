import numpy as np


def generate_results_matrix_requests(requests):
    results_matrix_requests = np.zeros((len(requests), 11))
    for r in range(len(requests)):
        results_matrix_requests[r][0] = int(requests[r][7])
    return results_matrix_requests


def distances_from_assigned(assigned_requests, requests, vehicles, results_matrix_requests):
    for r in range(len(requests)):
        for v in range(len(vehicles)):
            if assigned_requests[v][r] == 1:
                if vehicles[v][7] == 1:
                    results_matrix_requests[r][1] = results_matrix_requests[r][1] + vehicles[v][15]

                elif vehicles[v][7] == 2:
                    results_matrix_requests[r][2] = results_matrix_requests[r][1] + vehicles[v][15]

                elif vehicles[v][7] == 3:
                    results_matrix_requests[r][3] = results_matrix_requests[r][1] + vehicles[v][15]

    return results_matrix_requests


def emissions_from_assigned(assigned_requests, requests, vehicles, results_matrix_requests, H_matrix):
    for r in range(len(requests)):
        for v in range(len(vehicles)):
            if assigned_requests[v][r] == 1:
                results_matrix_requests[r][9] = results_matrix_requests[r][8] + vehicles[v][14]

        for r in range(len(requests)):
            origin = requests[r][0]
            destination = requests[r][1]
            results_matrix_requests[r][10] = H_matrix[origin][destination]

    return results_matrix_requests


def times_from_assigned(assigned_requests, requests, vehicles, results_matrix_requests, a_star_used_vehicles,
                        a_star_requests):
    for r in range(len(requests)):
        request_id = int(requests[r][7] - 100000)
        for v in range(len(vehicles)):
            if request_id not in a_star_requests and assigned_requests[v][request_id] == 1:
                results_matrix_requests[request_id][4] = vehicles[v][11]
                results_matrix_requests[request_id][5] = vehicles[v][12]

        if request_id in a_star_requests:
            used_vehicle_index = a_star_requests.index(request_id)
            k = 0
            truck_time_before = 0
            while k < len(a_star_used_vehicles[used_vehicle_index]):
                vehicle = int(a_star_used_vehicles[used_vehicle_index][k])
                if vehicles[vehicle][7] != 3:
                    results_matrix_requests[request_id][4] = vehicles[vehicle][11] - truck_time_before
                    k = len(a_star_used_vehicles[used_vehicle_index]) + 1
                elif vehicles[vehicle][7] == 3:
                    truck_time_before += vehicles[vehicle][16]
                    k = k + 1

            i = len(a_star_used_vehicles[used_vehicle_index])
            truck_time_after = 0
            while i > 0:
                vehicle = int(a_star_used_vehicles[used_vehicle_index][i - 1])
                if vehicles[vehicle][7] != 3:
                    results_matrix_requests[request_id][5] = vehicles[vehicle][12] + truck_time_after
                    # print(vehicles[vehicle][11], truck_time_after)
                    i = 0
                elif vehicles[vehicle][7] == 3:
                    truck_time_after += vehicles[vehicle][16]
                    i = i - 1

    return results_matrix_requests


def delay(requests, results_matrix_requests):
    for r in range(len(results_matrix_requests)):
        request_id = int(results_matrix_requests[r][0] - 100000)
        bp = requests[request_id][5]
        results_matrix_requests[request_id][6] = results_matrix_requests[request_id][5] - bp
        if results_matrix_requests[request_id][6] < 0:
            results_matrix_requests[request_id][6] = 0
    return results_matrix_requests


def time_increased(requests, results_matrix_requests, times_trucks):
    for r in range(len(results_matrix_requests)):
        request_id = int(results_matrix_requests[r][0] - 100000)
        origin = requests[request_id][0]
        destination = requests[request_id][1]
        results_matrix_requests[request_id][8] = times_trucks[origin][destination]


def overlap(vehicles, results_matrix_requests, a_star_used_vehicles, a_star_requests):
    for r in range(len(results_matrix_requests)):
        request_id = int(results_matrix_requests[r][0] - 100000)
        current_time = results_matrix_requests[request_id][4]
        if request_id in a_star_requests:
            index = a_star_requests.index(request_id)
            used_vehicles = a_star_used_vehicles[index]
            overlap_var = 0
            for v in range(len(used_vehicles) - 1):
                vehicle = int(used_vehicles[v + 1])
                previous_vehicle = int(used_vehicles[v])
                if vehicles[previous_vehicle][7] != 3:
                    delivery_previous_vehicle = vehicles[previous_vehicle][12]
                    current_time = delivery_previous_vehicle
                    if vehicles[vehicle][7] != 3:
                        pickup_vehicle = vehicles[vehicle][11]
                        if pickup_vehicle < current_time:
                            overlap_var += (current_time - pickup_vehicle)
                        current_time = vehicles[vehicle][12]
                    elif vehicles[vehicle][7] == 3:
                        current_time += vehicles[vehicle][16]

                elif vehicles[previous_vehicle][7] == 3:
                    if vehicles[vehicle][7] != 3:
                        pickup_vehicle = vehicles[vehicle][11]
                        if pickup_vehicle < current_time:
                            overlap_var += (current_time - pickup_vehicle)
                        current_time = vehicles[vehicle][12]
                    elif vehicles[vehicle][7] == 3:
                        current_time += vehicles[vehicle][16]

            results_matrix_requests[request_id][7] = overlap_var

    return results_matrix_requests
