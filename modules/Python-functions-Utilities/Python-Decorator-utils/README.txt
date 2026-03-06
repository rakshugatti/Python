Concept: Python Decorators
Definition

A decorator is a function that modifies or extends the behavior of another function without changing its code.

Decorators are written using the @decorator_name syntax.

Example structure:

def decorator(func):
    def wrapper(*args, **kwargs):
        # extra functionality
        result = func(*args, **kwargs)
        return result
    return wrapper
(1) Timer Decorator

The @timer decorator measures how long a function takes to execute.

It uses the time module.

(2) Logger Decorator

The @logger decorator prints:

Function name

Arguments passed

Return value

This helps in debugging and tracking function behavior.
---------------------------------------------------------------
Key Points

Decorator	            |    Purpose
------------------------------------------------------
@timer	                |Measures execution time
@logger             	|Logs function calls
Decorator stacking  	|Multiple decorators applied to one function