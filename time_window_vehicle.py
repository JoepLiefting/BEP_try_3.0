import read_files

from openpyxl import load_workbook

data_file_vehicles = 'Instances/Vehicles.xlsx'
wb_vehicles = load_workbook(data_file_vehicles)
ws_vehicles = wb_vehicles['K']

all_rows = list(ws_vehicles.rows)

for row in all_rows[1:117]:
    vehicle = row[0].value
    vehicle_loading_start = row[10].value
    vehicle_leaves = row[11].value
    vehicle_arrives = row[12].value
    vehicle_unloading_ends = row[13].value

    print(f"\n{vehicle}")
    print("loading time starts at:"f"{vehicle_loading_start}")
    print("leaves at:" f"{vehicle_leaves}")
    print("arrives at" f"{vehicle_arrives}")
    print("unloading time ends at:" f"{vehicle_unloading_ends}")



#
# def time_window_barge(vehicle_id, type='str'):
#     for vehicle_id in read_files.vehicles['K']:
#         Ap = read_files.vehicles['Ap']
#     return Ap
#
# time_window_barge('Barge1')
#
# print(time_window_barge('Barge1'))
#
# print(read_files.vehicles.item("Barge1"))