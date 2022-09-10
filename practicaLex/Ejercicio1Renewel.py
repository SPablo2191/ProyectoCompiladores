import sys
import ply.lex as lex
tokens =['numero']
t_numero = r'[0-9][0-9]+'
t_ignore = r'[ \t]+'


# Error handling rule

def t_error(t):
    print("Error: %s" % repr(t.value[0]))
    t.lexer.skip(1)


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def leerTxt():
    try:
        f = open('ejercicioDesafio.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        sys.stdout.write('Reading from stad  input (tye EOF to end) : \n')
        data = sys.stdin.read()
        return data

lexer = lex.lex()
lexer.input(leerTxt())
print('Token - Lexema - Linea')
contMd = 0
while True:
    tok = lexer.token()
    if not tok:
        print(contMd)
        break
    else:
        if tok.type == 'numero':
            contMd += 1
        