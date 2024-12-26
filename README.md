<div align="center">
  <a href="https://oliverbarreto.com">
    <img src="https://www.oliverbarreto.com/images/site-logo.png" />
  </a>
</div>
</br>
</br>
<div align="center">
  <h1>Design Patterns in Python inspired by the book "Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Erich</h1>
  </br>
  <p>An attempt to (officialy) learn Design Patterns to be able to apply them. Let's use Python instead of Java.</p>
  <p>Code: <a href="https://github.com/oliverbarreto/designpatterns.python">https://github.com/oliverbarreto/designpatterns.python</a></p>
  </br>
  <p>Resources:</p>
  <a href="https://www.youtube.com/playlist?list=PL5C9QKu8AsmVRvgzeYTepoGgH5U9-XLc4">https://www.youtube.com/playlist?list=PL5C9QKu8AsmVRvgzeYTepoGgH5U9-XLc4</a>
  </br>
  </br>
  <p>Created with ❤️ by Oliver Barreto</p>
</div>

</br>
</br>

# Design Patterns in Python inspired by the book "Design Patterns: Elements of Reusable Object-Oriented Software by Gamma, Erich

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

## Builder

Separate the construction of a complex object from its representation so that the same construction process can create different representations.

Applicability: Use the Builder pattern when:

- the algorithm for creating a complex object should be independent of the parts that make up the object and how they're assembled
- the construction process must allow different representations for the object that's constructed

# Structural Design Patterns

## Adapter

## Facade

# Behavioral Design Patterns

## Strategy

## Observer
