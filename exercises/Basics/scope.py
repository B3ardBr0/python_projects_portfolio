# local scope
# A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.
def myfunc():
  x = "JOU"
  print(x)

myfunc()

#global scope
# A variable created outside a function is called a global variable and belongs to the global scope.
y = "MA"

def myfunc():
  print(y)

myfunc()    

#global keyword
# The global keyword makes the variable global.
def myfunc():
  global x
  x = "SE"   # x is global now                   
  print(x)  

myfunc()

def outer_myfunc():
    x = "POES"
    def inner_myfunc():
        nonlocal x
        x += " gesig"
        return x
    print(inner_myfunc())
outer_myfunc()

