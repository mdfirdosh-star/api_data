

from pydantic import BaseModel,Field
from typing import List,Annotated,Optional
class student_detail(BaseModel):
    student_id:Annotated[int,Field(...,description="enter the roll no")]
    name:Annotated[str,Field(...,description="enter the name")]
    age:Annotated[int,Field(...,description="enter the age ")]
    gender:Annotated[str,Field(...,description="enter the gender")]
    p_class:Annotated[str,Field(...,description="enter the p_calss",example="10th")]
    study_hours:Annotated[float,Field(...,description="enter the study hours")]
    attendence:Annotated[int,Field(...,description="enter the attendence persentage")]
    math_score:Annotated[int,Field(...,description="enter the math persentage ")]
    science_score:Annotated[int,Field(...,description="enter the science presentage")]
    english_score:Annotated[int,Field(...,description="enter the english presentage")]
    passed:bool