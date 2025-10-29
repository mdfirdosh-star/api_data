
from fastapi import FastAPI,Path,HTTPException
from fastapi.responses import JSONResponse
from model.load_data import  load_data
from model.save_data import save_data
from p_data.student_data import student_detail
from p_data.update import update_details


app=FastAPI()

@app.get("/")
def home():
    return {"message":"welcome to my school "}
@app.get("/about")
def about():
    return{"message":"all student detali in the api"}

@app.get("/view")
def view_details():
    data=load_data()
    return data

@app.get("/stuednt/{student_id}")
def find_student(student_id:int=Path(...,description="enter the roll_no od student",example=1)):
    data=load_data()
    for i in data["student"]:
        if i["student_id"]==student_id:
            return i
    HTTPException(status_code=404,detail="file not found ")

@app.get("/total")
def total_student():
    data=load_data()
    return {"total student details" :len(data["student"])}
    



# post 
@app.post("/create")
def create_data(d:student_detail):
    data=load_data()
    if any(i["student_id"]==d.student_id for i in data["student"]):
       raise HTTPException(status_code=400,detail="data already exists")
    data["student"].append(d.model_dump())
    save_data(data)
    return JSONResponse(status_code=201,content={"message":"data sucessful create"})


@app.put("/edit/{student_id}")
def edit_student(student_id:int,d:update_details):
    data=load_data()
    for i in data["student"]:
        if i["student_id"]==student_id:
            update_val=d.model_dump(exclude_unset=True)
            i.update(update_val)
            save_data(data)
            return JSONResponse(status_code=200,content={"message":"file successful edit"})
        

@app.delete("/delete")
def delete_student(student_id:int):
    data=load_data()
    for i in data["student"]:
        if i["student_id"]==student_id:
            data["student"].remove(i)
            save_data(data)
            return JSONResponse(status_code=200,content={"message":"file successful delete"})
