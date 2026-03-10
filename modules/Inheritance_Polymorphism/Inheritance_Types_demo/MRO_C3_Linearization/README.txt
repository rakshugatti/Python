Explanation of Method Resolution Order (MRO)

Method Resolution Order (MRO) defines the order in which Python searches for methods and attributes in a class hierarchy.

In the example:

class D(B, C)

When obj.show() is called, Python searches in this order:

D → B → C → A → object

Since B contains the show() method, it is executed.

The MRO can be checked using:

D.mro()
C3 Linearization Algorithm (Explanation)

Python uses the C3 Linearization algorithm to determine the MRO in multiple inheritance.

Rules of C3 Linearization
1.Child class is checked before parent classes.
2.Parent classes are searched from left to right.
3.Each class appears only once in the MRO list.
4.The inheritance hierarchy order must be preserved.

Example:

class D(B, C)
class B(A)
class C(A)

C3 Linearization calculates MRO as:

D → B → C → A → object

This ensures:
1.No class is repeated.
2.The hierarchy order is maintained.
3.Ambiguity in multiple inheritance is avoided.
