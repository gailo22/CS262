# Writing Reductions

# We are looking at chart[i] and we see x => ab . cd from j.

# Hint: Reductions are tricky, so as a hint, remember that you only want to do
# reductions if cd == []

# Hint: You'll have to look back previously in the chart. 

def reductions(chart, i, x, ab, cd, j):
    # Insert code here!
    any_state = []
    if cd == [] :
        for rule in chart.values()[j] :
            
            if x == rule[2][0] : any_state += [(rule[0],rule[1]+[x],rule[2][1:],rule[3])]          
            
        return any_state
    else : return None
    
    
    
chart = {0: [('exp', ['exp'], ['+', 'exp'], 0), ('exp', [], ['num'], 0), ('exp', [], ['(', 'exp', ')'], 0), ('exp', [], ['exp', '-', 'exp'], 0), ('exp', [], ['exp', '+', 'exp'], 0)], 1: [('exp', ['exp', '+'], ['exp'], 0)], 2: [('exp', ['exp', '+', 'exp'], [], 0)]}

print reductions(chart,2,'exp',['exp','+','exp'],[],0) == [('exp', ['exp'], ['-', 'exp'], 0), ('exp', ['exp'], ['+', 'exp'], 0)]

