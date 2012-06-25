# "I Could Wile Away The Hours"
#
# 
# Although our HTML and JavaScript interpreters are not yet integrated into
# a single browser, we can still extend our JavaScript interpreter
# independently. We already have support for recursive functions and "if"
# statements, but it would be nice to add support for "while".
#
# Consider the following two JavaScript fragments:
#
#    var i = 0;
#    while (i <= 5) {
#      document.write(i); 
#      i = i + 2;
#    };
#
# And: 
#
#    function myloop(i) {
#      if (i <= 5) {
#         document.write(i);
#         myloop(i + 2);
#      } ;
#    }
#    myloop(0);
#
# They both have the same effect: they both write 0, 2 and 4 to the
# webpage. (In fact, while loops and recursion are equally powerful! You
# really only need one in your language, but it is very convenient to have
# them both.) 
#
# We can extend our lexer to recognize 'while' as a keyword. We can extend
# our parser with a new statement rule like this: 
#
#    def p_stmt_while(p):
#        'stmt : WHILE exp compoundstmt'
#         p[0] = ("while",p[2],p[3])
#
# Now we just need to extend our interpreter to handle while loops. The
# meaning of a while loop is: 
#
#       1. First, evaluate the conditional expression in the current
#       environment. If it evaluates to false, stop.
#
#       2. Evaluate the body statements in the current environment. 
#
#       3. Go to step 1. 
#
# Recall that our JavaScript interpreter might have functions like:
#
#       eval_stmts(stmts,env)
#       eval_stmt(stmt,env)
#       eval_exp(exp,env) 
#
# For this assignment, you should write a procedure:
#
#       eval_while(while_stmt,evn) 
#
# Your procedure can (and should!) call those other procedures. Here is 
# how our interpreter will call your new eval_while(): 
# 
# def eval_stmt(stmt,env): 
#         stype = stmt[0] 
#         if stype == "if-then":
#                 cexp = stmt[1]
#                 then_branch = stmt[2] 
#                 if eval_exp(cexp,env):
#                         eval_stmts(then_branch,env) 
#         elif stype == "while":
#                 eval_while(stmt,env) 
#         elif stype == "if-then-else":
#                 ...
#
# Hint 1: We have structured this problem so that it is difficult for you
# to test (e.g., because we have not provided you the entire JavaScript
# interpreter framework). Thus, you should think carefully about how to
# write the code correctly. Part of the puzzle of this exercise is to
# reason to the correct answer without "guess and check" testing.
#
# Hint 2: It is totally legal to define JavaScript's while using a Python
# while statement. (Remember, an interpreter is like a translator.) You
# could also define JavaScript's while using recursion in Python.
#
# Hint 3: Extract the conditional expression and while loop body statements
# from while_stmt first. 

def eval_stmt(tree,environment):
    stmttype = tree[0]
    if stmttype == "call": # ("call", "sqrt", [("number","2")])
        fname = tree[1] # "sqrt"
        args = tree[2] # [ ("number", "2") ]
        fvalue = env_lookup(fname, environment)
        if fvalue[0] == "function":
            # We'll make a promise to ourselves:
            # ("function", params, body, env)
            fparams = fvalue[1] # ["x"]
            fbody = fvalue[2]
            fenv = fvalue[3]
            if len(fparams) <> len(args):
                print "ERROR: wrong number of args"
            else:
                #QUIZ: Make a new environment frame
                for index in range(len(fparams)):
                    fenv[fparams[index]] = eval_exp(args[index],environment)
                new_env = ("environment",fenv)
                #print new_env
                #print eval_exp(("identifier","x"),new_env)
                #print fbody[0]
                try:
                    eval_stmt(fbody[0],new_env)
                    # QUIZ : Evaluate the body
                    return None
                except Exception as return_value:
                    return return_value
        else:
            print  "ERROR: call to non-function"
    elif stmttype == "return":
        retval = eval_exp(tree[1],environment) 
        raise Exception(retval) 
    elif stmttype == "exp": 
        eval_exp(tree[1],environment)
    elif stmttype == "while":
        eval_while(stmt,env)
    elif stmttype == "assign":
        print eval_exp(tree[2],environment)
        env_update(tree[1],eval_exp(tree[2],environment),environment)
        print envi
            
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
            return float(exp[1])
        elif etype == "binop":
            a = eval_exp(exp[1],env)
            op = exp[2]
            b = eval_exp(exp[3],env)
            if op == "*":
                return a*b
            elif op == "<":
                return a<b
            elif op == ">":
                return a>b
            elif op == "+":
                return a+b
        elif etype == "identifier":
            vname = exp[1]
            value = env_lookup(vname,env) 
            if value == None: 
                print "ERROR: unbound variable " + vname
            else:
                return value

def eval_stmts(stmts,env): 
        for stmt in stmts:
            eval_stmt(stmt,env) 


def eval_while(while_stmt, env):
    print while_stmt[1]
    print while_stmt[2]
    expr = eval_exp(while_stmt[1],env)
    #body = eval_exp(while_stmt[2],env)
    print expr
    #print body
    while eval_exp(while_stmt[1],env) :
        eval_stmts(while_stmt[2],env)
    return

        # Fill in your own code here. Can be done in as few as 4 lines.

envi = (None, {"x" : 0})  
print eval_stmt(('assign', 'x', ('binop', ('identifier', 'x'), '+', ('number', '1'))),envi)
print eval_while(('while', ('binop', ('identifier', 'x'), '<', ('number', '3')), (('assign', 'x', ('binop', ('identifier', 'x'), '+', ('number', '1'))),)),envi)
print envi

