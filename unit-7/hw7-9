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

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

def p_exp_char(p):
    'exp : CHAR'
    p[0] = ("char", p[1])

def p_args(p):
    'args : exp args'
    p[0] = [p[1]]+p[3]

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

########## grammar ##########

grammar = []

start = 'exp'

def addtochart(chart, index, state):
    # Insert code here!
    if all([False for chartex in chart[index] if chartex == state]) :
    #if chart[index] != [state] :
        chart[index] += [state]
        return True
    else : return False

def closure (grammar, i, x, ab, cd, j):
    # Insert code here!

    if cd == [] : return []
    states = []
    for rule in [part for part in grammar if part[0] == cd[0]] :
        if ab in rule : print "inline"
        state = (rule[0],[],rule[1],i)
        states += [state]
        #print states
    return states

def shift (tokens, i, x, ab, cd, j):
    # Insert code here
    any_state = ()
    if cd == [] : return None
    if cd[0] != tokens[i] : any_state = None
    else : any_state = (x,ab+[cd[0]],cd[1:],j)
    return any_state

def reductions(chart, i, x, ab, cd, j):
    return [ (jstate[0],jstate[1] + [x],(jstate[2])[1:], jstate[3] )
        for jstate in chart[j]
        if cd == [] and jstate[2] != [] and (jstate[2])[0] == x ]

def parse(tokens,grammar):
    tokens = tokens + ["end_of_input_marker"]
    chart = {}
    start_rule = grammar[0]
    for i in range(len(tokens)+1):
        chart[i] = []
    start_state = (start_rule[0],[],start_rule[1],0)
    chart[0] = [ start_state ]
    for i in range(len(tokens)):
        while True:
            changes = False
            for state in chart[i]:
                x = state[0]
                ab = state[1]
                cd = state[2]
                j = state[3]
                next_states = closure(grammar,i,x,ab,cd,j)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes

                next_state = shift(tokens,i,x,ab,cd,j)
                if next_state != None :
                    any_changes = addtochart(chart,i+1,next_state) or any_changes

                next_states = reductions(chart,i,x,ab,cd,j)
                for next_state in next_states:
                    changes = addtochart(chart,i,next_state) or changes

            if not changes : break

    for i in range(len(tokens)):
        print "== chart " + str(i)
        for state in chart[i]:
            x = state[0]
            ab = state[1]
            cd = state[2]
            j = state[3]
            print "    " + x + " ->",
            for sym in ab :
                print " " + sym,
            print " .",
            for sym in cd :
                print " " + sym,
            print "  from " + str(j)

    accepting_state = (start_rule[0],start_rule[1],[],0)
    return accepting_state in chart[len(tokens)-1]

#print grammar
#print tokens

#result = parse(tokens,grammar)

########## grammar ##########

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

question1 = "a(b*)4c56"
question2 = "((ab)|(cd))*"

print test_lexer(question1)
print test_lexer(question2)

print test_parser(question1)
print test_parser(question2)

