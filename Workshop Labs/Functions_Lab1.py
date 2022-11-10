#DEFINING FUNCTION

#A function is a named section of a program which performs a specific task. 
#Functions add flexibility to code like variables because they are reusable, which reduces the amount of code we have to write.
#To declare a function:
def hello_world():
    print('hello world')
    
hello_world()               #if the function is not called, it will not run

#The hash # symbol is used for comments. Anything after this on that line is ignored by python.
#The function is defined using def.
#The function has a name hello_world.
#The next line is indented to show it is inside the function.
#The function is called by last line hello_world().

#Now let's return the information from the function:
def hello_world():
    return 'hello world'
    
greeting = hello_world()
print(greeting)

#You created a function called hello_world().
#In the first example, you used print() to display the output directly to the console.
#In the second example, you used return to return the string hello_world to the point in the code where the function was called.
#You assigned the hello_world() function to a variable called greeting.
#You printed out the value of the variable greeting.