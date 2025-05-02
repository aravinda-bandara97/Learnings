#python Decorators - get function return value seperately with decorations - need to learn more about this,

def mydecorator(function):

    def wrapper(*args,**kwargs):
        print("I am decorating your function!")
        return_value = function(*args,**kwargs)
        return return_value

        
    
    return wrapper

@mydecorator
def hello_person(person):
    print(f"Hello {person}")
    return f"Hello {person} !!!"


print(hello_person("Ara"))
