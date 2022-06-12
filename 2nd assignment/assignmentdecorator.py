#decorator super charges our function
#its kind of way the decorator defined or works or method

def my_decorator(func):
    def wrap_func():
        print("**")
        func()
        print("***")
    return wrap_func

# @ signifies a decorator 
#@my_decotor on top of the function that we want to give capabilities
#by adding @my_decorator adds extra functionality
#it wraps another function and enhances it doesnt change orginal function
#it just enhances it, we can in a way take all things from 

@my_decorator
def hello():
    print("hello")

@my_decorator
def bye():
    print("see yea later")

hello()
bye()

