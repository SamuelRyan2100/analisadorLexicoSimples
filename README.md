**É um analisador léxico simplista**


**Gramática:**

<programa>       ::= <comando>*

<comando>        ::= <atribuicao> ";"

<atribuicao>     ::= <identificador> "=" <expressao>

<expressao>      ::= <termo> (("+" | "-") <termo>)*

<termo>          ::= <fator> (("*" | "/") <fator>)*

<fator>          ::= <numero> | <identificador> | "(" <expressao> ")"

<numero>         ::= <inteiro> | <real>

<inteiro>        ::= [0-9]+

<real>           ::= [0-9]+"."[0-9]+

<identificador>  ::= [a-zA-Z_][a-zA-Z0-9_]*


**Linguagem aceita:**
-Identificadores
-Números Intereiros e Reais
-operadores
-Parênteses
-ponto e vírgula(;)
-espaços em branco(eles são ignorados)

