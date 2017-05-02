#using recursion:
#Food for thought: Recursion uses stacks to remember function calls and every
#computer has a stack size limit. So why use Recursion?
def fibonacci(n):
    if n<2 : return n
    else: return fibonacci(n-1) + fibonacci(n-2)

#using dicts (optimized): we can reduce the complexity of recursive function
#call by remembering the results of each function call and thus reusing
#the value straight away with out function call
def fib(n):
    if n<2 : return n
    elif n not in fib_dict :
            fib_dict[n]= fib(n-1) + fib(n-2)
    return fib_dict[n]

fib_dict = {}
print fib(11)
