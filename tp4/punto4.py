import sys
import ply.lex as lex


tokens = ["word", "htmlBegin","headBegin","titleBegin","titleEnd"
,"headEnd","body","parBegin","boldBegin","boldEnd","horRule","parEnd"]
t_word = r'([a-z|A-Z|0-9|_|.|,|¡|!|¿|?|"|\'|(|)|{|}|[|\]|\s])+'
t_htmlBegin = r'[<][H][T][M][L][>]'
t_headBegin = r'[<][H][E][A][D][>]'
t_titleBegin = r'[<][T][I][T][L][E][>]'
t_titleEnd = r'[<][/][T][I][T][L][E][>]'
t_headEnd = r'[<][/][H][E][A][D][>]'
t_body = r'[<][B][O][D][Y][>]'
t_parBegin = r'[<][P][>]'
t_boldBegin = r'[<][B][>]'
t_boldEnd = r'[<][/][B][>]'
t_horRule = r'[<][H][R][>]'
t_parEnd = r'[<][/][P][>]'
t_ignore = r'[ ]+'


def t_error(t):
    print(f"ERROR: la cadena {t.value} no es aceptada")
    t.lexer.skip(len(t.value))


def t_newline(t):
    r'\n'
    t.lexer.lineno += 1


def leerTxt():
    try:
        f = open(
            'D:/uni/4 año/2do semestre/compiladores/ProyectoCompiladores/tp4/punto4.txt', 'r')
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
