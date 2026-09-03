"""
Assignment 2: Multi-Format Log Converter (Text to CSV & JSON)
Scenario
A server records raw access events as unformatted plain-text log lines. You need to parse the log lines into structured records and export them to both CSV and JSON formats.

Problem Description
Create a function convert_log_file(input_log_path, output_csv_path, output_json_path):

Each line in input_log_path follows the format: "<TIMESTAMP> | <USER_ID> | <ENDPOINT> | <STATUS_CODE>" (e.g., "2026-09-01 10:15:30 | USR102 | /api/v1/predict | 200").
Parses each line into a dictionary containing keys: timestamp, user_id, endpoint, status_code (as integer).
Writes all parsed records to output_csv_path with a header row using csv.DictWriter.
Writes the list of records to output_json_path with an indentation of 2 spaces using json.dump().
Example Walkthrough
convert_log_file("server_access.log", "access_records.csv", "access_records.json")
"""

import csv
import json

def convert_log_file(input_log_path, output_csv_path, output_json_path):
    payload = {
        'timestamp': '',
        'user_id': '',
        'endpoint': '',
        'status_code': ''
    }

    data_list = []

    with open(input_log_path, mode='r', encoding='utf-8', newline="") as file:
        for line in file:
            line = line.split("|")
            payload['timestamp'] = line[0]
            payload['user_id'] = line[1]
            payload['endpoint'] = line[2]
            payload['status_code'] = int(line[-1])
            data_list.append(payload)
    
    with open(output_csv_path, mode='w', encoding='utf-8', newline="") as csv_file, open(output_json_path, mode='w', encoding='utf-8',\
                                                                                         newline="") as json_file:
        write = csv.DictWriter(csv_file, fieldnames=['timestamp', 'user_id', 'endpoint', 'status_code'])
        write.writeheader()
        write.writerows(data_list)
        json.dump(data_list, json_file, indent=4)



def main():
    convert_log_file('api_access.log', 'output_csv_ex2.csv', 'output_json_ex2.json')

if __name__ == "__main__": main()