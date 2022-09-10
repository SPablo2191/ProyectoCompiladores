import os
import sys
import ply.lex as lex
reserved = {
    'if': 'if',
    'then': 'then',
    'else': 'else',
    'while': 'while',

}
tokens = [
    "NUMERO",
    "punto",
    "suma",
    "resta",
    "producto",
    "division",
    "parent_inicial",
    "parent_final",
    "ID"] + list(reserved.values())
print(tokens)
# Expresiones regulares
# t_ID = r'[a-zA-Z_][a-zA-Z0-9_]*'
t_NUMERO = r'[0-9]+'
t_ignore = r'[ ]+'
t_suma = r'\+'
t_resta = r'\-'
t_producto = r'\*'
t_division = r'\/'
t_parent_inicial = r'\('
t_parent_final = r'\)'
t_punto = r'[.]'


def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved:
        t.type = reserved[t.value]
    return t


def t_error(t):
    print("Error: %s" % repr(t.value[0]))
    t.lexer.skip(1)


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


def leerTxt():
    try:
        f = open('ejemplo.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        sys.stdout.write('Reading from stad  input (tye EOF to end) : \n')
        data = sys.stdin.read()
        return data


lexer = lex.lex()
lexer.input(leerTxt())

# Identifica tokens
print('Token - Lexema - Linea')
while True:
    tok = lexer.token()
    if not tok:
        break
    print('(', tok.type, ',', tok.value, ',', tok.lineno, ')')
