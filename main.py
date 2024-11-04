import json
from correct import correct_text
import pprint
import dotenv
import csv
from datetime import datetime


dotenv.load_dotenv()


# Load the JSON file
def get_data():
    path = 'sample_data/ProductApplicationEvaluation.json'
    with open(path, 'r') as file:
        data = json.load(file)
    return data

# Process the evaluations.
def transform(data):   
    processed_data = []
    for i, item in enumerate(data):
        before = item["reference"]
        if not before:
            continue
        corrected_text, errors = correct_text(item["reference"])
        after = corrected_text
        
        if errors:
            for error in errors:
                processed_data.append({
                    "id": item["id"],
                    "error": error,
                    "before": before,
                    "after": after
            })
        
        print("Progress: ", i/len(data))
    return processed_data
        
    
    

# @TD TODO: Save the processed data to a Google Sheet using Google Sheets API
def save_rows(data: list[dict]):
    # Prepare data
    headers = ["id", "error", "before", "after"]
    rows = []
    for datum in data:
        try:
            rows.append([datum["id"], datum["error"], datum["before"], datum["after"]])
        except Exception as e:
            print(f"Error: {datum}")
    
    # Generate filename with timestamp
    filename = f'results_{datetime.now().strftime("%Y%m%d_%H%M%S")}.csv'
    
    # Write data
    with open(filename, 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(rows)
    
    print(f"Data saved to file: {filename}")

if __name__ == "__main__":
    sample_data = [
        {"id": "1234", "errors": ["Sample error", "Sample error 2"], "before": "Before", "after": "After"}
    ]
    
    data = get_data()
    processed_data = transform(data)
    save_rows(processed_data)
    