import read_files
import time_windows_3
import OD_matrices
import capacity_vehicles

requests = read_files.R

time_window_barge = time_windows_3.time_matrix_barge(requests= requests)
time_window_train = time_windows_3.time_matrix_train(requests= requests)

O_matrix_barge = OD_matrices.O_matrix_barge(requests= requests)
D_matrix_barge = OD_matrices.D_matrix_barge(requests= requests)
O_matrix_train = OD_matrices.O_matrix_train(requests= requests)
D_matrix_train = OD_matrices.D_matrix_train(requests= requests)

capacity_check = capacity_vehicles.capacity_check(requests= requests)

suitable_routes_barge = capacity_check * time_window_barge * ((O_matrix_barge * D_matrix_barge) + O_matrix_barge)
suitable_routes_train = capacity_check * time_window_train * ((O_matrix_train * D_matrix_train) + O_matrix_train)



# vehicles = read_files.vehicles
# for v in range(len(vehicles)):
#     for r in range(len(requests)):
#         suitable_routes_barge = suitable_routes_barge[v][r]
#
#         if request_qr <= curcap:
#             capacity_check[v][r] = 1



update_capacity = capacity_vehicles.update_curcap(requests= requests,
                                                  vehicle_id= 2,
                                                  request_id= 100001)

