import pandas as pd
import numpy as np
import copy

vehicle_dict = {'Barge1': 0, 'Barge2': 1, 'Barge3': 2, 'Barge4': 3, 'Barge5': 4, 'Barge6': 5,

                'Barge7': 6, 'Barge8': 7, 'Barge9': 8, 'Barge10': 9, 'Barge11': 10, 'Barge12': 11, 'Barge13': 12,
                'Barge14': 13, 'Barge15': 14, 'Barge16': 15,

                'Barge17': 16, 'Barge18': 17, 'Barge19': 18, 'Barge20': 19, 'Barge21': 20, 'Barge22': 21, 'Barge23': 22,
                'Barge24': 23, 'Barge25': 24, 'Barge26': 25,

                'Barge27': 26, 'Barge28': 27, 'Barge29': 28, 'Barge30': 29, 'Barge31': 30, 'Barge32': 31, 'Barge33': 32,
                'Barge34': 33, 'Barge35': 34, 'Barge36': 35,

                'Barge37': 36, 'Barge38': 37, 'Barge39': 38, 'Barge40': 39, 'Barge41': 40, 'Barge42': 41, 'Barge43': 42,
                'Barge44': 43, 'Barge45': 44, 'Barge46': 45,

                'Barge47': 46, 'Barge48': 47, 'Barge49': 48, 'Train1': 49, 'Train2': 50, 'Train3': 51, 'Train4': 52,
                'Train5': 53, 'Train6': 54, 'Train7': 55,

                'Train8': 56, 'Train9': 57, 'Train10': 58, 'Train11': 59, 'Train12': 60, 'Train13': 61, 'Train14': 62,
                'Train15': 63, 'Train16': 64, 'Train17': 65,

                'Train18': 66, 'Train19': 67, 'Train20': 68, 'Train21': 69, 'Train22': 70, 'Train23': 71, 'Train24': 72,
                'Train25': 73, 'Train26': 74, 'Train27': 75,

                'Train28': 76, 'Train29': 77, 'Train30': 78, 'Train31': 79, 'Train32': 80, 'Train33': 81, 'Truck1': 82,
                'Truck2': 83, 'Truck3': 84, 'Truck4': 85,

                'Truck5': 86, 'Truck6': 87, 'Truck7': 88, 'Truck8': 89, 'Truck9': 90, 'Truck10': 91, 'Truck11': 92,
                'Truck12': 93, 'Truck13': 94, 'Truck14': 95,

                'Truck15': 96, 'Truck16': 97, 'Truck17': 98, 'Truck18': 99, 'Truck19': 100, 'Truck20': 101,
                'Truck21': 102, 'Truck22': 103, 'Truck23': 104, 'Truck24': 105,

                'Truck25': 106, 'Truck26': 107, 'Truck27': 108, 'Truck28': 109, 'Truck29': 110, 'Truck30': 111,
                'Truck31': 112, 'Truck32': 113, 'Truck33': 114, 'Truck34': 115, 'Truck35': 116}


def read_D(what, K):
    D_path = "Instances/D_EGS-r.xlsx"

    D_origin_barge = pd.read_excel(D_path, 'Barge')
    D_origin_train = pd.read_excel(D_path, 'Train')
    D_origin_truck = pd.read_excel(D_path, 'Truck')

    D_origin_barge = D_origin_barge.set_index('N')
    D_origin_train = D_origin_train.set_index('N')
    D_origin_truck = D_origin_truck.set_index('N')

    D_origin_barge = D_origin_barge.values
    D_origin_train = D_origin_train.values
    D_origin_truck = D_origin_truck.values

    D = {}

    for k in range(len(K)):

        if K[k, 5] == 1:

            D[k] = D_origin_barge.copy()

        else:

            if K[k, 5] == 2:

                D[k] = D_origin_train.copy()

            else:

                D[k] = D_origin_truck.copy()

    if what == 'D':
        return D

    D_origin_All = pd.read_excel(D_path, 'All')
    D_origin_All = D_origin_All.set_index('N')
    D_origin_All = D_origin_All.values

    if what == 'D_All':
        return D, D_origin_All

    if what == 'all':
        return D, D_origin_All, D_origin_barge, D_origin_train, D_origin_truck


