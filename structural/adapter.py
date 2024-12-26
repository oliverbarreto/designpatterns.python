# Design Patterns - Structural - Adapter (Wrapper)

# Convert the interface of a class into another interface clients expect.
# Adapter lets classes work together that couldn't otherwise because of incompatible interfaces.

# Applicability: Use the Adapter pattern when:

# - you want to use an existing class, and its interface does not match the one you need.
# - you want to create a reusable class that cooperates with unrelated or unforeseen classes, that is, classes that don’t necessarily have compatible interfaces.
# - (object adapter only) you need to use several existing subclasses, but it’s impractical to adapt their interface by subclassing every one. An object adapter can adapt the interface of its parent class.


class CelsiusTemperature:
    """Old system that works with Celsius"""

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature(self):
        return self.temperature


class FahrenheitTemperature:
    """New system that only understands Fahrenheit"""

    def __init__(self, temperature):
        self.temperature = temperature

    def get_temperature_fahrenheit(self):
        return self.temperature


class CelsiusToFahrenheitAdapter:
    """Adapter to make Celsius work where Fahrenheit is expected"""

    def __init__(self, celsius_temp):
        self.celsius_temp = celsius_temp

    def get_temperature_fahrenheit(self):
        # Convert Celsius to Fahrenheit
        celsius = self.celsius_temp.get_temperature()
        fahrenheit = (celsius * 9 / 5) + 32
        return fahrenheit


# Client code
def print_temperature(fahrenheit_temp):
    print(
        f"Temperature in Fahrenheit: {fahrenheit_temp.get_temperature_fahrenheit()}°F"
    )


# Usage example
if __name__ == "__main__":
    # Using the new system directly
    fahrenheit = FahrenheitTemperature(100)
    print_temperature(fahrenheit)

    # Using the old system through the adapter
    celsius = CelsiusTemperature(0)
    adapter = CelsiusToFahrenheitAdapter(celsius)
    print_temperature(adapter)  # The adapter makes it work!
