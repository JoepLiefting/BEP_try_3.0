import numpy as np

# Import files
import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles
import A_star
import A_star_time
import logbook
import Results
import random


def total_emissions(vehicles):
    # Requests die errors geven
    vervelend_5 = [4, 5]
    vervelend_10 = []  # leeg
    vervelend_20 = [12]
    vervelend_30 = []  # leeg
    vervelend_50 = [24, 36]
    vervelend_100 = [10, 12, 45, 80, 82, 87]
    vervelend_200 = [6, 9, 11, 23, 39, 48, 68, 74, 128, 134, 150, 164]
    vervelend_400 = [20, 62, 87, 120, 134, 153, 174, 176, 197, 234, 236, 239, 262, 278, 305, 308, 316, 318, 339, 345,
                     347,
                     348, 351, 369, 381, 399]
    # number of requests, it can be 5, 10, 20, 30, 50, 100, 200, 400, 700, 1000, 1300, 1600
    vervelend = []

    # Initial variables
    requests = read_files.R
    open_requests = requests.copy()
    closed_requests = []
    invalid_requests = []
    capacities = capacity_vehicles.capacity_matrix(vehicles=vehicles)
    assigned_requests = logbook.assigned_requests_matrix(vehicles=vehicles, requests=requests)
    E_matrix_All = read_files.E_matrix_All
    H_matrix = read_files.H_matrix
    results_matrix_requests = Results.generate_results_matrix_requests(requests=requests)
    trajecten = []
    a_star_requests = []
    a_star_used_vehicles = []
    a_star_runs_all = []
    times_trucks = read_files.T[100]
    timed_out_requests = []
    total_emissions = 0

    # Decision matrices for selecting possible vehicles
    time_window_barge = time_windows_3.time_matrix_barge(requests=requests)
    time_window_train = time_windows_3.time_matrix_train(requests=requests)
    time_window_truck = time_windows_3.time_matrix_truck(requests=requests)
    time_window_combined = time_window_train + time_window_barge + time_window_truck
    O_matrix_barge = OD_matrices.O_matrix_barge(requests=requests)
    D_matrix_barge = OD_matrices.D_matrix_barge(requests=requests)
    O_matrix_train = OD_matrices.O_matrix_train(requests=requests)
    D_matrix_train = OD_matrices.D_matrix_train(requests=requests)
    capacity_check = capacity_vehicles.capacity_check(requests=requests, capacities=capacities, vehicles=vehicles)

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
                                                                               assigned_requests=assigned_requests,
                                                                               time_window=time_window_combined)

                if assigned_requests[v][r] == 1 and r not in closed_requests:
                    closed_requests.append(r)

    # Assigning direct requests to trains
    for r in range(len(requests)):
        for v in range(len(vehicles)):
            direct_routes_train_check = capacity_check * time_window_train * (
                    (O_matrix_train * D_matrix_train) + O_matrix_train)

            # Possible direct routes train
            if direct_routes_train_check[v][r] == 2:
                # Assign requests to vehicles
                assign_direct_routes_train = logbook.assign_request_to_vehicle(open_requests=open_requests,
                                                                               closed_requests=closed_requests,
                                                                               vehicles=vehicles,
                                                                               capacities=capacities,
                                                                               vehicle_id=v,
                                                                               request_id=r,
                                                                               assigned_requests=assigned_requests,
                                                                               time_window=time_window_combined)
                if assigned_requests[v][r] == 1 and r not in closed_requests:
                    closed_requests.append(r)

    print(closed_requests)

    # Astar requests:
    for r in range(len(requests)):
        request_id = requests[r][7] - 100000
        used_vehicles = []
        if request_id not in closed_requests and request_id not in vervelend:
            print(f"Request_id: {request_id} ----------------------------------------------------------------------")
            capacity_check = capacity_vehicles.capacity_check(requests=requests, capacities=capacities,
                                                              vehicles=vehicles)

            CTE_matrix = OD_matrices.CTE2_matrix(E_matrix=E_matrix_All,
                                                 vehicles=vehicles,
                                                 time_window_matrix=time_window_combined,
                                                 request_id=request_id,
                                                 capacity_check=capacity_check)

            # Aanpassen time
            used_vehicles, a_star_runs = A_star_time.a_star_time(CTE_matrix=CTE_matrix,
                                                                 heuristic=H_matrix,
                                                                 start=requests[request_id][0],
                                                                 goal=requests[request_id][1] + 20,
                                                                 vehicles=vehicles,
                                                                 requests=requests,
                                                                 request_id=r)

            if a_star_runs < 50:
                unique_used_vehicles = used_vehicles

                # trajecten.append(traject)
                a_star_requests.append(request_id)
                a_star_used_vehicles.append(unique_used_vehicles)
                a_star_runs_all.append(a_star_runs)
                # print(used_vehicles)
                print(unique_used_vehicles)
                print(
                    f"Request_id: {request_id} ----------------------------------------------------------------------")

                # print(unique_used_vehicles)
                for v in range(len(unique_used_vehicles)):
                    vehicle_id = int(unique_used_vehicles[v])
                    assign_astar_routes = logbook.assign_request_to_vehicle(open_requests=open_requests,
                                                                            closed_requests=closed_requests,
                                                                            vehicles=vehicles,
                                                                            capacities=capacities,
                                                                            vehicle_id=vehicle_id,
                                                                            request_id=request_id,
                                                                            assigned_requests=assigned_requests,
                                                                            time_window=time_window_combined)

                closed_requests.append(request_id)
            else:
                unique_used_vehicles = []
                timed_out_requests.append(request_id)

    # Put emissions in results_matrix
    Results.emissions_from_assigned(assigned_requests=assigned_requests,
                                    vehicles=vehicles,
                                    requests=requests,
                                    results_matrix_requests=results_matrix_requests,
                                    H_matrix=H_matrix)

    results_matrix_requests, skipped_containers = logbook.skipped_requests(requests=requests,
                                                                           time_out_list=timed_out_requests,
                                                                           results_matrix_requests=results_matrix_requests,
                                                                           H_matrix=H_matrix)

    for r in range(len(requests)):
        total_emissions += results_matrix_requests[r][11]

    return total_emissions, timed_out_requests


