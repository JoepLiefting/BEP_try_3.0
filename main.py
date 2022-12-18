import numpy as np

# Import files
import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import A_star
import logbook
import Results

# Initial variables
requests = read_files.R
open_requests = requests.copy()
closed_requests = []
invalid_requests = []
vehicles = read_files.vehicles
capacities = capacity_vehicles.capacity_matrix(vehicles=vehicles)
assigned_requests = logbook.assigned_requests_matrix(vehicles=vehicles, requests=requests)
E_matrix_All = read_files.E_matrix_All
H_matrix = read_files.H_matrix
results_matrix_requests = Results.generate_results_matrix_requests(requests= requests)
trajecten = []
a_star_requests = []
a_star_used_vehicles = []

# Decision matrices for selecting possible vehicles
time_window_barge = time_windows_3.time_matrix_barge(requests=requests)
time_window_train = time_windows_3.time_matrix_train(requests=requests)
time_window_combined = time_window_train + time_window_barge
O_matrix_barge = OD_matrices.O_matrix_barge(requests=requests)
D_matrix_barge = OD_matrices.D_matrix_barge(requests=requests)
O_matrix_train = OD_matrices.O_matrix_train(requests=requests)
D_matrix_train = OD_matrices.D_matrix_train(requests=requests)
capacity_check = capacity_vehicles.capacity_check(requests=requests, capacities=capacities, vehicles=vehicles)

# Compute decision values for each request based on time_window, fixed_vehicle_type and available capacity
direct_routes_barge_check = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)
direct_routes_train_check = capacity_check * time_window_train * ((O_matrix_train * D_matrix_train) + O_matrix_train)

# Assigning direct requests to barges
for r in range(len(requests)):
    for v in range(len(vehicles)):
        direct_routes_barge_check = capacity_check * time_window_barge * (
                (O_matrix_barge * D_matrix_barge) + O_matrix_barge)

        # Possible direct routes barge
        if direct_routes_barge_check[v][r] == 2:
            # Assign requests to vehicles
            assign_direct_routes_barge = logbook.assign_request_to_vehicle(open_requests=open_requests,
                                                                           closed_requests=closed_requests,
                                                                           vehicles=vehicles,
                                                                           capacities=capacities,
                                                                           vehicle_id=v,
                                                                           request_id=r,
                                                                           assigned_requests=assigned_requests)

            if assigned_requests[v][r] == 1 and r not in closed_requests:
                closed_requests.append(r)

# Assigning direct requests to trains
for r in range(len(requests)):
    for v in range(len(vehicles)):
        direct_routes_train_check = capacity_check * time_window_barge * (
                (O_matrix_barge * D_matrix_barge) + O_matrix_barge)

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
            if assigned_requests[v][r] == 1 and r not in closed_requests:
                closed_requests.append(r)

print(closed_requests)

# Astar requests:
for r in range(len(requests)):
    request_id = requests[r][7] - 100000
    used_vehicles = []
    if request_id not in closed_requests:
        capacity_check = capacity_vehicles.capacity_check(requests=requests, capacities=capacities,
                                                          vehicles=vehicles)
        CTE_matrix = OD_matrices.CTE_matrix(E_matrix=E_matrix_All,
                                            vehicles=vehicles,
                                            time_window_matrix=time_window_combined,
                                            request_id=r,
                                            capacity_check=capacity_check)

        traject = A_star.a_star(graph=CTE_matrix,
                                heuristic=H_matrix,
                                start=requests[request_id][0],
                                goal=requests[request_id][1])

        unique_used_vehicles = A_star.get_vehicles_from_astar(traject=traject,
                                                              vehicles=vehicles,
                                                              request_id=r,
                                                              time_window_matrix=time_window_combined)

        trajecten.append(traject)
        a_star_requests.append(request_id)
        a_star_used_vehicles.append(unique_used_vehicles)

        print(request_id)

        # print(unique_used_vehicles)
        for v in range(len(unique_used_vehicles)):
            vehicle_id = int(unique_used_vehicles[v])
            assign_astar_routes = logbook.assign_request_to_vehicle(open_requests=open_requests,
                                                                    closed_requests=closed_requests,
                                                                    vehicles=vehicles,
                                                                    capacities=capacities,
                                                                    vehicle_id=vehicle_id,
                                                                    request_id=request_id,
                                                                    assigned_requests=assigned_requests)

        closed_requests.append(request_id)

#Generate results for statistics

#Put distances in results_matrix
Results.distances_from_assigned(assigned_requests= assigned_requests,
                                vehicles= vehicles,
                                requests= requests,
                                results_matrix_requests= results_matrix_requests)

#Put emissions in results_matrix
Results.emissions_from_assigned(assigned_requests= assigned_requests,
                                vehicles= vehicles,
                                requests= requests,
                                results_matrix_requests= results_matrix_requests,
                                H_matrix= H_matrix)

#Put times in results_matrix
Results.times_from_assigned(assigned_requests= assigned_requests,
                            requests= requests,
                            vehicles= vehicles,
                            results_matrix_requests= results_matrix_requests,
                            trajecten= trajecten,
                            a_star_requests= a_star_requests)