import requests
import json
from services.fallback_parser import fallback_expression



OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

SYSTEM_PROMPT = """
YOU ARE A STRICT MATH PARSING ENGINE.

YOUR ONLY TASK:
Convert natural language math problems into a structured JSON response.

================================================
🚨 OUTPUT FORMAT (ABSOLUTE RULE - MUST FOLLOW)
================================================

Return ONLY valid JSON. No markdown. No explanation. No extra text.

EXACT FORMAT:

{
  "mode": "solve" or "clarify",
  "expression": "...",
  "label": "...",
  "question": ""
}

If you output anything outside JSON → it is INVALID.

================================================
🧠 MODE RULES
================================================

If the math problem is solvable:
- mode = "solve"
- expression = valid Python math expression
- label = short description of result
- question = ""

If missing information:
- mode = "clarify"
- expression = ""
- label = ""
- question = ask only what is missing

DO NOT guess missing values.

================================================
🧮 MATH RULES
================================================

1. BASIC OPERATIONS:
- plus, add → +
- minus, subtract → -
- times, into, multiplied by → *
- divided by, over → /

2. IGNORE CONTEXT WORDS:
Ignore words that do NOT affect math:
income, salary, cost, expense, profit, total, amount

3. PERCENTAGE RULES:
- X% of Y → Y * (X / 100)

- Y after X% tax → Y * (1 - X / 100)

- Y after X% discount → Y * (1 - X / 100)

- increase Y by X% → Y * (1 + X / 100)

- decrease Y by X% → Y * (1 - X / 100)

4. SPLIT RULE:
- split X among Y people → X / Y

================================================
📌 OUTPUT RULES
================================================

- expression MUST be a valid Python math expression
- NO words inside expression
- NO explanations outside JSON
- NO extra keys allowed

================================================
📌 EXAMPLES
================================================

Input: income 30000 minus 12000
Output:
{"mode":"solve","expression":"30000-12000","label":"Result","question":""}

Input: 12000 after 12% tax
Output:
{"mode":"solve","expression":"12000*(1-12/100)","label":"After tax","question":""}

Input: 12% of 12000
Output:
{"mode":"solve","expression":"12000*(12/100)","label":"Percentage","question":""}

Input: increase 100 by 10%
Output:
{"mode":"solve","expression":"100*(1+10/100)","label":"Increase","question":""}

Input: split 5000 among 5 people
Output:
{"mode":"solve","expression":"5000/5","label":"Split","question":""}

Input: split 5000 among people
Output:
{"mode":"clarify","expression":"","label":"","question":"How many people?"}
"""

def call_ai_mode(text: str):
    try:
        response = requests.post(
            OLLAMA_URL,
            json={
                "model": "llama3:8b",
                "prompt": SYSTEM_PROMPT + "\nInput: " + text,
                "stream": False
            }
        )

        data = response.json()

        if "response" not in data:
            return None

        raw = data["response"]

        try:
            return json.loads(raw)
        except:
            return None

    except:
        return None
'''
we done this to prevent the error as occured when we
try the input `income 30000 minus 12000`

'''

def parse_natural_language(text: str):
    # AI attempt 
    result = call_ai_mode(text)

    # Fallback if AI fails OR empty expression 
    if not result or not result.get("expression"):
        expr = fallback_expression(text)

        return {
            "mode": "solve",
            "expression": expr,
            "label": " answer is: ",
            "question": ""
        }
    
    return result