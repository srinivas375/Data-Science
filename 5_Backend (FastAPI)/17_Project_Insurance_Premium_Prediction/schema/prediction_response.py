from pydantic import BaseModel, Field
from typing import Dict

class PredictionResponse(BaseModel):
    predicted_category:str = Field(
        ...,
        description="category to be predicted by the model",
        examples=['Low', "medium", "High"]
    )
    confidence:float = Field(
        ...,
        description="Defines the confidence score of the prediction",
        example = 0.78
    )
    class_probabilities: Dict[str, float] = Field(
        ...,
        description="Defines all the classes probabilities",
        example={"Low": 0.01, "Medium": 0.15, "High": 0.84}
    )