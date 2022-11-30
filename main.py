import read_files
import time_windows_3
import OD_matrices

requests = read_files.R

time_window_barge = time_windows_3.time_matrix_barge(requests= requests)
time_window_train = time_windows_3.time_matrix_train(requests= requests)

O_matrix_barge = OD_matrices.O_matrix_barge(requests= requests)
D_matrix_barge = OD_matrices.D_matrix_barge(requests= requests)
O_matrix_train = OD_matrices.O_matrix_train(requests= requests)
D_matrix_train = OD_matrices.D_matrix_train(requests= requests)

suitable_routes_barge = time_window_barge * (time_window_barge + O_matrix_barge * D_matrix_barge)
suitable_routes_train = time_window_train * (time_window_train + O_matrix_train * D_matrix_train)


