#patrick lugassy,ID:319266177
#ivan borisenco,ID:317366102

import sys


def newton(func,d_func,x0,epsilon,max_iter):
    """function return the result of A quadratic equation and solve it withe newton-refson Method """
    sum=0
    counter=0
    if d_func(x0)==0:
        return "No Solution"
    for i in range(max_iter):
        sum=x0-((func(x0))/(d_func(x0))) 
        x0=sum
        counter=i
        if (abs(func(x0)) < epsilon):
            print("The solution was found after: "+ str(counter+1) + " iterations") 
            return sum         
    return None   






def first(x):
    """function that return result of Assembling two functions with lambda functions """
    pow3=lambda x:x**3
    return pow3(x)
    
def second(x):
    add=lambda x:x+1
    return add(x)

def composition(f,g):
    return lambda x:f(g(x))
 
  