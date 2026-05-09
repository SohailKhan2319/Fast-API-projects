# from fastapi import FastAPI
# app=FastAPI()

# @app.get("/")
# def hello():
#     return {'message':'Hello Girls'}

# @app.get('/about')
# def about():
#     return{'message':'All my Uni Girls Are Noob'}

# To run Project    uvicorn main:app --reload


              # Project Work  (Doctor Managing Profile Of Patient)
from fastapi import FastAPI,Path,HTTPException,Query
import json
app=FastAPI()

def load_data():
    with open('patients.json','r') as f:
        data=json.load(f)
    return data    

@app.get("/")
def hello():
    return {'message':'Patient Management System API'}

@app.get('/about')
def about():
    return{'message':'A Fully Functional API to manage your Patient records'}

@app.get('/view')
def view():
    data=load_data()

    return data

@app.get('/patient/{patient_id}')
def view_patient(patient_id:str=Path(...,description='ID of the patient in the DB',example='P001')):
    #Load all patients
    data=load_data()

    if patient_id in data:
        return data[patient_id]
    #  Raise An error 
    raise HTTPException(status_code=404,detail='Patient Not Found')

# Query Parameter   To pass additional data
@app.get('/sort')
def sort_patients(sort_by: str = Query(...,description='Sort on the basis of height,weight or bmi'),order:str=Query('asc',description='sort in asc or desc order')):
    valid_fields=['height','weight','bmi']

    if sort_by not in valid_fields:
        raise HTTPException(status_code=400,detail=f'Invalid field select from {valid_fields}')
    
    if order not in valid_fields:
        raise HTTPException(status_code=400,detail='Invalid oder select between asc and esc')
    
    data=load_data()

    sort_order=True if order=='desc' else False

    sorted_data=sorted(data.values(),key=lambda x:x.get(sort_by,0),reverse=sort_order)

    return sorted_data
