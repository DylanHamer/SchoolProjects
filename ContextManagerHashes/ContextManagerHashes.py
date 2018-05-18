"""
ContextManagers
Learning to use context context managers. Both these context managers add an exclamation to a string. In this case, a context manager would not be useful but with more complex operations it might be neccesary
by Dylan Hamer
"""

"""Method 1: Using a class"""
class testContextManager(object):
    """Test context manager, modifies strings"""
    def __init__(self, text):
        self.modifiedText = text + "!"
    
    def __enter__(self):
        return self.modifiedText
        
    def __exit__(self, type, value, traceback):
        if traceback is not None:
            print("Oh no! Error of type: {} occured with value: {}".format(type, value))
            return False
        else:
            return True
        
with testContextManager("Hello, World") as modifiedText:
    print(modifiedText)
    
"""Method 2: Using a decorator and generator"""

from contextlib import contextmanager

@contextmanager
def secondContextManager(text):
    """Test context manager, modifies strings"""
    modifiedText = text + "!"
    yield modifiedText
    
with secondContextManager("Hello, World") as modifiedText:
    print(modifiedText)











