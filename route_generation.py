from openpyxl import load_workbook

data_file = 'Instances/D_EGS-r.xlsx'
wb = load_workbook(data_file, data_only=True)
ws = wb['Barge']

all_rows = list(ws.rows)

for row in all_rows[1:11]:
    Delta = row[0].value
    afstand = row[1].value
    if afstand < 1000000:
       print('Van Delta naar', f"\n{Delta}", 'is', f"{afstand}",'m')
    else:
        print('Van Delta naar', f"\n{Delta}", 'is niet mogelijk')

    Euromax = row[0].value
    afstand2 = row[2].value
    if afstand < 1000000:
        print('Van Euromax naar', f"\n{Euromax}", 'is', f"{afstand2}", 'm')
    else:
        print('Van Euromax naar', f"\n{Euromax}", 'is niet mogelijk')

