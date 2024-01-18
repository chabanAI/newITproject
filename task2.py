import csv
import json

def convert_csv_to_json(csv_file_path, delimiter=',', newline='\n'):
   
    try:
        with open(csv_file_path, 'r', newline=newline, encoding='utf-8') as csv_file:
            
            csv_reader = csv.DictReader(csv_file, delimiter=delimiter)
            
            data_list = [row for row in csv_reader]

        json_string = json.dumps(data_list, indent=4, ensure_ascii=False)
        
        return json_string
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Пример использования:
csv_file_path = "path/to/your/file.csv"
json_result = convert_csv_to_json(csv_file_path)

if json_result is not None:
    print(json_result)
