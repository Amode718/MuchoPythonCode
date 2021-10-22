def area(a, b):
    return a * b 

print(area(4, 5))

def mean(*args):
    return sum(args) / len(args)
print(mean(1, 2, 33))

def num(**kwargs):
    return kwargs
print(num(a=1, b=2, c=3))