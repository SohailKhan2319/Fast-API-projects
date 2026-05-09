# # # Why Pydantic
# # def insert_patient_data(name,age):
# #     print(name)
# #     print(age)
# #     print('Inserted in to Database')


# # insert_patient_data('Sohail','Fifty')

# # # Do typeprinting to avoid this  but it only give hint if he enters again Fifty it is valid

# # def insert_patient_data(name:str,age:int):
# #     print(name)
# #     print(age)
# #     print('Inserted in to Database')


# # insert_patient_data('Sohail','30')

# # To Strictly follow this  this logic is good but not scalable
# def insert_patient_data(name:str,age:int):
#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('Inserted in to Database')
#     else:
#         raise TypeError('Incorrect Datatype')    


# insert_patient_data('Sohail','30')

# def update_patient_data(name:str,age:int):
#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('Updated')
#     else:
#         raise TypeError('Incorrect Datatype')    


# update_patient_data('Sohail','30')

# # There can be multiple tables so this Problem is solved by pydantic
# # First Problem that pydantic manages is type validation

# # Data Validation Problem   it also Scalable
# def insert_patient_data(name:str,age:int):
    
#     if type(name)==str and type(age)==int:
#           if age <0:
#               raise ValueError('Age can not be Negative')
#           else:
#               print(name)
#               print(age)
#               print('Inserted in to Database')
#     else:
#         raise TypeError('Incorrect Datatype')    


# insert_patient_data('Sohail','30')

# def update_patient_data(name:str,age:int):
    
#     if type(name)==str and type(age)==int:
#           if age <0:
#               raise ValueError('Age can not be Negative')
#           else:
#               print(name)
#               print(age)
#               print('Inserted in to Database')
#     else:
#         raise TypeError('Incorrect Datatype')    


# update_patient_data('Sohail','30')

# Pydantic solves the data validation and type validation
# Works in three Steps
# 1.create Pydantic Model  2.Create Object    3.Pass the validated object to function

from pydantic import BaseModel
class Patient(BaseModel):
    name:str
    age:int


def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Inserted in to Database')

patient_info={'name':'Sohail','age':30}    

patient1=Patient(**patient_info)

insert_patient_data(patient1)
#    Error  Code
# patient_info={'name':'Sohail','age':'thirty'}    

# patient1=Patient(**patient_info)

# insert_patient_data(patient1)

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print('Updated')

patient_info={'name':'Ahmed','age':20}    

patient1=Patient(**patient_info)

update_patient_data(patient1)



