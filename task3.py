# Import FastAPI to create the API and HTTPException to handle errors
from fastapi import FastAPI, HTTPException

# Import BaseModel from Pydantic to define request body structure
from pydantic import BaseModel

# Create FastAPI app
app = FastAPI()


# ----------- Request Models -----------

# Model for numbers input
# This defines the structure of data the API expects
class Numbers(BaseModel):
    num1: float
    num2: float


# Model for text input
class TextInput(BaseModel):
    text: str


# ----------- API 1 : Sum of two numbers -----------

# Endpoint to calculate the sum of two numbers
@app.post("/sum")
def calculate_sum(numbers: Numbers):
    
    try:
        # Add the two numbers provided in the request
        result = numbers.num1 + numbers.num2
        
        # Return the result as a JSON response
        return {"sum": result}
    
    except Exception:
        # If something goes wrong, return a user-friendly error
        raise HTTPException(
            status_code=400,
            detail="Invalid input. Please provide numbers only."
        )


# ----------- API 2 : Convert string to uppercase -----------

# Endpoint to convert a lowercase string to uppercase
@app.post("/uppercase")
def convert_uppercase(input_text: TextInput):

    # Get the text from the request body
    text = input_text.text
    
    # Check if the input text is lowercase
    if not text.islower():
        raise HTTPException(
            status_code=400,
            detail="Input must be a lowercase string."
        )

    # Convert text to uppercase and return it
    return {"uppercase_text": text.upper()}