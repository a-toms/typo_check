import json
from correct import correct_text
import pprint
from gsheets import Sheets


# Load the JSON file
def load_data():
    path = '/Users/t/PycharmProjects/expert-dashboard/prisma/seed/tmp/ProductApplicationEvaluation.json'
    with open(path, 'r') as file:
        data = json.load(file)
    return data

# Process the evaluations.
def process_evaluations(data):   
    for i, item in enumerate(data):
        print(item)
        before = item["reference"]
        if not before:
            continue
        corrected_text, errors = correct_text(item["reference"])
        after = corrected_text
        
        pprint.pprint(f"Errors:")
        for error in errors:
            pprint.pprint(error)
        pprint.pprint(f"Before: {before}")
        pprint.pprint(f"After: {after}")
        
        print("Progress: ", i/len(data))
        
    save_rows(data)
    
    

# @TD TODO: Save the processed data to a Google Sheet using Google Sheets API
def save_rows(data):
    """ 
    Docs: https://gsheets.readthedocs.io/en/stable/api.html#sheets
    """
    client = Sheets.from_files('~/client_secrets.json', '~/storage.json')
    
    

    

if __name__ == "__main__":
    sample_data = [
        {"id":"1234",
         "productApplicationId":"5678",
         "evaluationCriterionId":"91011",
         "answer":"YES",
         "comment": None,
         "quality":6,
         "reference": (
             "<p><span style=\"color: rgb(0, 0, 0);\">You can set up a </span>"
             "<strong style=\"color: rgb(0, 0, 0);\">different interview kit for each interview stage</strong>"
             "<span style=\"color: rgb(0, 0, 0);\">.</span></p><p><br></p>"
             "<p>Interview Kit:</p><p>- Add new sections</p><p>- Set multiple question types: Score, Number, Multiple Choice, Yes/ No, Multiple Choice, Long/ Short Answer etc.</p><p>- Include candidate info e.g. CV</p><p>- Include job info e.g. job details and requireements</p><p><br></p>"
             "<p>Score candidates:</p><p>- Give candidates an overall scroe for that interview stage</p><p>- Give candidates multiple scores for that interview stage e.g. for each skill you're evaluating</p><p><br></p>"
             "<p>Plaftorm automatically calculates an overall score for the candidate based on all of the overall scores a candidate has received.</p>")}
    ]
    
    data = load_data()
    
    process_evaluations(data)
