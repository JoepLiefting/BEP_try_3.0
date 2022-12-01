import numpy as np
import capacity_vehicles

def assigned_requests_matrix(vehicles, requests):
    vehicles = vehicles
    requests = requests
    assigned_requests = np.zeros([len(vehicles), len(requests)])
    return assigned_requests

def assign_request_to_vehicle(requests, capacities, assignments, assigned_requests):

    requests = requests
    capacities = capacities
    assigned_requests = assigned_requests
    assignment_vehicle = assignments[0][0]
    assignment_request = assignments[1][0]

    capacity_vehicles.update_curcap(requests= requests,
                                  capacities= capacities,
                                  request_id= assignment_request+100000,
                                  vehicle_id= assignment_vehicle)

    assigned_requests[assignment_vehicle][assignment_request] = 1