def randomize_vehicles(vehicles_array, fixed_vehicles, origin, destination, amount_barges, number_possibilities):
    vehicles = fixed_vehicles.copy()
    random_time_slots = []

    for r in range(amount_barges * number_possibilities):
        random_number = random.randint(1, 190)
        random_time_slots.append(random_number)

# random vehicles werkt nog niet
    for r in range(int(number_possibilities)):
        for b in range(int(amount_barges)):
            for v in range(len(vehicles)):
                if vehicles[v][7] == 1 and vehicles[v][8] == origin and vehicles[v][9] == destination:
                    vehicles[v][11] = random_time_slots[r*b+b]
                    vehicles[v][10] = vehicles[v][11] - 1
                    vehicles[v][12] = vehicles[v][11] + fixed_vehicles[v][16]
                    vehicles[v][13] = vehicles[v][12] = 1
            vehicles_array.append(vehicles)

    return vehicles_array


fixed_vehicles = read_files.vehicles
vehicle_array = []
total_emissions_array = []
time_outs_array = []

# generate vehicle_array
vehicle_array = randomize_vehicles(vehicles_array=vehicle_array,
                                   fixed_vehicles=fixed_vehicles,
                                   origin=0,
                                   destination=3,
                                   amount_barges=14,
                                   number_possibilities=20)

# calculate total emissions for all vehicles options in vehicle_array
for v in range(len(vehicle_array)):
    emissions, timed_out_requests = total_emissions(vehicles=vehicle_array[2])
    total_emissions_array.append(emissions)
    time_outs_array.append(timed_out_requests)
