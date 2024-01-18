import json

def calculate_sum_of_products(json_path):
    
    try:
        with open(json_path, 'r') as file:
            data = json.load(file)
        
        products = [entry["score"] * entry["weight"] for entry in data]
        
        total_sum = sum(products)
        
        rounded_result = round(total_sum, 3)
        
        return rounded_result
    except FileNotFoundError:
        print("File not found.")
    except json.JSONDecodeError:
        print("Invalid JSON format.")
    except KeyError:
        print("Invalid JSON structure.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


json_file_path = "path/to/file.json"
result = calculate_sum_of_products(json_file_path)

if result is not None:
    print(f"Sum of products: {result}")
