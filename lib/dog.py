#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
    def __init__(self, name="Storm", breed="Beagle"):
        self._name = None
        self._breed = None
        self.name = name  # Uses setter for validation
        self.breed = breed  # Uses setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (1 <= len(value) <= 25):
            self._name = value
        else:
            print("Name must be string between 1 and 25 characters.")
            self._name = "Unnamed"

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value in APPROVED_BREEDS:
            self._breed = value
        else:
            print("Breed must be in list of approved breeds.")
            self._breed = "Unknown"

# Example usage
d1 = Dog("Buddy", "Pug")
print(d1.name)   # Output: Buddy
print(d1.breed)  # Output: Pug

d2 = Dog("Max", "Golden Retriever")  # Invalid breed
print(d2.breed)  # Output: Unknown (fallback)

d3 = Dog("", "Beagle")  # Invalid name
print(d3.name)  # Output: Unnamed
