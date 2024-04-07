import re

# Definindo os tipos de tokens
tokens = (
    'NUM_INT', 'NUM_FLOAT', 'OPERATOR', 'DELIMITER', 'IDENTIFIER', 'COMMAND', 'STRING', 'COMMENT', 'BOOLEAN'
)

# Utilizando Regex para definir os tokens
t_NUM_INT = r'\b\d+\b'
t_NUM_FLOAT = r'\b\d+\.\d+\b'
t_OPERATOR = r'\+|-|\*|/|==|!=|<|>|<=|>=|='
t_DELIMITER = r'\(|\)|\{|\}|\[|\]|,|;'
t_IDENTIFIER = r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'
t_COMMAND = r'\bif|else|for|while|print|return\b'
t_BOOLEAN = r'\bTrue|False\b'
t_STRING = r'\".*?\"'
t_COMMENT = r'\#.*'

t_ignore = ' \t'

# Lidando com erros
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Construindo o lexer
import ply.lex as lex
lexer = lex.lex()

# Testando o lexer
data = input("Digite o texto a ser reconhecido: ")

lexer.input(data)

# Criando um contador de tokens
typesCount = {
}

# Printando os tokens
# Escolhendo como printar os tokens
while True:
    resposta = input("Deseja visualizar o valor de cada token : (S/N)")
    if resposta.upper() in ['S', 'N']:
        break
    else:
        print("Resposta inválida. Por favor, responda com 'S' ou 'N'.")

while True:
    tok = lexer.token()
    if not tok: 
        break

    if tok.type in typesCount:
        typesCount[tok.type] += 1
    else:
        typesCount[tok.type] = 1
    
    if resposta == "S":
        print(f"Tipo: {tok.type}, Valor: {tok.value}")


print("\n--- Relatório dos Tokens Encontrados ---")
for typesCount, count in typesCount.items():
    print(f"Tipo: {typesCount}, Contagem: {count}")