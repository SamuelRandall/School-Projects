class Foo(object):
    pass

class Bar(Foo):
    pass

a = Bar()

print(type(Foo))
print(type(Bar))
print(type(a))
print(type(type))
print(type(object))

print(isinstance(Foo, type))
print(isinstance(Bar, type))
print(isinstance(a, Bar))
print(isinstance(a, Foo))
print(isinstance(Bar, Foo))
print(isinstance(a, object))
print("*" + str(isinstance(type, object)))
print(isinstance(Bar, object))
print(isinstance(Foo, object))
print(isinstance(type, type))
print(isinstance(type, object))
