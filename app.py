##Importing required libraries 
import uvicorn 
from fastapi import FastAPI 
from BankNotes import BankNote 
import numpy as np
import pandas as pd
import pickle 

##create app object
app = FastAPI()

pickle_in= open('classifier.pkl', 'rb')
classifier = pickle.load(pickle_in)

# Index route, opens automatically on http://127.0.0.1:8000  
@app.get('/')
def index():
    return {'message': 'Hello, world!!!!'}

# Route with a single parameter, returns the parameters within a passage,
 # located at http://127.0.0.1:8000
@app.get('/{name}')
def get_name(name: str):
    return {"Welcome to Wakanda": f'{name}'}
## Exposed the prediction functionality, make a prediction from the passed 
## JSON data and return the predicted Bank Note with the confidence.

@app.post('/predict')
def predict_banknote(data: BankNote):
    data = data.dict()
    variance = data['variance']
    skewness = data['skewness']
    curtosis = data['curtosis']
    entropy  = data['entropy']
    
    prediction = classifier.predict([[variance, skewness, curtosis, entropy]])
    if (prediction[0]>0.5):
        prediction = "Fake Note"
    else:
        prediction = "Its a Bank note"
    return {
        "prediction": prediction}

## Run the API with uvicorn, will run on http://127.0.0.1:8000 

if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
    
#uvicorn app:app --reload 