def read_T(what, K):
    T_path = "Instances/T_EGS-r.xlsx"

    T_origin_barge = pd.read_excel(T_path, 'Barge')
    T_origin_train = pd.read_excel(T_path, 'Train')
    T_origin_truck = pd.read_excel(T_path, 'Truck')

    T_origin_barge = T_origin_barge.set_index('N')
    T_origin_train = T_origin_train.set_index('N')
    T_origin_truck = T_origin_truck.set_index('N')

    T_origin_barge = T_origin_barge.values
    T_origin_train = T_origin_train.values
    T_origin_truck = T_origin_truck.values

    T = {}

    for k in range(len(K)):

        if K[k, 5] == 1:

            T[k] = T_origin_barge.copy()

        else:

            if K[k, 5] == 2:

                T[k] = T_origin_train.copy()

            else:

                T[k] = T_origin_truck.copy()

    if what == 'T':
        return T


def read_E(what, K):
    E_path = "Instances/E_EGS-r.xlsx"

    E_origin_barge = pd.read_excel(E_path, 'Barge')
    E_origin_train = pd.read_excel(E_path, 'Train')
    E_origin_truck = pd.read_excel(E_path, 'Truck')

    E_origin_barge = E_origin_barge.set_index('N')
    E_origin_train = E_origin_train.set_index('N')
    E_origin_truck = E_origin_truck.set_index('N')

    E_origin_barge = E_origin_barge.values
    E_origin_train = E_origin_train.values
    E_origin_truck = E_origin_truck.values

    E = {}

    for k in range(len(K)):

        if K[k, 5] == 1:

            E[k] = E_origin_barge.copy()

        else:

            if K[k, 5] == 2:

                E[k] = E_origin_train.copy()

            else:

                E[k] = E_origin_truck.copy()

    if what == 'E':
        return E


def read_R_K(request_number_in_R, what='all'):
    Data = pd.ExcelFile(data_path)

    if what == 'K' or what == 'revert_K':

        K = pd.read_excel(Data, 'K')

        K = K.set_index('K')

        if what == 'revert_K':
            revert_K = dict(zip(K.index, range(len(K))))

            return revert_K

        K = K.values

        return K

    if what == 'all' or 'noR_pool':

        R = pd.read_excel(Data, 'R_' + str(request_number_in_R))

        revert_r = R['p'][0]

        if isinstance(revert_r, str):

            names = revert_names('str')

        else:

            names = revert_names('int')

        R['p'] = R['p'].map(names).fillna(R['p'])

        R['d'] = R['d'].map(names).fillna(R['d'])

        R.insert(7, 'r', range(len(R))) #kolom voor ID
        # R.insert(8, 'y', 0) #kolom voor bezorgdagen

        R = R.values



        # for index in range(len(R)):
        #     R[index, 8] = (R[index, 3] - R[index, 2])/24

        # #sorteren
        # R = R[R[:, 2].argsort()]
        # R = R[R[:, 8].argsort(kind='mergesort')]



        for index in range(len(R)):
            R[index, 7] = R[index, 7] + 100000 * parallel_number


        c_delay_list = []

        for request_number in R[:, 7]:

            index_r = list(R[:, 7]).index(request_number)

            if R[index_r, 5] - R[index_r, 2] < 30:

                c_delay_list.append(100)

            else:

                if R[index_r, 5] - R[index_r, 2] < 54:

                    c_delay_list.append(70)



                else:

                    c_delay_list.append(50)

        # R['c_delay'] = c_delay_list

        np.append(R, np.c_[c_delay_list], axis=1)

        R_info = -1

        R_pool = R.copy()

        K = pd.read_excel(Data, 'K')

        K = K.set_index('K')

        K = K.values

        if what == 'noR_pool':
            return R, R_info, K

        if what == 'all':
            return R, R_info, K, R_pool
        # return R


def revert_names(type='str'):
    if type == 'str':

        return {'Delta': 0, 'Euromax': 1, 'HOME': 2, 'Moerdijk': 3, 'Venlo': 4, 'Duisburg': 5,

                'Willebroek': 6, 'Neuss': 7, 'Dortmund': 8, 'Nuremberg': 9, 'Delta1': 10, 'Euromax1': 11, 'HOME1': 12,
                'Moerdijk1': 13, 'Venlo1': 14, 'Duisburg1': 15,

                'Willebroek1': 16, 'Neuss1': 17, 'Dortmund1': 18, 'Nuremberg1': 19, 'Delta2': 20, 'Euromax2': 21,
                'HOME2': 22, 'Moerdijk2': 23, 'Venlo2': 24, 'Duisburg2': 25,

                'Willebroek2': 26, 'Neuss2': 27, 'Dortmund2': 28, 'Nuremberg2': 29}

    else:

        return {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9, 11: 10, 12: 11, 13: 12, 14: 13, 15: 14,
                16: 15, 17: 16, 18: 17, 19: 18, 20: 19, 21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27,
                29: 28, 30: 29}


