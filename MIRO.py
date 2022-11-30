import itertools as iter
import numpy as np
import pandas as pd

import read_files

distances_path = "Instances/D_EGS-r.xlsx"
distances_barges = pd.ExcelFile(distances_path)

names = read_files.names

distances_barges = pd.read_excel(distances_barges, 'Barge')
#distances_barges['Barge'] = distances_barges['Barge'].map(names).fillna(distances_barges['Barge'])
# distances_barges['Delta'] = distances_barges['Delta'].map(names).fillna(distances_barges['Delta'])
# distances_barges['Euromax'] = distances_barges['Euromax'].map(names).fillna(distances_barges['Euromax'])
# distances_barges['HOME'] = distances_barges['HOME'].map(names).fillna(distances_barges['HOME'])
distances_barges = distances_barges.values
#distances_barges = read_files.D
requests = read_files.R
Distance_check = np.zeros([len(distances_barges), len(requests)])


for d in range(len(distances_barges)):
    for r in range(len(requests)):
        distance_id = distances_barges[d][0]
        distance_to_delta  = distances_barges[d][1]
        distance_to_euromax = distances_barges[d][2]
        distance_to_home = distances_barges[d][3]
        distance_to_moerdijk = distances_barges[d][4]
        distance_to_venlo = distances_barges[d][5]
        distance_to_duisberg = distances_barges[d][6]
        distance_to_willebroek = distances_barges[d][7]
        distance_to_neuss = distances_barges[d][8]
        distance_to_dortmund = distances_barges[d][9]
        distance_to_nuremberg = distances_barges[d][10]

        request_id = requests[r][7]
        request_origin = requests[r][0]
        request_destination = requests[r][1]

        if distances_barges_type == 1:
            if vehicle_bp > request_ap and vehicle_ad < request_bd:
                print(f"{request_id}" " in " f"{vehicle_id}")
                time_window_check[v][r] = 1
#print(names)
#print(distance_id)
#print(distances_barges)



# barge(Distance_EGS) = [A, B] #A = starting point, B = barge destination
# request_points = [O, D] #O = origin request, D = destination request
#
# for route in request_points(Intermodal_EGS_data):
#     if barge[A, B] = request_points[O, D]:
#         print(barge_number)
#         break
#     else:
#         if int(request_points) > dist(A -> O + B -> D)
#             return true
#         else:
#             false
#             if true:
#                 return min(dist(A -> O + B -> D))
#             if false:
#                use train
#                if train:



