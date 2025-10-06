#!/usr/bin/python3
"""
Main script for testing polymorphism with Shape, Rectangle, and Circle classes.
This script demonstrates polymorphic behavior through method overriding.
"""

from polymorphism_demo import Shape, Rectangle, Circle
import math


def main():
    """Main function to demonstrate polymorphism with different shapes."""
    shapes = [
        Rectangle(10, 5),
        Circle(7)
    ]

    for shape in shapes:
        print(f"The area of the {shape.__class__.__name__} is: {shape.area()}")


if __name__ == "__main__":
    main()