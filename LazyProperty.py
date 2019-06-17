# lazyProperty.py
#
# Use Prop() to define properties in your classes outside of the __init__()
#
# usage:
#
# class MyClass:
#     name  = Prop("")                                 # simple string defaulting to empty
#     title = Prop(lazy=lambda self:"Mr. "+self.name)  # lazy property, inits to Mr. name upon first reference
#                                                      # can be assigned a value
# 
class Prop(object):
    def __init__(self, value=None, lazy=None):
        self.value = value
        self.lazy  = lazy

    def __get__(self, obj, objtype):
        if self.lazy:
            self.value = self.lazy(obj)
            self.lazy  = None
        return self.value

    def __set__(self, obj, value):
        self.value = value

if __name__ == "__main__":
    class Test:
        answer   = Prop(lazy=lambda self:self.question+1)
        question = Prop(41)

    test = Test()
    test.question = 72
    print(test.answer) #73
    test.answer = 37
    print(test.answer) #37
    