def revert_vehicles(type='str'):
    if type == 'str':

        return vehicle_dict

    else:

        return {1: 0, 2: 1, 3: 2, 4: 3, 5: 4, 6: 5, 7: 6, 8: 7, 9: 8, 10: 9,
                11: 10, 12: 11, 13: 12, 14: 13, 15: 14, 16: 15, 17: 16, 18: 17, 19: 18, 20: 19,
                21: 20, 22: 21, 23: 22, 24: 23, 25: 24, 26: 25, 27: 26, 28: 27, 29: 28, 30: 29,
                31: 30, 32: 31, 33: 32, 34: 33, 35: 34, 36: 35, 37: 36, 38: 37, 39: 38, 40: 39,
                41: 40, 42: 41, 43: 42, 44: 43, 45: 44, 46: 45, 47: 46, 48: 47, 49: 48, 50: 49,
                51: 50, 52: 51, 53: 52, 54: 53, 55: 54, 56: 55, 57: 56, 58: 57, 59: 58, 60: 59,
                61: 60, 62: 61, 63: 62, 64: 63, 65: 64, 66: 65, 67: 66, 68: 67, 69: 68, 70: 69,
                71: 70, 72: 71, 73: 72, 74: 73, 75: 74, 76: 75, 77: 76, 78: 77, 79: 78, 80: 79,
                81: 80, 82: 81, 83: 82, 84: 83, 85: 84, 86: 85, 87: 86, 88: 87, 89: 88, 90: 89,
                91: 90, 92: 91, 93: 92, 94: 93, 95: 94, 96: 95, 97: 96, 98: 97, 99: 98, 100: 99,
                101: 100, 102: 101, 103: 102, 104: 103, 105: 104, 106: 105, 107: 106, 108: 107, 109: 108, 110: 109,
                111: 110, 112: 111, 113: 112, 114: 113, 115: 114}


def read_no_route():
    # please change it to your own data path

    Barge_no_land_path = "Instances/suitable_routes.xlsx"

    no_route_barge = pd.read_excel(Barge_no_land_path, 'Barge')

    no_route_truck = pd.read_excel(Barge_no_land_path, 'Truck')

    names = revert_names()

    no_route_barge['O'] = no_route_barge['O'].map(names).fillna(no_route_barge['O'])

    no_route_barge['D'] = no_route_barge['D'].map(names).fillna(no_route_barge['D'])

    no_route_truck['O'] = no_route_truck['O'].map(names).fillna(no_route_truck['O'])

    no_route_truck['D'] = no_route_truck['D'].map(names).fillna(no_route_truck['D'])

    no_route_barge = no_route_barge.values

    no_route_truck = no_route_truck.values

    return no_route_barge, no_route_truck


parallel_number = 1

# please change it to your own data path

data_path = "Instances/Intermodal_EGS_data_all.xlsx"
coords_path = "Instances/Coordinates.xlsx"
fixed_path = "Instances/Fixed_vehicles.xlsx"
vehicles_path = "Instances/Vehicles.xlsx"
H_path = "Instances/H_matrix.xlsx"

# read routes that are unsuitable to barges and trucks

no_route_barge, no_route_truck = read_no_route()

Data = pd.ExcelFile(data_path)

# number of requests, it can be 5, 10, 20, 30, 50, 100, 200, 400, 700, 1000, 1300, 1600

request_number_in_R = 100

# fixed vehicles information

# change names of terminals to numbers

names = revert_names()
vehiclesindex = revert_vehicles()
vehicles = pd.ExcelFile(vehicles_path)

vehicles = pd.read_excel(vehicles, 'K')
vehicles['K'] = vehicles['K'].map(vehiclesindex).fillna(vehicles['K'])
vehicles['o'] = vehicles['o'].map(names).fillna(vehicles['o'])
vehicles['o2'] = vehicles['o2'].map(names).fillna(vehicles['o2'])
vehicles.insert(14, 'E', np.zeros(len(vehicles)))
vehicles.insert(15, 'D', np.zeros(len(vehicles)))
vehicles.insert(16, 'T', np.zeros(len(vehicles)))
vehicles = vehicles.values

