
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'leftPLUSleftTIMESLPAREN NUMBER PLUS RPAREN TIMESstatement : expressionexpression : expression PLUS expression\n                  \n                  | expression TIMES expression\n                  expression : LPAREN expression RPARENexpression : NUMBER'
    
_lr_action_items = {'LPAREN':([0,3,5,6,],[3,3,3,3,]),'NUMBER':([0,3,5,6,],[4,4,4,4,]),'$end':([1,2,4,8,9,10,],[0,-1,-5,-2,-3,-4,]),'PLUS':([2,4,7,8,9,10,],[5,-5,5,-2,-3,-4,]),'TIMES':([2,4,7,8,9,10,],[6,-5,6,6,-3,-4,]),'RPAREN':([4,7,8,9,10,],[-5,10,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statement':([0,],[1,]),'expression':([0,3,5,6,],[2,7,8,9,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statement","S'",1,None,None,None),
  ('statement -> expression','statement',1,'p_statement_expr','ejemplazo.py',65),
  ('expression -> expression PLUS expression','expression',3,'p_expression_binop','ejemplazo.py',69),
  ('expression -> expression TIMES expression','expression',3,'p_expression_binop','ejemplazo.py',71),
  ('expression -> LPAREN expression RPAREN','expression',3,'p_expression_group','ejemplazo.py',83),
  ('expression -> NUMBER','expression',1,'p_expression_number','ejemplazo.py',87),
]
