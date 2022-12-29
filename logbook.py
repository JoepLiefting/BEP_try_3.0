import numpy as np
import capacity_vehicles


def assigned_requests_matrix(vehicles, requests):
    vehicles = vehicles
    requests = requests
    assigned_requests = np.zeros([len(vehicles), len(requests)])
    return assigned_requests


def assignment_lowest_capacity(vehicles, capacities, assignments, time_window_matrix):
    unique_assignments = assignments.copy()

    for v in range(len(assignments[0]) - 1):
        vehicle = assignments[0][v + 1]
        request = assignments[1][v + 1]
        previous_vehicle = assignments[0][v]
        previous_request = assignments[1][v]

        vehicle_O = vehicles[vehicle][8]
        vehicle_D = vehicles[vehicle][9]
        vehicle_curcap = capacities[vehicle][1]
        previous_vehicle_O = vehicles[previous_vehicle][8]
        previous_vehicle_D = vehicles[previous_vehicle][9]
        previous_vehicle_curcap = capacities[previous_vehicle][1]

        if request == previous_request and vehicle_O == previous_vehicle_O and vehicle_D == previous_vehicle_D:
            if vehicle_curcap >= previous_vehicle_curcap:
                unique_assignments = np.delete(unique_assignments, v, 1)
            else:
                unique_assignments = np.delete(unique_assignments, v + 1, 1)

    return unique_assignments


def assign_request_to_vehicle(open_requests, closed_requests, vehicles, capacities, vehicle_id, request_id,
                              assigned_requests, time_window):
    assignment_request = request_id
    assignment_vehicle = vehicle_id
    capacity_check = capacity_vehicles.capacity_check(requests=open_requests, capacities=capacities, vehicles=vehicles)

    if capacity_check[assignment_vehicle][assignment_request] == 1 and assigned_requests[assignment_vehicle][
        assignment_request] != 1 and assignment_request not in closed_requests:
        capacity_vehicles.update_curcap(requests=open_requests,
                                        capacities=capacities,
                                        request_id=assignment_request + 100000,
                                        vehicle_id=assignment_vehicle)

        assigned_requests[assignment_vehicle][assignment_request] = 1

    return assigned_requests


def assignment_check(requests, vehicles, assigned_requests):
    wrong_requests = []
    for r in range(len(requests)):
        request_id = requests[r][7] - 100000
        som = 0
        for v in range(len(vehicles)):
            if assigned_requests[v][request_id] == 1:
                som += 1
        if som == 0:
            wrong_requests.append(request_id)

    return wrong_requests
