## Pydantic
- Its Data PArsing and DAta Validation  Library for Python.
- Ensures Type safe of data. thats why mostly used along FastAPI

### Example:
```python
from pydantic import BaseModel

class Student(BaseModel):
    name : str

new_student= {'name':'maniii'}

student = Student(**new_student)
print(student)
print(type(student))
```
Output:
```
name='maniii'
<class '__main__.Student'>
```

## Example 2:
```python
from pydantic import BaseModel

class Student(BaseModel):
    name : str

new_student= {'name':32}

student = Student(**new_student)
print(student)
print(type(student))
```
Output:
```
  File "C:\Users\Anirudh31\Desktop\mini\GenAI\5) Structured Output\Pydantic\pydantic_demo.py", line 8, in <module>
    student = Student(**new_student)
  File "C:\Users\Anirudh31\AppData\Roaming\Python\Python313\site-packages\pydantic\main.py", line 250, in __init__
    validated_self = self.__pydantic_validator__.validate_python(data, self_instance=self)
pydantic_core._pydantic_core.ValidationError: 1 validation error for Student
name
  Input should be a valid string [type=string_type, input_value=32, input_type=int]
    For further information visit https://errors.pydantic.dev/2.12/v/string_type
```
- It causes error, tihs is not possible with just TypeDict

## Example with use of Optional and EmailStr
```python
from pydantic import BaseModel, EmailStr
from typing import Optional


class Student(BaseModel):
    name : str
    age: Optional[int]
    email: EmailStr

new_student= {'name':'maniii','age':32, 'email':"anirudh@gmail.com"}

student = Student(**new_student)
print(student)
print(type(student))
```
-O/P:
```
name='maniii' age=32 email='anirudh@gmail.com'
<class '__main__.Student'>
```

## ```Field``` in Pydantic:
- We can mention the RegEx, by using gt(Greater than), lt (lesser than).
- We can also use it as using Annotate in TypedDict using ```description```
- We can set Default value for the key
### Exmaple:
```python
from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class Student(BaseModel):
    name : str
    age: Optional[int]
    email: EmailStr
    cgpa : float = Field(gt=0 , lt= 10 , default=6 , description="this is float value grade procured by the student")

new_student= {'name':'maniii','age':32, 'email':"anirudh@gmail.com"}

student = Student(**new_student)
print(student)
print(type(student))
```
Output:
```
name='maniii' age=32 email='anirudh@gmail.com' cgpa=6
<class '__main__.Student'>
```
- As i used Default value of CGPA as 6, even though i dint give any parameter, the output shows 6.

## Conversion to Dictionary or json:
```python
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
```
Output:
```
32
{"name":"maniii","age":32,"email":"anirudh@gmail.com","cgpa":6.0}
```