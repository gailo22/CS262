# Addtochart

# Let's code in Python! Write a Python procedure addtochart(chart,index,state)
# that ensures that chart[index] returns a list that contains state exactly
# once. The chart is a Python dictionary and index is a number. addtochart
# should return True if something was actually added, False otherwise. You may
# assume that chart[index] is a list.


def addtochart(chart, index, state):
    # Insert code here!
    if all([False for chartex in chart[index] if chartex == state]) :
    #if chart[index] != [state] :
        chart[index] += [state]
        return True
    else : return False
    
    
#print addtochart({1:['A']},1,'B')
#print addtochart({1:['A', 'C', 'B']},1,'B')

