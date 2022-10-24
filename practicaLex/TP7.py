import sys
import ply.lex as lex

# List of token names.   This is always required
tokens = [
    'num',
    'sum',
    'por',
    'parBegin',
    'parEnd'
]


# Regular expression rules for simple tokens




# A string co|ntaining ignored characters (spaces and tabs)
t_sum = r'\+'
t_por = r'\*'
t_parBegin = r'\('
t_parEnd = r'\)'

# Definir una regla en la que, si sigue esta estructura, hacer algo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Definir una regla para contar las minusculas o mayusculas

def t_num(t):
    r'\d+'
    t.value = int(t.value)
    return t
# Error handling rule


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer


# Test it out
def leerTxt():
    try:
        f = open('ejercicio7.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        return ""


# Give the lexer some input
print(leerTxt())
lexer = lex.lex()
lexer.input('2+5+(4*2)')

# Tokenize
# Identifica tokens
# print('Token - Lexema - Linea')
# while True:
#     tok = lexer.token()
#     if not tok:
#         print("holis")
#         break
#     print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
# Parsing rules

precedence = (
    ('left','sum'),
    ('left','por')
    )

# dictionary of names
names = { }


def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression sum expression
                  | expression por expression
                  '''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]


def p_expression_group(t):
    'expression : parBegin expression parEnd'
    t[0] = t[2]

def p_expression_number(t):
    'expression : num'
    t[0] = t[1]


def p_error(t):
    print("Syntax error at '%s'" % t.value)


import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = '2'   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)