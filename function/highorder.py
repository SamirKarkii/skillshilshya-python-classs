#high order functions 
# it takes function as argument 
 #wrapper higher ordser function 





def logger(func):
    def wrapper(*args, **kwargs):
        print(f"Function {func.__name__} is called with arguments {args} and {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned {result}")
        return result
    return wrapper

@logger
def rev_string(samir):
    return samir[::-1]

print(rev_string('samir'))


