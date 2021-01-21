import ply.yacc as yacc
from analizador_lexico import tokens
import sys
import ply.lex as lex

#Array o lista donde se almacenaran los resultados.
resultado_gramatica = []

#Definicion de procedencias y formas de derivación
#Lectura hacia la izquierda o derecha.
precedence = (
    ('left', 'SI', 'SINO',),
    ('left', 'COMMA'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULT', 'DIV'),
    ('right', 'END'),
    ('right', 'ENTERO'),
    ('left', 'EQUALS'),
    ('left', 'MIENTRAS'),
)

#Se definen todas la reglas gramaticales
#Definición de declaraciones
def p_declaracion_coditionif(t):
    'declaracion : SI'
    t[0] = t[1]

def p_declaracion_coditionwhile(t):
    'declaracion : MIENTRAS'
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

#Declaracion de operaciones con expresiones
def p_expresion_operaciones(t):
    '''
    expresion  :   expresion SUMA expresion
                |   expresion RESTA expresion
                |   expresion MULT expresion
                |   expresion DIV expresion
                |   expresion POTENCIA expresion
                |   expresion MODULO expresion
                |   expresion EQUALS expresion
                |   PARENTIZQ expresion SUMA expresion PARENTDER MULT expresion
                |   PARENTIZQ expresion SUMA expresion PARENTDER expresion
                |   PARENTIZQ expresion SUMA expresion PARENTDER DIV expresion
                |   PARENTIZQ expresion RESTA expresion PARENTDER MULT expresion
                |   PARENTIZQ expresion RESTA expresion PARENTDER expresion
                |   PARENTIZQ expresion RESTA expresion PARENTDER DIV expresion
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
    elif t[2] == '==':
        t[0] = t[1] % t[3]
    elif t[2] == '**':
        i = t[3]
        t[0] = t[1]
        while i > 1:
            t[0] *= t[1]
            i -= 1

#Gramaticas de grupo, declaracion de los posibles utiles en el codigo
def p_expresion_grupo(t):
    '''
    expresion  : PRINT PARENTIZQ VARIABLE PARENTDER
                | PUTS PARENTIZQ VARIABLE PARENTDER
                | PRINT PARENTIZQ STRING PARENTDER
                | PRINT PARENTIZQ STRING COMMA VARIABLE PARENTDER
    '''
    t[0] = t[3]

#Uso de expresiones logicas, definición de posibles usos
def p_expresion_logicas(t):
    '''
    expresion   :  expresion MENORQUE expresion 
                |  expresion MAYORQUE expresion 
                |  expresion MENORIGUAL expresion 
                |   expresion MAYORIGUAL expresion 
                |   expresion IGUAL expresion 
                |   expresion DISTINTO expresion
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

#Definicion de expresiones
def p_expresion_numero(t):
    'expresion : ENTERO'
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

#En caso de errores gramaticales pasa por el siguiente metodo
def p_error(t):
    global resultado_gramatica
    if t:
        resultado = "Error sintactico de tipo {:4} en el valor {:4}".format(
            str(t.type), str(t.value))#Define donde se encuentra el error sintactico
    else:
        resultado = "Error sintactico {}".format(t) #Muestra un error de sintaxis
    resultado_gramatica.append(resultado)

parser = yacc.yacc()

#Proceso de analisis del codigo
def prueba_sintactica(data):
    global resultado_gramatica
   
    for item in data.splitlines(): #Saltos que da el puntero de analisis
        if item:
            gram = parser.parse(item)#Analiza cada item con respecto a la libreria yacc
            if gram:
                resultado_gramatica
        else:
            print()
    return resultado_gramatica

try:
    file_name = sys.argv[1] #Lectura del archivo
    archivo = open(file_name, "r")
except:
    print("el archivo no se encontro")#En caso de encontrar el archivo
    quit()

text = ""
for linea in archivo:#Lee el archivo linea a linea
    text += linea

prueba_sintactica(text)
print("")
print('******** PRUEBA DE ERRORES *********')
print("")
print('\n'.join(list(map(''.join, resultado_gramatica))))#Emite una lista con los resultados del analisis
print('-------------------------------------------------')