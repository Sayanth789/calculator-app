# main.py
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from database import engine, SessionLocal
from models import Base, Calculation
from calculator import evaluate_expression

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
Base.metadata.create_all(bind=engine)

class CalcRequest(BaseModel):
    expression: str

@app.post("/calculate")
def calculate(req: CalcRequest):
    result = evaluate_expression(req.expression)
    
    # Save to DB only if valid number
    if not isinstance(result, str) or not result.startswith("error"):
        db = SessionLocal()
        calc = Calculation(expression=req.expression, result=result)
        db.add(calc)
        db.commit()
        db.close()
    
    return {"result": result}

@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()