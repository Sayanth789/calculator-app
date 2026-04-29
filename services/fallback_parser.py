import re

'''
a rule based mini parser that sanitize natural language into math-safe expression.

The workflow is this:
AI parser (tries to understand full sentence). Can fail or empty 
                |
                v
Fallback parser (./)
                |
                v
Valid math expresion -> evaluator.




'''

def fallback_expression(text):
    text = text.lower()

    # 1. remove context words
    remove_words = [
        "income", "salary", "cost", "expense",
        "profit", "total", "amount"
    ]

    for word in remove_words:
        text = text.replace(word, "")

    # 2. convert words to operators
    text = text.replace("plus", "+")
    text = text.replace("minus", "-")
    text = text.replace("into", "*")
    text = text.replace("times", "*")
    text = text.replace("multiplied by", "*")
    text = text.replace("divided by", "/")

    # 3. extract ONLY valid math tokens (critical fix)
    tokens = re.findall(r"\d+|[\+\-\*/\(\)]", text)

    if not tokens:
        return "0"

    return "".join(tokens)