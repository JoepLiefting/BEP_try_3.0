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


def times_from_assigned(assigned_requests, requests, vehicles, results_matrix_requests, trajecten, a_star_requests):
    for r in range(len(requests)):
        for v in range(len(vehicles)):
            request_id = requests[r][7] - 100000
            if request_id not in a_star_requests and assigned_requests[v][request_id] == 1:
                results_matrix_requests[request_id][4] = vehicles[v][11]
                results_matrix_requests[request_id][5] = vehicles[v][12]

            elif request_id in a_star_requests and assigned_requests[v][request_id] == 1:
                traject_index = a_star_requests.index(request_id)
                for t in range(len(trajecten[traject_index])-1):
                    vehicle = trajecten[traject_index][t+1]
                    previous_vehicle = trajecten[traject_index][t]

    return results_matrix_requests
