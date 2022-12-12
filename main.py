import numpy as np

# Import files
import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import logbook

# Initial variables
requests = read_files.R
open_requests = requests.copy()
closed_requests = []
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
direct_routes_barge_check = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)
direct_routes_train_check = capacity_check * time_window_train * ((O_matrix_train * D_matrix_train) + O_matrix_train)

#Assigning direct requests to barges
for r in range(len(requests)):
    for v in range(len(vehicles)):
        direct_routes_barge_check = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)

        #Possible direct routes barge
        if direct_routes_barge_check[v][r] == 2:

            # Assign requests to vehicles
            assign_direct_routes_barge = logbook.assign_request_to_vehicle(open_requests= open_requests,
                                                                           closed_requests= closed_requests,
                                                                           vehicles= vehicles,
                                                                           capacities= capacities,
                                                                           vehicle_id= v,
                                                                           request_id= r,
                                                                           assigned_requests= assigned_requests)
#Assigning direct requests to trains
for r in range(len(requests)):
    for v in range(len(vehicles)):
        direct_routes_train_check = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)

        # Possible direct routes train
        if direct_routes_train_check[v][r] == 2:
            # Assign requests to vehicles
            assign_direct_routes_train = logbook.assign_request_to_vehicle(open_requests=open_requests,
                                                                           closed_requests=closed_requests,
                                                                           vehicles=vehicles,
                                                                           capacities=capacities,
                                                                           vehicle_id=v,
                                                                           request_id=r,
                                                                           assigned_requests=assigned_requests)

#Astar assignments:....
# for r in range(len(requests)) and not in closed_requests:
#     CTE_matrix =