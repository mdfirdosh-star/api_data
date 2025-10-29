import json, os

def load_data():
    path = "file/student_data.json"
    if not os.path.exists(path):
        raise FileNotFoundError(f"Data file not found: {path}")
    with open(path, "r") as f:
        return json.load(f)

