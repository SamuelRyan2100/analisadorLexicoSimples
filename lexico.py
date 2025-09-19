import re

# Definição dos tokens (expressões regulares)
token_specification = [
    ("NUMERO_REAL",   r'\d+\.\d+(?!\d)'),   # número real, ex: 20.5
    ("NUMERO_INT",    r'\d+(?!\.\d)'),      # inteiro, mas não seguido de ponto
    ("IDENTIFICADOR", r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ("OPERADOR",      r'[+\-*/=]'),
    ("ABRE_PAR",      r'\('),
    ("FECHA_PAR",     r'\)'),
    ("PONTO_VIRGULA", r';'),
    ("ESPACO",        r'[ \t\n]+'),
    ("ERRO",          r'.'),
]


# Compila a regex combinada
regex = '|'.join(f'(?P<{nome}>{padrao})' for nome, padrao in token_specification)
token_re = re.compile(regex)

def analisar_codigo(codigo):
    tokens = []
    for match in token_re.finditer(codigo):
        tipo = match.lastgroup
        valor = match.group()
        if tipo == "ESPACO":
            continue
        elif tipo == "ERRO":
            raise SyntaxError(f"Caractere inválido: {valor}")
        else:
            tokens.append((tipo, valor))
    return tokens


# 🔹 Testando
codigo = """
x = (10 + 20.5) * 3;
y = x / 2;
"""

resultado = analisar_codigo(codigo)
for token in resultado:
    print(token)
