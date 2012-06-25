# Terrible Tuples
#
# Focus: Units 3 and 4, Grammars and Parsing
#
# In this problem you will use context-free grammars to specify some
# expression for part of a new programming language. We will specify tuples
# and lists, as in Python. We will consider four types of expressions.
#
# 1. An expression can be a single NUMBER token. In this case, your parser
# should return ("number",XYZ) where XYZ is the value of the NUMBER
# token.
#
# 2. An expression can be LPAREN expression RPAREN . In this case, your
# parser should return the value of the expression inside the parentheses.
#
# 3. An expression can be LPAREN "a list of more than one comma-separated
# expressions" RPAREN. This should remind you of tuples in Python:
#
#               (1,2,3) 
#
# The inner expressions are 1 2 and 3, and they are separated by commas.
# In this case, your parser should return ("tuple", ...) where ... is a
# list of the child expression values. For example, for (1,2) you should
# return ("tuple",[("number",2),("number",3)]). 
#
# 4. An expression can be LBRACKET "a list of one or more comma-separated
# expressions" RBRACKET. This should remind you of lists in Python:
#
#               [7,8,9] 
#
# These parse exactly like tuples, except that they use square brackets
# instead of parentheses, and singleton lists like [7] are valid. Your
# parser should return ("list", ...) as above, so [7,8] would return
# ("list",[("number",7),("number",8)]). 
#
# Complete the parser below.  

import ply.lex as lex
import ply.yacc as yacc

start = 'exp'    # the start symbol in our grammar

#####
#

# Place your grammar definition rules here. 

def p_exp_number(p):
    'exp : NUMBER'
    p[0] = ("number", p[1])

#def p_exp_number_paren(p):
#    'exp : LPAREN NUMBER RPAREN'
#    p[0] = ("number", p[2])    

def p_exp_exp_paren(p):
    'exp : LPAREN exp RPAREN'
    p[0] = p[2]
    
def p_args(p):
    'args : exp COMMA args'
    p[0] = [p[1]]+p[3]

def p_args_last(p):
    'args : exp'
    p[0] = [p[1]]

def p_exp_tuple(p):
    'exp : LPAREN exp COMMA args RPAREN'
    p[0] = ("tuple",[p[2]]+p[4])

def p_exp_list(p):
    'exp : LBRACKET args RBRACKET'
    p[0] = ("list", p[2])
    
#
#####

def p_error(p):
        raise SyntaxError


# We have provided a lexer for you. You should not change it.

tokens = ('LPAREN', 'RPAREN', 'LBRACKET', 'RBRACKET', 'NUMBER', 'COMMA') 

def t_NUMBER(token):
        r"[0-9]+"
        token.value = int(token.value)
        return token

t_ignore        = ' \t\v\r'
t_COMMA         = r','
t_LPAREN        = r'\(' 
t_RPAREN        = r'\)' 
t_LBRACKET      = r'\[' 
t_RBRACKET      = r'\]' 

def t_error(t):
  print "Lexer: unexpected character " + t.value[0]
  t.lexer.skip(1) 

# We have included some testing code to help you check your work. Since
# this is the final exam, you will definitely want to add your own tests.
lexer = lex.lex() 

def test(input_string):
  lexer.input(input_string)
  parser = yacc.yacc() 
  try: 
    parse_tree = parser.parse(input_string, lexer=lexer) 
    return parse_tree 
  except:
    return "error" 

""""test cases from forum by Replicant262"""
questions = [ " 123 " ,
              " (123) ",
              " (1,2,3) ",
              " [123] ",
              " [1,2,3] " ,
              " [(1,2),[3,[4]]] ",
              " (1,2) [3,4) ",
              " [1] ",
              " (1) ",
              " (1,2,3,4,5,6) ",
              " [1,2,3,4,5,6] ",
              " [((1))] "
            ]
answers   = [ ('number', 123),
              ('number', 123),
              ('tuple', [('number', 1), ('number', 2), ('number', 3)]),
              ('list', [('number', 123)]),
              ('list', [('number', 1), ('number', 2), ('number', 3)]),
              ('list', [('tuple', [('number', 1), ('number', 2)]), ('list', [('number', 3), ('list', [('number', 4)])])]),
              "error",
              ('list', [('number', 1)]),
              ('number', 1),
              ('tuple', [('number', 1), ('number', 2), ('number', 3), ('number', 4), ('number', 5), ('number', 6)]),
              ('list', [('number', 1), ('number', 2), ('number', 3), ('number', 4), ('number', 5), ('number', 6)]),
              ('list', [('number', 1)])
            ]

print [test(questions[i]) == answers[i] for i in range(len(questions))]

""""test cases from forum by dave jones"""

import random
def generate_string(depth=6):
    """Generate a tree and string that should parse to the tree"""
    def gen_num(*args):
        n = random.randint(0,1000)
        return ("number", n), str(n)
    def gen_paren(depth):
        e, s = gen_exp(depth-1)
        return e, "(" + s + ")"
    def gen_tuple(depth):
        nexp = random.randint(2, 5)
        exps = [gen_exp(depth-1) for i in xrange(nexp)]
        e = ("tuple", [x[0] for x in exps])
        s = "(" + ",".join([x[1] for x in exps]) + ")"
        return e, s
    def gen_list(depth):
        nexp = random.randint(1, 5)
        exps = [gen_exp(depth-1) for i in xrange(nexp)]
        e = ("list", [x[0] for x in exps])
        s = "[" + ",".join([x[1] for x in exps]) + "]"
        return e, s    
    def gen_exp(depth):
        if depth == 0:
            return gen_num()
        f = random.choice([gen_num, gen_paren, gen_tuple, gen_list])
        return f(depth)
    return gen_exp(depth)

def test_random(N=100):
    for kk in xrange(N):
        e, s = generate_string(4)
        if not test(s) == e:
            print "failed!", '\n', s, '\n', e
            print test(s)
            assert False
    print "passed", N, "tests"
test_random()

