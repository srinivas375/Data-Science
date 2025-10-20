# This file is explains, how to use a ML model in FastAPI
# worked on insurance risk prediction (low, medium, high)
# need to install fastapi using `pip install fastapi[all]`
# using a built .pkl file
# For learning and understanding the integration, i used avaialbe .pkl model file

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from schema.user_input import User_Input
from model.predict import model, MODEL_VERSION, predict_premium
from schema.prediction_response import PredictionResponse



# defing the fastapi app
app = FastAPI()


@app.get('/')
def home():
    return {'message':'Welcome to FastAPI, Insurance premium prediction API'}


# helth checkup -- for machine readability
@app.get('/health')
def health_check():
    return {
        'status':'OK',
        'version': MODEL_VERSION,
        'model_loaded': model is not None
    }

    
# defining the `/predict` api route
@app.post('/predict', response_model=PredictionResponse)
def predict(data: User_Input):
    # for input to the model, the data should be a dataframe
    input_data ={
        'bmi':data.bmi,
        'age_group':data.age_group,
        'lifestyle_risk':data.lifestyle_risk,
        'city_tier':data.city_tier,
        'income_lpa':data.income_lpa,
        'occupation':data.Occupation
    }

    try:
        #prediction
        prediction = predict_premium(input_data)

        return JSONResponse(status_code=200, content=prediction)
    except Exception as e:
        return JSONResponse(status_code=500, content=str(e))

