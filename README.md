**É um analisador léxico que suporta um subonjunto de uma linguagem imperativa simples**


**Gramática:**

<programa> ::= <comando_lista>

<comando_lista> ::= <comando> <comando_lista> | ε

<comando> ::= <atribuicao> ";"
             | <se>
             | <enquanto>
             | "{" <comando_lista> "}"

<atribuicao> ::= <identificador> "=" <expressao>

<se> ::= "if" "(" <expressao> ")" <comando> <senao_opcional>

<senao_opcional> ::= "else" <comando> | ε

<enquanto> ::= "while" "(" <expressao> ")" <comando>

<expressao> ::= <expressao_logica>

<expressao_logica> ::= <expressao_relacional> <op_logico> <expressao_logica>
                     | <expressao_relacional>

<op_logico> ::= "&&" | "||"

<expressao_relacional> ::= <expressao_aritmetica> <op_relacional> <expressao_aritmetica>
                         | <expressao_aritmetica>

<op_relacional> ::= "==" | "!=" | ">" | "<" | ">=" | "<="

<expressao_aritmetica> ::= <termo> { ("+" | "-") <termo> }

<termo> ::= <fator> { ("*" | "/") <fator> }

<fator> ::= <numero>
           | <booleano>
           | <identificador>
           | "(" <expressao> ")"

<booleano> ::= "true" | "false"

<numero> ::= <NUMERO_INT> | <NUMERO_REAL>

<identificador> ::= <IDENTIFICADOR>



**Linguagem aceita:**
A linguagem é um subconjunto de uma linguagem de programação imperativa simples, contendo:

Identificadores → nomes de variáveis e funções: [a-zA-Z_][a-zA-Z0-9_]*

Números inteiros 

Números reais 

Palavras-chave → if, else, while, true, false

Operadores aritméticos → +, -, *, /

Operadores relacionais → ==, !=, >, <, >=, <=

Operadores lógicos → &&, ||

Atribuição → =

Delimitadores → ( ) { } ;

Espaços e quebras de linha → ignorados pelo léxico

👉 Em resumo, a linguagem aceita é uma linguagem de programação imperativa simplificada, com controle de fluxo (if, else, while), expressões aritméticas, booleanas e atribuição.

