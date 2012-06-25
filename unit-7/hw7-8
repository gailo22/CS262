grammar = [
    ("S",["E"]),
    ("E",["(","E",")"]),
    ("E",["E","+","E"]),
    ("E",["E","-","E"]),
    ("E",["id"]),
    ("E",["id","(","A",")"]),
    ("A",[]),
    ("A",["NA"]),
    ("NA",["E"]),
    ("NA",["E",",","NA"]),
]

tokens = ["id", "(", "(", "id", ")", ",", "id", ")"]

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

print grammar
print tokens

result = parse(tokens,grammar)
