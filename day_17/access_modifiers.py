# Acess specifiers : Python does not have strict access specifiers like Java or C# (public, private, protected) enforced by the compiler. Instead, it follows a "we are all consenting adults" philosophy, relying on naming conventions to indicate intended access levels rather than enforcing them.

"""Types of access levels in Python:

Public: Default for all members. Accessible from anywhere.

Protected: Indicated by a single underscore _var. Suggests internal use within the class or subclasses, but still accessible externally.

Private: Indicated by double underscores __var. Uses name mangling to make accidental access harder (_ClassName__var), but still possible if explicitly referenced."""
# public variable (accessible anywhere)

class Student:
    def __init__(self,name):
        self.name = name
s1 = Student ("Tanvee")
print(s1.name)

# protected variable (_name): indicated by a single underscore suggest internal use within the class or subclasses, but still accessible externally.
class Student:
    def __init__(self):
        self._age =19
s1= Student()
print(s1._age)

#private variable(__name): indicated by double underscore uses name mangling
class Student:
    def __init__(self):
        self.__marks = 90 #(this will give attribute error)
s1= Student()
print(s1._Student__marks) 



