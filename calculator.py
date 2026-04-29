import math

SAFE_MATH = {
    "pi": math.pi,
    "e": math.e,
    "sin": lambda x: math.sin(math.radians(x)),
    "cos": lambda x: math.cos(math.radians(x)),
    "tan": lambda x: math.tan(math.radians(x)),
    "sqrt": math.sqrt,
    "log": math.log
}

def evaluate_expression(expr: str):
    """Evaluate a math expression safely using SAFE_MATH."""
    try:
        return eval(expr, {"__builtins__": {}}, SAFE_MATH)
    except Exception as e:
        return f"error: {str(e)}"
    
def evaluate_expression(expr: str):
    """
     Only evaluates CLEAN mathematical expressions.
     AI must already convert natural language → expression.
    """    
    try:
        # small normalization step (important).
        expr = expr.replace("^", "**")

        result = eval(expr, {"__builtins__", {}}, SAFE_MATH)
        return result
    
    except Exception as e:
        return f"error: {str(e)}"