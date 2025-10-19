import re

# Definição dos tokens 
token_specification = [
    # Palavras-chave
    ("IF",            r'\bif\b'),
    ("ELSE",          r'\belse\b'),
    ("WHILE",         r'\bwhile\b'),
    ("TRUE",          r'\btrue\b'),
    ("FALSE",         r'\bfalse\b'),

    # Operadores relacionais e lógicos
    ("IGUALDADE",     r'=='),
    ("DIFERENTE",     r'!='),
    ("MAIOR_IGUAL",   r'>='),
    ("MENOR_IGUAL",   r'<='),
    ("AND",           r'&&'),
    ("OR",            r'\|\|'),

    # Operadores simples
    ("ATRIBUICAO",    r'='),
    ("MAIOR",         r'>'),
    ("MENOR",         r'<'),
    ("OPERADOR",      r'[+\-*/]'),

    # Números e identificadores
    ("NUMERO_REAL",   r'\d+\.\d+(?!\d)'),
    ("NUMERO_INT",    r'\d+(?!\.\d)'),
    ("IDENTIFICADOR", r'[a-zA-Z_][a-zA-Z0-9_]*'),

    # Símbolos
    ("ABRE_PAR",      r'\('),
    ("FECHA_PAR",     r'\)'),
    ("ABRE_CHAVE",    r'\{'),
    ("FECHA_CHAVE",   r'\}'),
    ("PONTO_VIRGULA", r';'),

    # Espaços e erro
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
            raise SyntaxError(f"Erro léxico: {valor}")
        else:
            tokens.append((tipo, valor))
    return tokens



# Ler código
with open("codigo.txt", "r", encoding="utf-8") as f:
    codigo = f.read()

resultado = analisar_codigo(codigo)

for token in resultado:
    print(token)
