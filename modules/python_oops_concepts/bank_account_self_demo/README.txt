Concept of self in Python
What is self?

self is a reference to the current object (instance) of a class.
It allows methods inside a class to access and modify instance variables.

When a method is called using an object, Python automatically passes the object reference as the first argument, which we conventionally name self.

Example:

obj.deposit(500)

Internally Python treats it like:

BankAccount.deposit(obj, 500)
What happens if you don't use self?

If self is not used:
1.The method cannot access instance variables.
2.Python throws an error like:
TypeError: method() takes 1 positional argument but 2 were given
3.Variables will behave like local variables instead of object variables.