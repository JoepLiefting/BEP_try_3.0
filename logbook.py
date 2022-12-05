import numpy as np
import capacity_vehicles

def assigned_requests_matrix(vehicles, requests):
    vehicles = vehicles
    requests = requests
    assigned_requests = np.zeros([len(vehicles), len(requests)])
    return assigned_requests

def assignment_lowest_capacity(requests, vehicles, capacities, assignments):
    requests = requests
    vehicles = vehicles
    capacities = capacities
    assignments = assignments
    unique_assignments = assignments

    for v in range(len(assignments[0])-1):
        vehicle = assignments[0][v+1]
        request = assignments[1][v+1]
        previous_vehicle = assignments[0][v]
        previous_request = assignments[1][v]

        vehicle_O = vehicles[vehicle][7]
        vehicle_D = vehicles[vehicle][8]
        vehicle_curcap = capacities[vehicle][1]
        previous_vehicle_O = vehicles[previous_vehicle][7]
        previous_vehicle_D = vehicles[previous_vehicle][8]
        previous_vehicle_curcap = capacities[previous_vehicle][1]

        if request == previous_request and vehicle_O == previous_vehicle_O and vehicle_D == previous_vehicle_D:
            if vehicle_curcap >= previous_vehicle_curcap:
                unique_assignments = np.delete(unique_assignments, v, 1)
            else:
                unique_assignments = np.delete(unique_assignments, v+1, 1)

    return unique_assignments


def assign_request_to_vehicle(requests, vehicles, capacities, assignments, assigned_requests):
    requests = requests
    vehicles = vehicles
    capacities = capacities
    assignments = assignments
    assigned_requests = assigned_requests

    for r in range(len(assignments[1])):
        assignment_vehicle = assignments[0][r]
        assignment_request = assignments[1][r]
        capacity_check = capacity_vehicles.capacity_check(requests= requests, capacities= capacities, vehicles= vehicles)

        if capacity_check[assignment_vehicle][assignment_request] == 1 and assigned_requests[assignment_vehicle][assignment_request] != 1:

            capacity_vehicles.update_curcap(requests= requests,
                                          capacities= capacities,
                                          request_id= assignment_request+100000,
                                          vehicle_id= assignment_vehicle)

            assigned_requests[assignment_vehicle][assignment_request] = 1