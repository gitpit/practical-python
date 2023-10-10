'''
# Chapter 3: Program Organization - practice
# Dated:2023/10/06
'''

'''
3.1 Scripting
'''

#functions

def square_root(num):
    '''
    About square root 
    '''
    return num*num
square_root(44)

## to try... writing report.py program as a consolidated one

'''
3.2 More on Functions
'''
# default arguments
# If no return value is given or return is missing, None is returned.
# multiple reutrn value as tuple

#note:: function can't modify global variable outside
# to modify a global vairbale it has to prefix with global keyword inside its scope
name = 'Dave'
def spam():
    global name
    name = 'Guido' # Changes the global name above

# argument passing - pass by value ; pass by ref
## Key point: Functions don’t receive a copy of the input arguments.
## Reminder: Variable assignment never overwrites memory. The name is merely bound to a new value.

