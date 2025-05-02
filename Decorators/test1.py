#python Decorators

def mydecorator(function):

    def wrapper(*args,**kwargs):
        print("I am decorating your function!")
        function(*args,**kwargs)
    
    return wrapper

@mydecorator #optimal way to call decorators
def hello_world():
    print("Hello world!")




#mydecorator(hello_world)()

#hello_world()

@mydecorator
def hello_person(person):
    print(f"Hello {person} !")

@mydecorator
def get_age(name,age):
    #age = input("What is your age?")
    #name = input("What is your name?")

    print(f"Hello {name} !, You are {age} years old now.")

#hello_person("Anjali")

get_age("Aravinda",23)
