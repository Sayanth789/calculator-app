import requests
import json

OLLAMA_URL = "http://host.docker.internal:11434/api/generate"

SYSTEM_PROMPT = """
You are a strict math conversion engine.

TASK:
Convert natural language math problems into a valid JSON object.

RULES:
- Output ONLY valid JSON
- No explanation, no text, no markdown
- Format: {"expression": "..."}
- Convert percentages to decimals (16% -> 0.16)
- Use only operators: + - * / ( )
- Do NOT include words
"""

def parse_natural_language(text: str):
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

        # 🔴 handle API errors safely
        if "response" not in data:
            return {"error": data}

        raw = data["response"]

        # 🟢 try to parse JSON from model output
        try:
            parsed = json.loads(raw)
        except Exception:
            return {
                "error": "Invalid JSON from model",
                "raw_llm_output": raw
            }

        return parsed

    except Exception as e:
        return {"error": str(e)}