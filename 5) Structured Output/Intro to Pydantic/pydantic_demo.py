from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name : str
    age: Optional[int]
    email: EmailStr
    cgpa : float = Field(gt=0 , lt= 10 , default=6 , description="this is float value grade procured by the student")

new_student= {'name':'maniii','age':32, 'email':"anirudh@gmail.com"}

student = Student(**new_student)

student_dict = dict(student)

print(student_dict['age'])

student_json = student.model_dump_json()
print(student_json)