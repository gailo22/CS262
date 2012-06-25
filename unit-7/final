#!/usr/bin/python


import ply.lex as lex
import ply.yacc as yacc

########## tokens ##########

tokens = ('TIMES', 'OR', 'RPAREN', 'LPAREN', 'CHAR', 'NUMBER')

def t_TIMES(token):
    r'\*'
#   token.value = "*"
    token.type = 'TIMES'
    return token

def t_OR(token):
    r'\|'
#   token.value = "|"
    token.type = 'OR'
    return token

def t_LPAREN(token):
    r'\('
    token.type = 'LPAREN'
    return token

def t_RPAREN(token):
    r'\)'
    token.type = 'RPAREN'
    return token

def t_CHAR(token):
    r'[a-zA-Z]'
    token.value = str(token.value)
    token.type = 'CHAR'
    return token

def t_NUMBER(token):
    r'\d'
    token.value = int(token.value)
    token.type = 'NUMBER'
    return token

t_ignore = ' \t\v\r'

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1)

########## tokens ##########

########## parser ##########

start = 'args'

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

def p_exp_char(p):
    'exp : CHAR'
    p[0] = ("char", p[1])

def p_args(p):
    'args : exp args'
    p[0] = [p[1]]+p[2]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]

def p_exp_paren(p):
    'exp : LPAREN args RPAREN'
    p[0] = ("paren",p[2])

def p_exp_or(p):
    'exp : args OR args'
    p[0] = ("or",p[1],p[3])

def p_exp_times(p):
    'exp : args TIMES'
    p[0] = ("times", p[1])

def p_error(p):
        raise SyntaxError

########## parser ##########

########## interpreter ##########

def env_lookup(vname,env):
        if vname in env[1]:
                return (env[1])[vname]
        elif env[0] == None:
                return None
        else:
                return env_lookup(vname,env[0])

def env_update(vname,value,env):
        if vname in env[1]:
                (env[1])[vname] = value
        elif not (env[0] == None):
                env_update(vname,value,env[0])

def eval_exp(exp,env):
        etype = exp[0]
        if etype == "number":
            return int(exp[1])
        elif etype == "char":
            return str(exp[1])
        
def eval_stmts(stmts,env):
        for stmt in stmts:
            eval_stmt(stmt,env)

########## interpreter ##########

lexer = lex.lex()

def test_lexer(input_string):
  lexer.input(input_string)
  result = [ ]
  while True:
    tok = lexer.token()
    if not tok: break
    result = result + [(tok.type,tok.value)]
  return result

def test_parser(input_string):
  lexer.input(input_string)
  parser = yacc.yacc() 
  try: 
    parse_tree = parser.parse(input_string, lexer=lexer) 
    return parse_tree 
  except:
    return "error" 

question0 = "57"
question1 = "a(b*)4c56"
question2 = "((ab)|(cd))*"

print test_lexer(question0)
print test_lexer(question1)
print test_lexer(question2)

print test_parser(question0)
print test_parser(question1)
print test_parser(question2)

