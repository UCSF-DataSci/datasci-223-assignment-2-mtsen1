#!/usr/bin/env python3
"""
Patient Data Cleaner

This script standardizes and filters patient records according to specific rules:

Data Cleaning Rules:
1. Names: Capitalize each word (e.g., "john smith" -> "John Smith")
2. Ages: Convert to integers, set invalid ages to 0
3. Filter: Remove patients under 18 years old
4. Remove any duplicate records

Input JSON format:
    [
        {
            "name": "john smith",
            "age": "32",
            "gender": "male",
            "diagnosis": "hypertension"
        },
        ...
    ]

Output:
- Cleaned list of patient dictionaries
- Each patient should have:
  * Properly capitalized name
  * Integer age (≥ 18)
  * Original gender and diagnosis preserved
- No duplicate records
- Prints cleaned records to console

Example:
    Input: {"name": "john smith", "age": "32", "gender": "male", "diagnosis": "flu"}
    Output: {"name": "John Smith", "age": 32, "gender": "male", "diagnosis": "flu"}

Usage:
    python patient_data_cleaner.py
"""

import json
import os

def load_patient_data(filepath):
    """
    Load patient data from a JSON file.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        list: List of patient dictionaries
    """
    # BUG: No error handling for file not found
    # FIX: added a try/except clause
    try:
        with open(filepath, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File not found")
        return None

def clean_patient_data(patients):
    """
    Clean patient data by:
    - Capitalizing names
    - Converting ages to integers
    - Filtering out patients under 18
    - Removing duplicates
    
    Args:
        patients (list): List of patient dictionaries
        
    Returns:
        list: Cleaned list of patient dictionaries
    """
    cleaned_patients = []
    seen = set() # FIX: added a set to track duplicates
    
    for patient in patients:
        # BUG: Typo in key 'nage' instead of 'name'
        # FIX: Fixed 'nage' to 'name'
        patient['name'] = patient['name'].title()
        
        # BUG: Wrong method name (fill_na vs fillna)
        # FIX: fillna is not a method for dictionaries --> changed to try/except
        try:
            patient['age'] = int(patient['age'])
        except (KeyError, ValueError, TypeError):
            patient['age'] = 0
        
        # BUG: Wrong method name (drop_duplcates vs drop_duplicates)
        # FIX: Fixed "drop_duplcates" to "drop_duplicates"
        # FIX: removed this line since this is a dict not a dataframe
        # patient = patient.drop_duplicates()
        
        # BUG: Wrong comparison operator (= vs ==)
        # FIX: Used a correct operator
        if patient['age'] >= 18:
            # BUG: Logic error - keeps patients under 18 instead of filtering them out
            # FIX: changed above operator to only patients 18 or older
            # FIX: uses 'seen' set to remove duplicates for dict type
            identifier = (patient['name'], patient['age'], patient.get('diagnosis'))
            if identifier not in seen:
                seen.add(identifier)
                cleaned_patients.append(patient)

    # BUG: Missing return statement for empty list
    # FIX: Changed 'none' to [] 
    if not cleaned_patients:
        return []
    
    return cleaned_patients

def main():
    """Main function to run the script."""
    # Get the directory of the current script
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Construct the path to the data file
    data_path = os.path.join(script_dir, 'data', 'raw', 'patients.json')
    
    # BUG: No error handling for load_patient_data failure
    # FIX: Added error message for patient data loading failure
    patients = load_patient_data(data_path)
    if patients is None:
        print(f"Patient data not found")
        return
    
    # Clean the patient data
    cleaned_patients = clean_patient_data(patients)
    
    # BUG: No check if cleaned_patients is None
    # FIX: added error message if cleaned_patients is None
    # Print the cleaned patient data
    if cleaned_patients is None:
        print(f"No cleaned patient data found")
    else:
        print("Cleaned Patient Data:")
    for patient in cleaned_patients:
        # BUG: Using 'name' key but we changed it to 'nage'
        # FIX: 'nage' was fixed above
        print(f"Name: {patient['name']}, Age: {patient['age']}, Diagnosis: {patient['diagnosis']}")
    
    # Return the cleaned data (useful for testing)
    return cleaned_patients

if __name__ == "__main__":
    main()