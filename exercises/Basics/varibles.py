#varibles
#Creating and checking the type of varibles
elmar = 100
print(type(elmar))

# Example 2: Checking if a variable is defined by using try-except
try:
    print(my_undefined_var)  # This variable is not defined
except NameError:
    print("my_undefined_var is not defined.")

# Example 3: Checking if a variable name is in the local or global context
# locals() and globals() return dictionaries of defined variables      
my_var2 = "Hello"
print("my_var2 in locals? ->", 'my_var2' in locals())

x = str(3)
y = int(3)
z = float(3)

 
print(x,y,z)