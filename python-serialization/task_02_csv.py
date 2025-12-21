import csv
import json

def convert_csv_to_json(cfilename):
    try:
        with open(cfilename, 'r') as cfile:
            reader = csv.DictReader(cfile)
            data = list(reader)
            with open('data.json', 'w') as jfile:
                json.dump(line, jfile)
                return True
    except FileNotFoundError:
        return False
  