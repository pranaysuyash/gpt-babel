import json
import os

# Define the path for the JSON file that will store the data
DATA_FILE = 'events.json'

def read_data():
    """Read the data from the JSON file."""
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, 'r') as file:
        return json.load(file)

def check_existing_data(short_url_id):
    """Check if the URL data already exists in the JSON file."""
    data = read_data()
    return short_url_id in data

def save_data(short_url_id, gizmo_data):
    """Save the new data associated with the short_url_id to the JSON file."""
    data = read_data()
    data[short_url_id] = gizmo_data
    with open(DATA_FILE, 'w') as file:
        json.dump(data, file, indent=4)

def get_data(short_url_id):
    """Retrieve the data associated with the short_url_id from the JSON file."""
    data = read_data()
    return data.get(short_url_id)
