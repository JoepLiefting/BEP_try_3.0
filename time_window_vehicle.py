# def time_window_barge(vehicle_id, type='str'):
#     for vehicle_id in read_files.vehicles['K']:
#         Ap = read_files.vehicles['Ap']
#     return Ap
#
# time_window_barge('Barge1')
#
# print(time_window_barge('Barge1'))

import read_files
import itertools as iter
from openpyxl import load_workbook

data_file_vehicles = 'Instances/Vehicles.xlsx'
wb_vehicles = load_workbook(data_file_vehicles)
ws_vehicles = wb_vehicles['K']

all_rows = list(ws_vehicles.rows)

vehicles = read_files.vehicles
requests = read_files.R


# for row in all_rows[1:117]:
#     vehicle = row[0].value
#     vehicle_loading_start = row[10].value
#     vehicle_leaves = row[11].value
#     vehicle_arrives = row[12].value
#     vehicle_unloading_ends = row[13].value
#     vehicle_type = row[7].value
#     vehicle_origin = row[8].value
#     vehicle_destination = row[9].value
#
#     print(f"\n{vehicle}")
#     print("loading time starts at: "f"{vehicle_loading_start}")
#     print("leaves at: " f"{vehicle_leaves}")
#     print("arrives at: " f"{vehicle_arrives}")
#     print("unloading time ends at: " f"{vehicle_unloading_ends}")


for (vehicle, request) in iter.zip_longest(vehicles, requests):
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
        print(f"\n{vehicle_id}")
        print("loading time starts at: "f"{vehicle_ap}")
        print("leaves at: " f"{vehicle_bp}")
        print("arrives at: " f"{vehicle_ad}")
        print("unloading time ends at: " f"{vehicle_bd}")
