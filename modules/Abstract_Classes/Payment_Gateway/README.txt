1. What is an Abstract Class in Python?

An abstract class is a class that cannot be instantiated directly.

It can have abstract methods, which are methods without implementation.

Subclasses must implement all abstract methods to be instantiable.

In Python, abstract classes are created using the abc module (ABC and abstractmethod).

Why use abstract classes?
They define a contract for subclasses, ensuring certain methods are implemented in all child classes.

2. Using the abc Module

Import ABC and abstractmethod from the abc module.

Inherit your class from ABC.

Decorate abstract methods with @abstractmethod.
@Abstract Classes in Python using abc

In Python, abstract classes are created using the abc module. Abstract classes can have abstract methods, which must be implemented by concrete subclasses. You cannot instantiate an abstract class directly.