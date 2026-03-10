Explanation of Types of Inheritance
1️⃣ Single Inheritance

One child class inherits from one parent class.

Example:

Employee → Developer

Benefit:

Code reuse

Simpler structure

2️⃣ Multiple Inheritance

One child class inherits from multiple parent classes.

Example:

Person + Worker → Manager

Python resolves method conflicts using MRO (Method Resolution Order).

Example:

Manager.mro()

Output example:

[Manager, Person, Worker, object]
3️⃣ Multilevel Inheritance

Inheritance forms a chain.

Example:

Animal → Mammal → Dog

Dog inherits features from both Mammal and Animal.

4️⃣ Hierarchical Inheritance

Multiple child classes inherit from one parent class.

Example:

Vehicle
   ├── Car
   └── Bike

Both share the start() method.

5️⃣ Hybrid Inheritance

Combination of multiple and hierarchical inheritance.

Example:

      A
     / \
    B   C
     \ /
      D