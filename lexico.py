import re

# Definição dos tokens (expressões regulares)
token_specification = [
    ("IF",            r'\bif\b'),
    ("ELSE",          r'\belse\b'),
    ("WHILE",         r'\bwhile\b'),
    ("TRUE",          r'\btrue\b'),
    ("FALSE",         r'\bfalse\b'),
    ("NUMERO_REAL",   r'\d+\.\d+(?!\d)'),   # número real, ex: 20.5
    ("NUMERO_INT",    r'\d+(?!\.\d)'),      # inteiro, mas não seguido de ponto
    ("IDENTIFICADOR", r'[a-zA-Z_][a-zA-Z0-9_]*'),
    ("OPERADOR",      r'[+\-*/=<>!]'),      # já pega alguns operadores básicos
    ("ABRE_PAR",      r'\('),
    ("FECHA_PAR",     r'\)'),
    ("ABRE_CHAVE",    r'\{'),
    ("FECHA_CHAVE",   r'\}'),
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
if (x == true) {
    y = 10;
} else {
    while (y > 1.1) {
        y = y - 1;
    }
}
"""

resultado = analisar_codigo(codigo)
for token in resultado:
    print(token)
