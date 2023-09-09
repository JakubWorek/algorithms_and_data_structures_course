from egzP6btesty import runtests 

def jump ( M ):
    #tutaj proszę wpisać własną implementację
    x, y = 0, 0
    fields = {}
    fields.update({(f"({x}, {y})"): (x,y)})
    for el in M:
        if el == 'UL': x-=1; y+=2
        elif el == 'LU': x-=2; y+=1
        elif el == 'UR': x+=1; y+=2
        elif el == 'RU': x+=2; y+=1
        elif el == 'RD': x+=2; y-=1
        elif el == 'DR': x+=1; y-=2
        elif el == 'DL': x-=1; y-=2
        elif el == 'LD': x-=2; y-=1

        temp = fields.get(f"({x}, {y})")
        if temp: fields.pop(f"({x}, {y})")
        else: fields.update({(f"({x}, {y})"): (x,y)})

    return len(fields) 
    
runtests(jump, all_tests = True)