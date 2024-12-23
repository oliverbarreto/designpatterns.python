# Design Patterns in Python inspired by the book "Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Erich"

Code: designpatterns.python
[https://github.com/oliverbarreto/designpatterns.python](https://github.com/oliverbarreto/designpatterns.python)

Resources:

- [https://www.youtube.com/playlist?list=PL5C9QKu8AsmVRvgzeYTepoGgH5U9-XLc4](https://www.youtube.com/playlist?list=PL5C9QKu8AsmVRvgzeYTepoGgH5U9-XLc4)

# Creational Design Patterns

## Singleton

Applicability: Use the Singleton pattern when:

- there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
- when the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code.

It’s important for some classes to have exactly one instance. YOu could control the number of instances (more than one) on the singleton class.

## Factory Method

Define an interface for creating an object, but let subclasses decide which class to instantiate
Applicability: Use the Factory Method pattern when:

- a class can't anticipate the class of objects it must create
- a class wants its subclasses to specify the objects it creates
- classes delegate responsibility to one of several helper subclasses, and you want to localize the knowledge of which helper subclass is the delegate

# Structural Design Patterns

# Behavioral Design Patterns
