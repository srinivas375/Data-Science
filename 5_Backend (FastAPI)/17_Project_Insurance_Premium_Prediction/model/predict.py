import pickle
import pandas as pd

# MLFlow
MODEL_VERSION = '1.0.0'


# loading the ml model
with open('model/model.pkl', 'rb') as f:
    model = pickle.load(f)

class_labels = model.classes_.tolist()

def predict_premium(input_data):
    df = pd.DataFrame([input_data])
    prediction = model.predict(df)[0]

    # getting probabilities
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # mapping creation
    class_probs = dict(zip(class_labels, map(lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": prediction,
        "confidence": confidence,
        "class_probabilities": class_probs
    }   

