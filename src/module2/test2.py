def my_decorator(func):

    def wrapper():
        print("before function execution")
        func()
        print("after function execution")  
    return wrapper      
@my_decorator
def welcome():
    print("welcome to python")
welcome()
@my_decorator
def addition():
    print("Addition")
addition()

