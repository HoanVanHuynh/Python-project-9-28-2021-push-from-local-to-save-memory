class Base:
    def __init__(self, hard):
        self.hard = hard
    def foo(self):
        return self.bar()

# "If I do this I'll capture the original build class"
# "I'll write my own build class"
old_bc = __build_class__
def my_bc(*a, **kw): 
    print('my buildcclass, ' ,a, kw)
    return old_bc(*a, **kw)

"I'll import from the built-ins and"
import builtins 
" I'll swap them out "
builtins.__build_class__ = my_bc
" Here I can patch into what Python actually does"
" when it creates classes and "

class BaseMeta(type):
    def __new__(cls, name, bases, body):
        return super().__new__(cls, name, bases, body)