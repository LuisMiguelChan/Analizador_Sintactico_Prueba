import ply.lex as lex
import re
import sys

resultado_lexema = []


tokens = [
    'ENTERO',
    'SUMA',
    'RESTA',
    'MULT',
    'DIV',
    'POTENCIA',
    'MODULO',
    'MINUSMINUS',
    'PLUSPLUS',
    'COMA', 'DECIMAL', 'COMENTARIO','ENTRE',
    'SI', 'SINO', 'VARIABLE',
    'MIENTRAS', 'PARA',
    'AND', 'OR', 'NOT', 'MENORQUE', 'MENORIGUAL', 'MAYORQUE', 'MAYORIGUAL', 'IGUAL', 'DISTINTO',
    'PARENT', 'CORIZQ', 'CORDER', 'LLAIZQ', 'LLADER', 'STRING','COMILLA','COMMA', 'END', 'EQUALS',
    'PRINT', 'PUTS'
]

t_SUMA = r'\+'
t_RESTA = r'\-'
t_MINUSMINUS = r'\-\-'
t_MULT = r'\*'
t_DIV = r'\/'
t_MODULO = r'\%'
t_POTENCIA = r'(\*{2} | \^)'
t_COMILLA = r'["]'
t_COMMA = r'\,'
t_AND = r'\&\&'
t_OR = r'\|{2}'
t_NOT = r'\!'
t_MENORQUE = r'<'
t_MAYORQUE = r'>'
t_CORIZQ = r'\['
t_CORDER = r'\]'
t_LLAIZQ = r'\{'
t_LLADER = r'\}'
t_EQUALS = r'\=\='

# palabras reservadas de PHP

def t_SINO(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_PUTS(t):
    r'puts'
    return t

def t_VARIABLE(t):
    r'[tyr]'
    return t

def t_PARENT(t):
    r'[()]'
    return t

def t_END(t):
    r'end'
    return t

def t_SI(t):
    r'if'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_MIENTRAS(t):
    r'while'
    return t

def t_PARA(t):
    r'for'
    return t

def t_DECIMAL(t):
    r'[0-9]+\.[0-9]+'
    t.value = float(t.value)
    return t

def t_ENTERO(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t

# operacion logica

def t_PLUSPLUS(t):
    r'\+\+'
    return t

def t_MENORIGUAL(t):
    r'<='
    return t

def t_MAYORIGUAL(t):
    r'>='
    return t

def t_IGUAL(t):
    r'='
    return t

def t_MAYORDER(t):
    r'<<'
    return t

def t_MAYORIZQ(t):
    r'>>'
    return t

def t_DISTINTO(t):
    r'!='
    return t

def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

def t_STRING(t):
    r'[a-zA-Z:]+'
    return t

def t_COMENTARIO(t):
    r'/\*(.|\n)*?\*/'
    t.lexer.lineno += t.value.count('\n')
    print("Comentario de multiple linea")

def t_comments_ONELine(t):
    r'\/\/(.)*\n'
    t.lexer.lineno += 1
    print("Comentario de una linea")

t_ignore = '\t'

def t_espacio(t):
    r"\s"
    pass

def t_error(t):
    global resultado_lexema
    estado = "Token no valido en la Linea {:4}".format(str(t.lineno))
    resultado_lexema.append(estado)
    t.lexer.skip(1)

# Prueba de ingreso

def prueba(data):
    global resultado_lexema

    analizador = lex.lex()
    analizador.input(data)
    while True:
        tok = analizador.token()
        if not tok:
            break
        estado = "Linea {:4} Tipo {:4} Valor {:4}".format(
            str(tok.lineno), str(tok.type), str(tok.value))
        resultado_lexema.append(estado)

    return resultado_lexema

# abrir archivo

analizador = lex.lex()

try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea
prueba(text)
print('\n'.join(list(map(''.join, resultado_lexema))))