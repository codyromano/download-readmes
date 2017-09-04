from config import config
import csv

def for_each_csv_item(callback):
    with open(config['PATH_CSV_SOURCE'], 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        for row in reader:
            callback(row[0], row[1])
