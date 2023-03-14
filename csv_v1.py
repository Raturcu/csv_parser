import csv
import pandas as pd

with open('glpi.csv', newline='', encoding='utf-8') as csvfile:
    read = csv.reader(csvfile, delimiter=';', quotechar='"')
    table_header = next(read)
    table_header = [header.replace('"', '') for header in table_header] # elimina toate ghilimelele din antete
    print(table_header)

# Scrie antetul tabelului în fișier cu primul caracter eliminat din primul antet și fără ghilimele
with open('export.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    new_table_header = [table_header[0][1:]] + table_header[1:] # elimina primul caracter din primul antet si pastreaza celelalte antete
    writer.writerow(new_table_header)
    
    # Deschide fișierul 'glpi.csv' în modul de citire
    with open('glpi.csv', newline='', encoding='utf-8') as csvfile_read:
        read = csv.reader(csvfile_read, delimiter=';', quotechar='"')
        next(read)  # Sari peste antetul tabelului
        for row in read:
            writer.writerow(row)
            
df = pd.read_csv('export.csv')
print(df)