import re
#token patterns
TOKENS = [
    ("COMMENT", r"//.|/\[\s\S]?\/"),     
    ("KEYWORD", r"\b(int|if|else|return)\b"), 
    ("IDENTIFIER", r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"), 
    ("NUMBER", r"\b\d+\b"),                   
    ("OPERATOR", r"[+\-*/=]"),               
    ("PUNCTUATION", r"[();{}]"),              
    ("STRING", r"\".*?\""),             
]

def scanner(code):
    tokens = []
    position = 0

    while position < len(code):
        match = None
        for token_type, pattern in TOKENS:
            regex = re.compile(pattern)
            match = regex.match(code, position)
            if match:
                token_value = match.group(0)
                tokens.append((token_type, token_value))
                position = match.end(0)
                break
        if not match:
            position += 1  # Skip any unknown character

    return tokens

# Example usage
code = input("inter the code")
tokens = scanner(code)
for key,value in tokens:
    print(f"Token tybe : {key}, Token value :  {value}")
