import csv
import json

def convert_csv_to_json(cfilename):
    try:
        with open(cfilename, 'r') as cfile:
            reader = csv.DictReader(cfile)
            with open('data.json', 'w') as jfile:
                for line in reader:
                    json.dump(line, jfile)
                return True
    except FileNotFoundError:
        return False
  