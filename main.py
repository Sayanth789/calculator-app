from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
import math

from database import engine, SessionLocal
from models import Base, Calculation


app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

# create tables automatically
Base.metadata.create_all(bind=engine)

SAFE_MATH = {
    "pi": math.pi,
    "e": math.e,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "sqrt": math.sqrt,
    "log": math.log
}


class CalcRequest(BaseModel):
    expression: str


@app.post("/calculate")
def calculate(req: CalcRequest):

    try:

        result = eval(req.expression, {"__builtins__": {}}, SAFE_MATH)

        db = SessionLocal()

        calc = Calculation(
            expression=req.expression,
            result=result
        )

        db.add(calc)
        db.commit()
        db.close()

        return {"result": result}

    except Exception as e:
        return {"error": str(e)}


@app.get("/", response_class=HTMLResponse)
def home():
    with open("static/index.html") as f:
        return f.read()