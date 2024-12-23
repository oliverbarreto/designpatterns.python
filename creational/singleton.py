# Design Patterns - Structural - Singleton

# Applicability: Use the Singleton pattern when:
# - there must be exactly one instance of a class, and it must be accessible to clients from a well-known access point.
# - when the sole instance should be extensible by subclassing, and clients should be able to use an extended instance without modifying their code.

# It’s important for some classes to have exactly one instance. YOu could control the number of instances (more than one) on the singleton class.


class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        # Initialize your singleton instance here
        self.some_attribute = "I am a singleton"


# Usage example
if __name__ == "__main__":
    # Create instances
    singleton1 = Singleton()
    singleton2 = Singleton()

    # Verify both instances are the same
    print(singleton1 is singleton2)  # True
    print(singleton1.some_attribute)  # "I am a singleton"
    print(singleton2.some_attribute)  # "I am a singleton"

    # Modify one instance affects the other
    singleton1.some_attribute = "Modified value"
    print(singleton2.some_attribute)  # "Modified value"
