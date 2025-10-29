import json
def load_data():
    with open("file\student_data.json","r") as f:
        data=json.load(f)
    return data