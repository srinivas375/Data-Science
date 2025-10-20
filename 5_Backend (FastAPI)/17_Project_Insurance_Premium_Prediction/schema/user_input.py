from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field, field_validator
from config.cities_tier import tier_1_cities, tier_2_cities

# building the pydantic base model

class User_Input(BaseModel):
    age: Annotated[int, Field(..., description="Age of the user", lt=120, gt=0)]
    weight: Annotated[float, Field(..., description="Weight of the user", gt=0)]
    height: Annotated[float, Field(..., description="Height of the user (in meters)", gt=0, lt=2.5)]
    income_lpa: Annotated[float, Field(..., description="Yearly income of the user (in LPA)", gt=0)]
    smoker: Annotated[bool, Field(..., description="Does the user smokes?")]
    city: Annotated[str, Field(..., description="City of the user")]
    Occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'], Field(..., description="Occupation of the user")]
    
    # converting the input city to capitalize value
    @field_validator('city')
    @classmethod
    def capitalize_city(cls, v:str) -> str:
        return v.strip().title()


    @computed_field
    @property
    def bmi(self) -> float:
        return self.weight/(self.height**2)
    
    @computed_field
    @property
    def lifestyle_risk(self) -> str:
        if self.smoker and self.bmi > 30:
            return 'high'
        elif self.smoker or self.bmi >27:
            return 'medium'
        else:
            return 'low'
        
    @computed_field
    @property
    def age_group(self) -> str:
        if self.age <25:
            return 'young'
        elif self.age <45:
            return 'adult'
        elif self.age <60:
            return 'middle_aged'
        return 'senior'
    
    @computed_field
    @property
    def city_tier(self) -> int:
        if self.city in tier_1_cities:
            return 1
        elif self.city in tier_2_cities:
            return 2
        return 3