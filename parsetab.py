
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightSISINOleftCOMMAleftSUMARESTAleftMULTDIVrightENDrightENTEROrightEQUALSrightMIENTRASCOMMA CORDER CORIZQ DECIMAL DISTINTO DIV END ENTERO EQUALS IGUAL LLADER LLAIZQ MAYORIGUAL MAYORQUE MENORIGUAL MENORQUE MIENTRAS MODULO MULT PARENTDER PARENTIZQ POTENCIA PRINT PUTS RESTA SI SINO STRING SUMA VARIABLEdeclaracion : SIdeclaracion : MIENTRASdeclaracion : SINOexpresion :  COMMAdeclaracion : expresion\n    expresion  :   expresion SUMA expresion\n                |   expresion RESTA expresion\n                |   expresion MULT expresion\n                |   expresion DIV expresion\n                |   expresion POTENCIA expresion\n                |   expresion MODULO expresion\n                |   expresion EQUALS expresion\n    \n    expresion  : PRINT PARENTIZQ VARIABLE PARENTDER\n                | PUTS PARENTIZQ VARIABLE PARENTDER\n                | PRINT PARENTIZQ STRING PARENTDER\n                | PRINT PARENTIZQ STRING COMMA VARIABLE PARENTDER\n    \n    expresion   :  expresion MENORQUE expresion \n                |  expresion MAYORQUE expresion \n                |  expresion MENORIGUAL expresion \n                |   expresion MAYORIGUAL expresion \n                |   expresion IGUAL expresion \n                |   expresion DISTINTO expresion\n    expresion : ENTEROexpresion : DECIMALexpresion : VARIABLEexpresion : END'
    
