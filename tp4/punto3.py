import sys
import ply.lex as lex
tokens = ["beginOne","beginZero"]
t_beginOne = r'([1][0|1|2|3|4|5|6|7|8|9]*[0][0])'
t_ignore = r'[ ]+'
t_beginZero = r'([0][0|1|2|3|4|5|6|7|8|9]*[1][1])'



def t_error(t):
    print(f"ERROR: la cadena {t.value} no es aceptada")
    t.lexer.skip(len(t.value))


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


def leerTxt():
    try:
        f = open('D:/uni/4 año/2do semestre/compiladores/ProyectoCompiladores/tp4/punto3.txt', 'r')
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