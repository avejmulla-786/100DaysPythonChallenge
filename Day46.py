#PYTHON DECORATORS 

def greet(fx):
  def mfx():
    print("Good Morning")
    fx()
    print("Thanks for using this function")
    return mfx
  
@greet 
def add(a,b):
    print(a+b)

def hello():
    print("Hello world")

hello()
