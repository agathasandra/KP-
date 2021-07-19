#https://stackoverflow.com/questions/46614526/how-to-import-a-csv-file-into-a-data-array
#membaca csv dan mengubahnya ke dalam bentuk array
import csv

with open('bidmc_01_Signals.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

#print(data[1][0])
