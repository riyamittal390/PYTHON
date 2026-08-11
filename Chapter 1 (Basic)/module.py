# A module is a file containing code written by somebody else(usually) which can be imported and used in our programs.

import pyjokes
joke = pyjokes.get_joke()     # get_joke() will print random jokes 
print(joke)



# Types of Modules

# 1. Built in Modules (Pre-installed in Python. eg: os, random, etc.)
# 2. External Modules (Need to install using pip. eg: tensorflow, flask, etc.)