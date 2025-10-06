#!/usr/bin/python3
"""
Demonstration of class methods and static methods in Python.
This module shows the differences between @classmethod and @staticmethod decorators.
"""


class Calculator:
    """Calculator class demonstrating class methods and static methods."""
    
    calculation_type = "Arithmetic Operations"
    
    @staticmethod
    def add(a, b):
        """
        Static method to add two numbers.
        
        Args:
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The sum of a and b
        """
        return a + b
    
    @classmethod
    def multiply(cls, a, b):
        """
        Class method to multiply two numbers.
        
        Args:
            cls: Reference to the class
            a (float): First number
            b (float): Second number
            
        Returns:
            float: The product of a and b
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b