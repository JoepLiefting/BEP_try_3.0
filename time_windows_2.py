import read_files
import itertools as iter
import numpy as np

vehicles = read_files.vehicles
requests = read_files.R
time_window_check = np.zeros([len(vehicles), len(requests)])


for vehicle in vehicles:
    for request in requests:
        vehicle_id = vehicle[0]
        vehicle_ap = vehicle[10]
        vehicle_bp = vehicle[11]
        vehicle_ad = vehicle[12]
        vehicle_bd = vehicle[13]
        vehicle_type = vehicle[7]
        vehicle_origin = vehicle[8]
        vehicle_destination = vehicle[9]

        request_id = request[7]
        request_ap = request[2]
        request_bp = request[3]
        request_ad = request[4]
        request_bd = request[5]
        request_origin = request[0]
        request_destination = request[1]

        if vehicle_type == 1:
            if vehicle_bp > request_ap and vehicle_ad < request_bd:

                print(f"{request_id}" " in " f"{vehicle_id}")

                time_window_check[vehicle_id][request_id] = 1



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
