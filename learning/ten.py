#!/home/avis/venv/bin/python3

def getvar(*args: int):
    import math
    return "{:.2}".format(sum( pow(x - sum(args)/len(args), 2) for x in args ) / (len(args)-1))
print(getvar(1,2,3,4))
    
