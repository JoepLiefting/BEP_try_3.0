import numpy as np

import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import logbook

requests = read_files.R
open_requests = requests
vehicles = read_files.vehicles
capacities = capacity_vehicles.capacity_matrix(vehicles= vehicles)
assigned_requests = logbook.assigned_requests_matrix(vehicles= vehicles, requests= requests)

time_window_barge = time_windows_3.time_matrix_barge(requests= requests)
time_window_train = time_windows_3.time_matrix_train(requests= requests)

O_matrix_barge = OD_matrices.O_matrix_barge(requests= requests)
D_matrix_barge = OD_matrices.D_matrix_barge(requests= requests)
O_matrix_train = OD_matrices.O_matrix_train(requests= requests)
D_matrix_train = OD_matrices.D_matrix_train(requests= requests)

capacity_check = capacity_vehicles.capacity_check(requests= requests, capacities= capacities, vehicles= vehicles)

suitable_routes_barge = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)
suitable_routes_train = capacity_check * time_window_train * ((O_matrix_train * D_matrix_train) + O_matrix_train)

direct_routes_barge = np.where(suitable_routes_barge == 2)

assign_direct_routes_barge = logbook.assign_request_to_vehicle(requests= requests,
                                                               capacities= capacities,
                                                               assignments= direct_routes_barge,
                                                               assigned_requests= assigned_requests)


