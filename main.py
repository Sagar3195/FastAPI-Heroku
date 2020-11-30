##pip install fastapi uvicorn

##importing required libraries
import uvicorn  ##ASGI 
from fastapi import FastAPI 

##now create app object
app = FastAPI()

#Index route, opens automatically on http://127.0.0.1:8000 
@app.get('/') 
def index():
    return {"message": "Heyy Yoouu!!!"}

## Route with a single parameters, returns the parameter within a message
## Locate at :http://127.0.0.1:8000/AnyNameHere
@app.get('/welcome')
def get_name(name: str):
    return {"Welcome to Wakanda": f'{name}'}

## Run the API with uvicorn     
##It will run on http://127.0.0.1:8000 
if __name__ == "__main__":
    uvicorn.run(app, host = '127.0.0.1', port = 8000)
    
##uvicorn main:app --reload   
 
