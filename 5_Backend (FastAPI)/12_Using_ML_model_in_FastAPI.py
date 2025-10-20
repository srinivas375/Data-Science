'''
 - This file explains, how to use a ML model in FastAPI
 - worked on insurance risk prediction (low, medium, high)
 - need to install fastapi using `pip install fastapi[all]`
 - using a built .pkl file
 - For learning and understanding the integration, i used avaialbe .pkl model file
'''

from fastapi import FastAPI
from fastapi.responses import JSONResponse
import pickle
from typing import Literal, Annotated
from pydantic import BaseModel, Field, computed_field
import pandas as pd

# defing the fastapi app
app = FastAPI()

@app.get('/home')
def greet():
    return {'message':'Welcome to FastAPI, This file is used to work on integrating the ml model with FastAPI'}

# loading the ml model
with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

# defining the city tiers
tier_1_cities = ["Mumbai", "Delhi", "Bangalore", "Chennai", "Kolkata", "Hyderabad", "Pune"]
tier_2_cities = [
    "Jaipur", "Chandigarh", "Indore", "Lucknow", "Patna", "Ranchi", "Visakhapatnam", "Coimbatore",
    "Bhopal", "Nagpur", "Vadodara", "Surat", "Rajkot", "Jodhpur", "Raipur", "Amritsar", "Varanasi",
    "Agra", "Dehradun", "Mysore", "Jabalpur", "Guwahati", "Thiruvananthapuram", "Ludhiana", "Nashik",
    "Allahabad", "Udaipur", "Aurangabad", "Hubli", "Belgaum", "Salem", "Vijayawada", "Tiruchirappalli",
    "Bhavnagar", "Gwalior", "Dhanbad", "Bareilly", "Aligarh", "Gaya", "Kozhikode", "Warangal",
    "Kolhapur", "Bilaspur", "Jalandhar", "Noida", "Guntur", "Asansol", "Siliguri"
]

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
    
# defining the `/predict` api route
@app.post('/predict')
def predict(data: User_Input):
    # for input to the model, the data should be a dataframe
    input_data = pd.DataFrame([{
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.Occupation
    }])

    #prediction
    prediction = model.predict(input_data)[0]

    return JSONResponse(status_code=200, content={'Predicted-category':prediction})