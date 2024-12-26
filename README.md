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

## Adapter (Wrapper)

Convert the interface of a class into another interface clients expect.
Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

Applicability: Use the Adapter pattern when:

- you want to use an existing class, and its interface does not match the one you need.
- you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don’t necessarily have compatible interfaces.
- (object adapter only) you need to use several existing subclasses, but it’s impractical to adapt their interface by subclassing every one. An object adapter can adapt the interface of its parent class.

## Facade

Provide a unified interface to a set of interfaces in a subsystem. Facade defines a higher-level interface that makes the subsystem easier to use.

Applicability: Use the Facade pattern when:

- you want to provide a simple interface to a complex subsystem. Subsystems often get more complex as they evolve. Most patterns, when applied, result in more and smaller classes. This makes the subsystem more reusable and easier to customize, but it also becomes harder to use for clients that don’t need to customize it. A facade can provide a simple default view of the subsystem that is good enough for most clients. Only clients needing more customizability will need to look beyond the facade.
- there are many dependencies between clients and the implementation classes of an abstraction. Introduce a facade to decouple the subsystem from clients and other subsystems, thereby promoting subsystem independence and portability.
- you want to layer your subsystems. Use a facade to define an entry point to each subsystem level. If subsystems are dependent, then you can simplify the dependencies between them by making them communicate with each other solely through their facades.

# Behavioral Design Patterns

## Strategy

## Observer
