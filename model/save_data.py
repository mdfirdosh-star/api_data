import json
from model.load_data import load_data
def save_data(data):
    with open("file\student_data.json","w") as f:
        json.dump(data,f)