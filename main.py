import numpy as np

# Import files
import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import A_star
import logbook

# Initial variables
requests = read_files.R
open_requests = requests.copy()
closed_requests = []
vehicles = read_files.vehicles
capacities = capacity_vehicles.capacity_matrix(vehicles= vehicles)
assigned_requests = logbook.assigned_requests_matrix(vehicles= vehicles, requests= requests)
E_matrix_All = read_files.E_matrix_All
H_matrix = read_files.H_matrix

# Decision matrices for selecting possible vehicles
time_window_barge = time_windows_3.time_matrix_barge(requests= requests)
time_window_train = time_windows_3.time_matrix_train(requests= requests)
time_window_combined = time_window_train+time_window_barge
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

#Astar requests:
for r in range(len(requests)):
    # if r not in closed_requests:
    if r == 4:
        capacity_check = capacity_vehicles.capacity_check(requests= requests, capacities= capacities, vehicles= vehicles)
        CTE_matrix = OD_matrices.CTE_matrix(E_matrix= E_matrix_All,
                                            vehicles= vehicles,
                                            time_window_matrix= time_window_combined,
                                            request_id= r,
                                            capacity_check= capacity_check)

        traject = A_star.a_star(graph= CTE_matrix,
                               heuristic= H_matrix,
                               start= requests[r][0],
                               goal= requests[r][1])

        used_vehicles = A_star.get_vehicles_from_astar(traject= traject,
                                                    vehicles= vehicles,
                                                    request_id= r,
                                                    time_window_matrix= time_window_combined)



        print(traject)
        print(used_vehicles)