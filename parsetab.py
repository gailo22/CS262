
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x11\xcc)WH\xa3\xbf#_<0\xad>\xaa\xf9\x1c'
    
_lr_action_items = {'RPAREN':([1,3,4,6,8,9,10,11,],[-4,-1,-2,-3,-7,11,-6,-5,]),'NUMBER':([0,1,3,4,5,6,7,8,10,11,],[3,3,-1,-2,3,-3,3,-7,-6,-5,]),'TIMES':([1,2,3,4,6,8,9,10,11,],[-4,8,-1,-2,8,-7,8,8,-5,]),'CHAR':([0,1,3,4,5,6,7,8,10,11,],[4,4,-1,-2,4,-3,4,-7,-6,-5,]),'LPAREN':([0,1,3,4,5,6,7,8,10,11,],[5,5,-1,-2,5,-3,5,-7,-6,-5,]),'OR':([1,2,3,4,6,8,9,10,11,],[-4,7,-1,-2,7,-7,7,7,-5,]),'$end':([1,2,3,4,6,8,10,11,],[-4,0,-1,-2,-3,-7,-6,-5,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'args':([0,1,5,7,],[2,6,9,10,]),'exp':([0,1,5,7,],[1,1,1,1,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> args","S'",1,None,None,None),
  ('exp -> NUMBER','exp',1,'p_exp_number','unit-7/final',58),
  ('exp -> CHAR','exp',1,'p_exp_char','unit-7/final',62),
  ('args -> exp args','args',2,'p_args','unit-7/final',66),
  ('args -> exp','args',1,'p_args_last','unit-7/final',70),
  ('exp -> LPAREN args RPAREN','exp',3,'p_exp_paren','unit-7/final',74),
  ('exp -> args OR args','exp',3,'p_exp_or','unit-7/final',78),
  ('exp -> args TIMES','exp',2,'p_exp_times','unit-7/final',82),
]
