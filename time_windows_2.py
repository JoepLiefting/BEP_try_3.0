import read_files
import itertools as iter
import numpy as np

vehicles = read_files.vehicles
requests = read_files.R
time_window_check = np.zeros([len(vehicles), len(requests)])


for v in range(len(vehicles)):
    for r in range(len(requests)):
        vehicle_id = vehicles[v][0]
        vehicle_ap = vehicles[v][10]
        vehicle_bp = vehicles[v][11]
        vehicle_ad = vehicles[v][12]
        vehicle_bd = vehicles[v][13]
        vehicle_type = vehicles[v][7]
        vehicle_origin = vehicles[v][8]
        vehicle_destination = vehicles[v][9]

        request_id = requests[r][7]
        request_ap = requests[r][2]
        request_bp = requests[r][3]
        request_ad = requests[r][4]
        request_bd = requests[r][5]
        request_origin = requests[r][0]
        request_destination = requests[r][1]

        if vehicle_type == 1 or vehicle_type == 2:
            if vehicle_bp > request_ap and vehicle_ad < request_bd:

                print(f"{request_id}" " in " f"{vehicle_id}")
                time_window_check[v][r] = 1




        # if vehicle_type == 1:
        #     print(f"\n{vehicle_id}")
        #     print("vehicle_ap: "f"{vehicle_ap}")
        #     print("vehicle_bp: " f"{vehicle_bp}")
        #     print("vehicle_ad: " f"{vehicle_ad}")
        #     print("vehicle_bd: " f"{vehicle_bd}")
        #
        # print(f"\n{request_id}")
        # print("request_ap: "f"{request_ap}")
        # print("request_bp: " f"{request_bp}")
        # print("request_ad: " f"{request_ad}")
        # print("request_bp: " f"{request_bd}")
