Access Modifiers in Python
Access modifiers control how attributes and methods of a class can be accessed.

1. Public Members

Declared normally without underscore.

Accessible from anywhere (inside and outside the class).

Example:

self.name
2. Protected Members (_)

Declared with single underscore.

Intended for internal use within the class and subclasses.

Still accessible outside the class, but it is a convention not to use it directly.

Example:

self._course
3. Private Members (__)

Declared with double underscore.

Python performs name mangling to avoid direct access.

Example:

self.__marks

It internally becomes:

_ClassName__marks

Example:

Student__marks
Why Python Doesn't Have True Private Members

Python follows the philosophy:

"We are all consenting adults here."

Instead of strict restrictions, Python uses conventions and name mangling to discourage direct access rather than completely preventing it.