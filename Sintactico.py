import ply.yacc as yacc
from analizador_lexico import tokens
import sys
import ply.lex as lex 
import re

resultado_gramatica = []

precedence = (
    ('right', 'SI', 'SINO',),
    ('right', 'STRING'),
    ('left', 'PARENT'),
    ('right', 'COMMA'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'END'),
    ('right', 'ENTERO'),
    ('right', 'EQUALS'),
    ('right', 'COMILLA'),
    ('right', 'VARIABLE'),
    ('right', 'PRINT'),
    ('right', 'PUTS'),
)
nombres = {}

def p_declaracion_coditionif(t):
    'declaracion : SI'
    t[0] = t[1]

def p_declaracion_EQUALS(t):
    'declaracion : EQUALS'
    t[0] = t[1]

def p_declaracion_coditionelse(t):
    'declaracion : SINO'
    t[0] = t[1]

def p_declaracion_comma(t):
    'expresion :  COMMA'
    t[0] = t[1]

def p_declaracion_expr(t):
    'declaracion : expresion'
    t[0] = t[1]

def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion
    '''
    if t[2] == '+':
        t[0] = t[1] + t[3]
    if t[2] == '-':
        t[0] = t[1] + t[3]
    if t[2] == '*':
        t[0] = t[1] + t[3]
    if t[2] == '/':
        t[0] = t[1] + t[3]
    elif t[2] == '%':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

def p_expresion_grupo(t):
    '''
    expresion  : LLAIZQ expresion LLADER
                | CORIZQ expresion CORDER
    '''
    t[0] = t[2]

# sintactico de expresiones logicas
    
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
                |   expresion PARENT expresion
                |   expresion STRING expresion
    '''
    if t[2] == "<":
        t[0] = t[1] < t[3]
    elif t[2] == ">":
        t[0] = t[1] > t[3]
    elif t[2] == "<=":
        t[0] = t[1] <= t[3]
    elif t[2] == ">=":
        t[0] = t[1] >= t[3]
    elif t[2] == "=":
        t[0] = t[1] is t[3]
    elif t[2] == "!=":
        t[0] = t[1] != t[3]

def p_expresion_numero(t):
    'expresion : ENTERO'
    t[0] = t[1]

def p_expresion_print(t):
    'expresion : PRINT'
    t[0] = t[1]

def p_expresion_puts(t):
    'expresion : PUTS'
    t[0] = t[1]

def p_comilla(t):
    'expresion : COMILLA'
    t[0] = t[1]

def p_expresion_decimal(t):
    'expresion : DECIMAL'
    t[0] = t[1]

def p_expresion_variable(t):
    'expresion : VARIABLE'
    t[0] = t[1]

def p_expresion_end(t):
    'expresion : END'
    t[0] = t[1]

def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))
    else:
        resultado = "Error sintactico {}".format(t)
    resultado_gramatica.append(resultado)

parser = yacc.yacc()

def prueba_sintactica(data):
    global resultado_gramatica
   
    for item in data.splitlines():
        if item:
            gram = parser.parse(item)
            if gram:
                resultado_gramatica.append(str(gram))
        else:
            print("")
    return resultado_gramatica

try:
    file_name = sys.argv[1]
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")
    quit()

text = ""
for linea in archivo:
    text += linea

prueba_sintactica(text)
print("")
print('******** PRUEBA DE ERRORES *********')
print("")
print('\n'.join(list(map(''.join, resultado_gramatica))))
print('-------------------------------------------------')