# terminals

N = pd.read_excel(Data, 'N')

N = N.values


# read depots

o = pd.read_excel(Data, 'o')

o = o.set_index('K')

o['o'] = o['o'].map(names).fillna(o['o'])

o['o2'] = o['o2'].map(names).fillna(o['o2'])

o = o.values

# transshipment terminals

T = pd.read_excel(Data, 'T')

T['T'] = T['T'].map(names).fillna(T['T'])

T = list(T['T'])

# requests, inforation of requests, vehicles, requests pool

R, R_info, K, R_pool = read_R_K(request_number_in_R)

# distance between terminals of all vehicles, distance between terminals of trucks

D, D_origin_All = read_D('D_All', K)
T = read_T('T', K)
E = read_E('E', K)

pickup_delivery = R[:, 0:2]

# coordinates nodes

Coordinates = pd.ExcelFile(coords_path)

Coords = pd.read_excel(Coordinates, 'c')
Coords = Coords.set_index('t')
Coords['x'] = Coords['x'].map(names).fillna(Coords['x'])
Coords['y'] = Coords['y'].map(names).fillna(Coords['y'])
Coords = Coords.values

H_matrix = pd.ExcelFile(H_path)
H_matrix = pd.read_excel(H_matrix, 'Barge', index_col=0)
H_matrix.reset_index()
H_matrix = H_matrix.values
for i in range(len(H_matrix)):
    for j in range(len(H_matrix)):
        if H_matrix[i][j] == 0:
            H_matrix[i][j] = 0.01

# for i in range(len(H_matrix)):
#     for j in range(len(H_matrix)):
#         if H_matrix[i][j] == 1000000:
#             H_matrix[i][j] = 0

E_path = "Instances/E_EGS-r.xlsx"
E_matrix_All = pd.read_excel(E_path, 'Allv')
E_matrix_All = E_matrix_All.set_index('N')
E_matrix_All = E_matrix_All.values
for i in range(len(E_matrix_All)):
    for j in range(len(E_matrix_All)):
        if E_matrix_All[i][j] == 0:
            E_matrix_All[i][j] = 0.01

for i in range(len(E_matrix_All)):
    for j in range(len(E_matrix_All)):
        if E_matrix_All[i][j] > 2000:
            E_matrix_All[i][j] = 0

E2_path = "Instances/E_EGS-r-2.xlsx"
E2_matrix_All = pd.read_excel(E2_path, 'Allv')
E2_matrix_All = E2_matrix_All.set_index('N')
E2_matrix_All = E2_matrix_All.values
for i in range(len(E2_matrix_All)):
    for j in range(len(E2_matrix_All)):
        if E2_matrix_All[i][j] > 2000:
            E2_matrix_All[i][j] = 0


# for i in range(len(E_matrix_All)):
#     for j in range(len(E_matrix_All)):
#         if E_matrix_All[i][j] == 1000000:
#             E_matrix_All[i][j] = 0

# Vehicles = pd.ExcelFile(vehicles_path)
# curcap = pd.read_excel(Vehicles, 'K', usecols=['curcap'])
# curcap = curcap.values

# emissions in vehicles array based on E_matrix
for v in range(len(vehicles)):
    vehicle_type = vehicles[v][7]
    origin = int(vehicles[v][8])
    destination = int(vehicles[v][9])

    if vehicle_type == 1:
        vehicles[v][14] = E_matrix_All[origin][destination]

    elif vehicle_type == 2:
        vehicles[v][14] = E_matrix_All[origin + 10][destination + 10]

    elif vehicle_type == 3:
        vehicles[v][14] = E_matrix_All[origin + 20][destination + 20]

# E_coefficient from paper Bilge
E_coefficient_barge = 0.2288
E_coefficient_train = 0.3146
E_coefficient_truck = 0.8866

# Distance vehicle based on emissions
for v in range(len(vehicles)):
    vehicle_type = vehicles[v][7]

    if vehicle_type == 1:
        vehicles[v][15] = vehicles[v][14] / E_coefficient_barge

    elif vehicle_type == 2:
        vehicles[v][15] = vehicles[v][14] / E_coefficient_train

    elif vehicle_type == 3:
        vehicles[v][15] = vehicles[v][14] / E_coefficient_truck

# Time vehicle based on distance
for v in range(len(vehicles)):
    vehicles[v][16] = vehicles[v][15] / vehicles[v][3]
