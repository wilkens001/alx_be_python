#!/usr/bin/python3
"""
Main script for testing class methods and static methods.
This script demonstrates the functionality and usage of Calculator class methods.
"""

from class_static_methods_demo import Calculator


def main():
    """Main function to demonstrate class and static method usage."""
    # Using the static method
    sum_result = Calculator.add(10, 5)
    print(f"The sum is: {sum_result}")

    # Using the class method
    product_result = Calculator.multiply(10, 5)
    print(f"The product is: {product_result}")


if __name__ == "__main__":
    main()