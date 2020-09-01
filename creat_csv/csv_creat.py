import csv

list_of_guitarists = {
    'Eric Clapton': 'Cream',
    'Jimmy Page': 'Led Zeppelin',
    'Keith Richards': 'Rolling Stones',
    'Eddie Van Halen': 'Van Halen',
    'David Gilmour': 'Pink Floyd',
    'Angus Young': 'AD/DC',
    'Brian May': 'Queen',
    'Johnny Ramone': 'Ramones',
    'Tom Morello': 'Rage Against the Machine',
    'Slash': "Guns'n Roses",
    'Jim Root': 'Slipknot',
    'Kirk Hammet': 'Metallica'
}
"""list_of_guitarists dictionary transformed in csv file."""

with open('list_of_guitarists.csv', 'w') as f:
    for key in list_of_guitarists:
        csv_columns = []
        k = key
        csv_columns.append(k)
        v = list_of_guitarists[key]
        csv_columns.append(v)
        w = csv.DictWriter(f, fieldnames=csv_columns)
        w.writeheader()
