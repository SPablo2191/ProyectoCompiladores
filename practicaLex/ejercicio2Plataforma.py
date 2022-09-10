import sys
import ply.lex as lex

reserved = {
    'subcadena' : 'md'    
}
tokens = [
'letra'
]+list(reserved.values())
t_ignore = r'[ \t]+'
t_letra = r'[a-zA-Z_]+'



def t_error(t):
    print("Error: %s" % repr(t.value[0]))
    t.lexer.skip(1)


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1

def leerTxt():
    try:
        f = open('ejercicio1.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        sys.stdout.write('Reading from stad  input (tye EOF to end) : \n')
        data = sys.stdin.read()
        return data

lexer = lex.lex()
lexer.input(leerTxt())

#Identifica tokens
print('Token - Lexema - Linea')
contMd = 0
while True:
    tok = lexer.token()
    if not tok: 
        print(f"cantidad de subcadenas: {contMd}")
        break
    else:
        if(tok.value.find('md')!=-1):
            contMd += 1