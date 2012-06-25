# Memofibo

# Submit via the interpreter a definition for a memofibo procedure that uses a
# chart. You are going to want the Nth value of the chart to hold the Nth
# fibonacci number if you've already computed it and to be empty otherwise.

chart = {}

def memofibo(n):
    # Quiz
    if n in chart : return chart[n]
    else:
        if n <= 2 : chart[n] = 1
        else : chart[n] = memofibo(n-2) + memofibo(n-1)
        return chart[n]
    
    
print memofibo(24)




