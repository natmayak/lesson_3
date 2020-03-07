import csv

with open('suits_export', 'w', encoding='utf-8', newline='') as f:
    fields = ['name', 'age', 'job']
    writer = csv.DictWriter(f, fields, delimiter=',')
    writer.writeheader()
    suits_list = [
        {'name': 'Mike', 'age': 28, 'job': 'Associate'},
        {'name': 'Harvey', 'age': 38, 'job': 'Partner'},
        {'name': 'Rachel', 'age': 28, 'job': 'Paralegal'},
    ]
    for suiter in suits_list:
        writer.writerow(suiter)