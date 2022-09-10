import sys
import ply.lex as lex

# List of token names.   This is always required
tokens = [
'letra'
]


# Regular expression rules for simple tokens



# Definir una regla en la que, si sigue esta estructura, hacer algo
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)
# Definir una regla para contar las minusculas o mayusculas

    

# A string co|ntaining ignored characters (spaces and tabs)
t_letra = r'[a-zA-Z_]+'
t_ignore = r'[ \t]+'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


# Build the lexer
lexer = lex.lex()




# Test it out
def leerTxt():
    try:
        f = open('ejercicio1.txt', 'r')
        data = f.read()
        f.close()
        return data
    except:
        return ""

# Give the lexer some input
lexer.input(leerTxt())

# Tokenize
contMay = 0
contMin = 0
while True:
    
    tok = lexer.token()
    if not tok:
        print(f"Minusculas encontradas: {contMin}") 
        print(f"Mayusculas encontradas: {contMay}")
        break
    else:
        if(tok.value == tok.value.lower()):
            contMin +=1
            
        else:
            if(tok.value == tok.value.upper()):
                contMay +=1  # No more input
