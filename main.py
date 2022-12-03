import numpy as np

# Import files
import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import logbook

# Initial variables
requests = read_files.R
open_requests = requests
vehicles = read_files.vehicles
capacities = capacity_vehicles.capacity_matrix(vehicles= vehicles)
assigned_requests = logbook.assigned_requests_matrix(vehicles= vehicles, requests= requests)

# Decision matrices for selecting possible vehicles
time_window_barge = time_windows_3.time_matrix_barge(requests= requests)
time_window_train = time_windows_3.time_matrix_train(requests= requests)
O_matrix_barge = OD_matrices.O_matrix_barge(requests= requests)
D_matrix_barge = OD_matrices.D_matrix_barge(requests= requests)
O_matrix_train = OD_matrices.O_matrix_train(requests= requests)
D_matrix_train = OD_matrices.D_matrix_train(requests= requests)
capacity_check = capacity_vehicles.capacity_check(requests= requests, capacities= capacities, vehicles= vehicles)

# Compute decision values for each request based on time_window, fixed_vehicle_type and available capacity
suitable_routes_barge = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)
suitable_routes_train = capacity_check * time_window_train * ((O_matrix_train * D_matrix_train) + O_matrix_train)

# Assigning request with direct OD to barge
direct_routes_barge = np.asarray(np.where(suitable_routes_barge == 2))

unique_assignments = logbook.assignment_lowest_capacity(requests= requests,
                                                        vehicles= vehicles,
                                                        capacities= capacities,
                                                        assignments= direct_routes_barge)

assign_direct_routes_barge = logbook.assign_request_to_vehicle(requests= requests,
                                                               vehicles= vehicles,
                                                               capacities= capacities,
                                                               assignments= unique_assignments,
                                                               assigned_requests= assigned_requests)