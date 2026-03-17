An abstract class is a class that can contain both abstract methods (without implementation) and concrete methods (with implementation). It is used when some common functionality can be shared among subclasses.

An interface is a concept where a class only defines method signatures without any implementation. It ensures that any class implementing it must provide implementations for all methods.

| Feature        | Abstract Class                 | Interface                     |
| -------------- | ------------------------------ | ----------------------------- |
| Methods        | Abstract + Concrete methods    | Only abstract methods         |
| Implementation | Partial implementation allowed | No implementation             |
| Variables      | Can have instance variables    | Usually no state              |
| Inheritance    | Used for "is-a" relationship   | Used for "can-do" capability  |
| Python Support | Using `abc` module             | No direct keyword (simulated) |
