#!/usr/bin/env python3

APPROVED_JOBS = [
    "Admin",
    "Customer Service",
    "Human Resources",
    "ITC",
    "Production",
    "Legal",
    "Finance",
    "Sales",
    "General Management",
    "Research & Development",
    "Marketing",
    "Purchasing"
]

class Person:
    def __init__(self, name="John Doe", job="Sales"):
        self._name = None
        self._job = None
        self.name = name  # Uses setter for validation and formatting
        self.job = job  # Uses setter for validation

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and (1 <= len(value) <= 25):  
            self._name = value.title()  # ✅ Convert name to title case
        else:
            print("Name must be string between 1 and 25 characters.")  
            self._name = "Unnamed"

    @property
    def job(self):
        return self._job

    @job.setter
    def job(self, value):
        if isinstance(value, str) and value in APPROVED_JOBS:
            self._job = value
        else:
            print("Job must be in list of approved jobs.")
            self._job = "Unassigned"

# ✅ Test Case: This should now pass
guido = Person(name="guido van rossum")
print(guido.name)  # Output: "Guido Van Rossum"
