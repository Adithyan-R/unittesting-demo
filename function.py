def average(args):
    Summ=0
    for i in args:
        Summ=Summ+i

    return Summ/len(args)

def maximum(args):
    maxx=max(args)
    return maxx