import os  # Unused import

def testFunction():  # Function name should be lowercase
  # Bad indentation and unnecessary semicolon
  a = 20;
  b = 30
  sum_of_numbers=a+b # Operators should be surrounded by spaces
  print("Sum is:",sum_of_numbers)  # Missing whitespace after ','

class MyClass():
  def __init__(self, val1, val2):
    # Too long line below (more than 79-80 characters for PEP 8 compliance)
    self.myvariable = 'This is a really, really, really, really, really, really, really long string'

    self.value1 = val1; self.value2 = val2 # Multiple statements on one line

  def MyMethod(self): # Method name should be lowercase
    # Unnecessary pass statement and unused variable
    pass
    unused_var = 123

def another_function(): # Too few spaces before inline comment
  #Incorrectly spaced comment
  # Correctly spaced comment
  pass

# Extra whitespace before this comment

#Incorrectly indented docstring
"""
This is a docstring.
"""
# Correctly indented docstring
def some_function():
    """
    This is a docstring.
    """
    pass


if __name__ == "__main__":
 testFunction() # Bad indentation
 my_object = MyClass(10, 20) # Missing whitespace after ','
 my_object.MyMethod() # Method should be called with lower case
 another_function()
 # Trailing whitespace at the end of the script