_lr_action_items = {'SI':([0,],[2,]),'MIENTRAS':([0,],[3,]),'SINO':([0,],[4,]),'COMMA':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,42,],[6,6,6,6,6,6,6,6,6,6,6,6,6,6,46,]),'PRINT':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[7,7,7,7,7,7,7,7,7,7,7,7,7,7,]),'PUTS':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[9,9,9,9,9,9,9,9,9,9,9,9,9,9,]),'ENTERO':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[10,10,10,10,10,10,10,10,10,10,10,10,10,10,]),'DECIMAL':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[11,11,11,11,11,11,11,11,11,11,11,11,11,11,]),'VARIABLE':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,46,],[8,8,8,8,8,8,8,8,8,8,8,8,8,8,41,43,48,]),'END':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[12,12,12,12,12,12,12,12,12,12,12,12,12,12,]),'$end':([1,2,3,4,5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[0,-1,-2,-3,-5,-4,-25,-23,-24,-26,-6,-7,-8,-9,-10,-11,-12,-17,-18,-19,-20,-21,-22,-13,-15,-14,-16,]),'SUMA':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[13,-4,-25,-23,-24,-26,-6,-7,-8,-9,13,13,-12,13,13,13,13,13,13,-13,-15,-14,-16,]),'RESTA':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[14,-4,-25,-23,-24,-26,-6,-7,-8,-9,14,14,-12,14,14,14,14,14,14,-13,-15,-14,-16,]),'MULT':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[15,-4,-25,-23,-24,-26,15,15,-8,-9,15,15,-12,15,15,15,15,15,15,-13,-15,-14,-16,]),'DIV':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[16,-4,-25,-23,-24,-26,16,16,-8,-9,16,16,-12,16,16,16,16,16,16,-13,-15,-14,-16,]),'POTENCIA':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[17,-4,-25,-23,-24,-26,-6,-7,-8,-9,17,17,-12,17,17,17,17,17,17,-13,-15,-14,-16,]),'MODULO':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[18,-4,-25,-23,-24,-26,-6,-7,-8,-9,18,18,-12,18,18,18,18,18,18,-13,-15,-14,-16,]),'EQUALS':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[19,-4,-25,-23,-24,-26,19,19,19,19,19,19,19,19,19,19,19,19,19,-13,-15,-14,-16,]),'MENORQUE':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[20,-4,-25,-23,-24,-26,-6,-7,-8,-9,20,20,-12,20,20,20,20,20,20,-13,-15,-14,-16,]),'MAYORQUE':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[21,-4,-25,-23,-24,-26,-6,-7,-8,-9,21,21,-12,21,21,21,21,21,21,-13,-15,-14,-16,]),'MENORIGUAL':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[22,-4,-25,-23,-24,-26,-6,-7,-8,-9,22,22,-12,22,22,22,22,22,22,-13,-15,-14,-16,]),'MAYORIGUAL':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[23,-4,-25,-23,-24,-26,-6,-7,-8,-9,23,23,-12,23,23,23,23,23,23,-13,-15,-14,-16,]),'IGUAL':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[24,-4,-25,-23,-24,-26,-6,-7,-8,-9,24,24,-12,24,24,24,24,24,24,-13,-15,-14,-16,]),'DISTINTO':([5,6,8,10,11,12,28,29,30,31,32,33,34,35,36,37,38,39,40,44,45,47,49,],[25,-4,-25,-23,-24,-26,-6,-7,-8,-9,25,25,-12,25,25,25,25,25,25,-13,-15,-14,-16,]),'PARENTIZQ':([7,9,],[26,27,]),'STRING':([26,],[42,]),'PARENTDER':([41,42,43,48,],[44,45,47,49,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'declaracion':([0,],[1,]),'expresion':([0,13,14,15,16,17,18,19,20,21,22,23,24,25,],[5,28,29,30,31,32,33,34,35,36,37,38,39,40,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> declaracion","S'",1,None,None,None),
  ('declaracion -> SI','declaracion',1,'p_declaracion_coditionif','Sintactico.py',21),
  ('declaracion -> MIENTRAS','declaracion',1,'p_declaracion_coditionwhile','Sintactico.py',25),
  ('declaracion -> SINO','declaracion',1,'p_declaracion_coditionelse','Sintactico.py',29),
  ('expresion -> COMMA','expresion',1,'p_declaracion_comma','Sintactico.py',33),
  ('declaracion -> expresion','declaracion',1,'p_declaracion_expr','Sintactico.py',37),
  ('expresion -> expresion SUMA expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',42),
  ('expresion -> expresion RESTA expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',43),
  ('expresion -> expresion MULT expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',44),
  ('expresion -> expresion DIV expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',45),
  ('expresion -> expresion POTENCIA expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',46),
  ('expresion -> expresion MODULO expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',47),
  ('expresion -> expresion EQUALS expresion','expresion',3,'p_expresion_operaciones','Sintactico.py',48),
  ('expresion -> PRINT PARENTIZQ VARIABLE PARENTDER','expresion',4,'p_expresion_grupo','Sintactico.py',71),
  ('expresion -> PUTS PARENTIZQ VARIABLE PARENTDER','expresion',4,'p_expresion_grupo','Sintactico.py',72),
  ('expresion -> PRINT PARENTIZQ STRING PARENTDER','expresion',4,'p_expresion_grupo','Sintactico.py',73),
  ('expresion -> PRINT PARENTIZQ STRING COMMA VARIABLE PARENTDER','expresion',6,'p_expresion_grupo','Sintactico.py',74),
  ('expresion -> expresion MENORQUE expresion','expresion',3,'p_expresion_logicas','Sintactico.py',80),
  ('expresion -> expresion MAYORQUE expresion','expresion',3,'p_expresion_logicas','Sintactico.py',81),
  ('expresion -> expresion MENORIGUAL expresion','expresion',3,'p_expresion_logicas','Sintactico.py',82),
  ('expresion -> expresion MAYORIGUAL expresion','expresion',3,'p_expresion_logicas','Sintactico.py',83),
  ('expresion -> expresion IGUAL expresion','expresion',3,'p_expresion_logicas','Sintactico.py',84),
  ('expresion -> expresion DISTINTO expresion','expresion',3,'p_expresion_logicas','Sintactico.py',85),
  ('expresion -> ENTERO','expresion',1,'p_expresion_numero','Sintactico.py',101),
  ('expresion -> DECIMAL','expresion',1,'p_expresion_decimal','Sintactico.py',105),
  ('expresion -> VARIABLE','expresion',1,'p_expresion_variable','Sintactico.py',109),
  ('expresion -> END','expresion',1,'p_expresion_end','Sintactico.py',113),
]