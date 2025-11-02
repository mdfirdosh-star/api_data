
from pydantic import BaseModel,Field
from typing import List,Annotated,Optional
class update_details(BaseModel):

    student_id:Annotated[Optional[int],Field(description="enter the id",default=None)]
    name:Annotated[Optional[str],Field(description="enter the  name",default=None)]
    age:Annotated[Optional[int],Field(description="enter the age",default=None)]
    gender:Annotated[Optional[str],Field(description="enter the gender",default=None)]
    p_class:Annotated[Optional[str],Field(description="enter the pclass",default=None)]
    study_hours:Annotated[Optional[float],Field(description="enter the study_hours",default=None)]
    attendance:Annotated[Optional[int],Field(description="enter the attendence persentage",default=None)]
    math_score:Annotated[Optional[int],Field(description="enter the math score",default=None)]
    science_score:Annotated[Optional[int],Field(description="enter the science_score",default=None)]
    english_score:Annotated[Optional[int],Field(description="enter the english_score",default=None)]
    passed:Annotated[Optional[bool],Field(default=None)]
