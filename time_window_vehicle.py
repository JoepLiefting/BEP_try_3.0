import read_files

def time_window_barge(vehicle_id, type='str'):
    if vehicle_id in read_files.vehicles.index:
        Ap = read_files.vehicles['Ap']
    return Ap

time_window_barge('Barge1')

print(time_window_barge('Barge1'))
