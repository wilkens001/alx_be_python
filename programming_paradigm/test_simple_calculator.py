#!/usr/bin/python3
"""
Unit tests for the SimpleCalculator class.
This module contains comprehensive tests for all arithmetic operations.
"""

import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """Test cases for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        # Test basic positive addition
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(10, 5), 15)
        
        # Test addition with negative numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)
        self.assertEqual(self.calc.add(-10, 15), 5)
        
        # Test addition with zero
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(5, 0), 5)
        self.assertEqual(self.calc.add(0, -3), -3)
        
        # Test addition with floating point numbers
        self.assertEqual(self.calc.add(2.5, 3.7), 6.2)
        self.assertEqual(self.calc.add(-1.5, 2.5), 1.0)

    def test_subtraction(self):
        """Test the subtraction method."""
        # Test basic subtraction
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(3, 2), 1)
        
        # Test subtraction with negative numbers
        self.assertEqual(self.calc.subtract(-5, -3), -2)
        self.assertEqual(self.calc.subtract(-10, 5), -15)
        self.assertEqual(self.calc.subtract(10, -5), 15)
        
        # Test subtraction with zero
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(5, 0), 5)
        self.assertEqual(self.calc.subtract(0, 3), -3)
        
        # Test subtraction with floating point numbers
        self.assertEqual(self.calc.subtract(5.5, 2.3), 3.2)
        self.assertEqual(self.calc.subtract(-1.5, 2.5), -4.0)
        
        # Test when result is zero
        self.assertEqual(self.calc.subtract(5, 5), 0)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Test basic multiplication
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(7, 8), 56)
        
        # Test multiplication with negative numbers
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-5, -6), 30)
        self.assertEqual(self.calc.multiply(5, -2), -10)
        
        # Test multiplication with zero
        self.assertEqual(self.calc.multiply(0, 0), 0)
        self.assertEqual(self.calc.multiply(5, 0), 0)
        self.assertEqual(self.calc.multiply(0, -3), 0)
        
        # Test multiplication with one
        self.assertEqual(self.calc.multiply(5, 1), 5)
        self.assertEqual(self.calc.multiply(1, -7), -7)
        
        # Test multiplication with floating point numbers
        self.assertEqual(self.calc.multiply(2.5, 4), 10.0)
        self.assertEqual(self.calc.multiply(-1.5, 2), -3.0)

    def test_division(self):
        """Test the division method."""
        # Test basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        self.assertEqual(self.calc.divide(15, 3), 5.0)
        
        # Test division with negative numbers
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        self.assertEqual(self.calc.divide(-15, -3), 5.0)
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        
        # Test division by zero (should return None)
        self.assertIsNone(self.calc.divide(10, 0))
        self.assertIsNone(self.calc.divide(-5, 0))
        self.assertIsNone(self.calc.divide(0, 0))
        
        # Test zero divided by number
        self.assertEqual(self.calc.divide(0, 5), 0.0)
        self.assertEqual(self.calc.divide(0, -3), 0.0)
        
        # Test division with floating point numbers
        self.assertEqual(self.calc.divide(7.5, 2.5), 3.0)
        self.assertEqual(self.calc.divide(-4.5, 1.5), -3.0)
        
        # Test division by one
        self.assertEqual(self.calc.divide(5, 1), 5.0)
        self.assertEqual(self.calc.divide(-7, 1), -7.0)
        
        # Test division that results in fraction
        self.assertEqual(self.calc.divide(1, 3), 1/3)
        self.assertEqual(self.calc.divide(2, 3), 2/3)

    def test_edge_cases(self):
        """Test additional edge cases and boundary conditions."""
        # Test very large numbers
        self.assertEqual(self.calc.add(1000000, 2000000), 3000000)
        self.assertEqual(self.calc.multiply(1000, 1000), 1000000)
        
        # Test very small numbers
        self.assertAlmostEqual(self.calc.add(0.0001, 0.0002), 0.0003, places=7)
        self.assertAlmostEqual(self.calc.divide(0.001, 0.1), 0.01, places=7)


if __name__ == '__main__':
    unittest.main()