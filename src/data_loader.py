import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

degree_requirements = load_data('data/degree_requirements.json')
user_progress = load_data('data/user_progress.json')

