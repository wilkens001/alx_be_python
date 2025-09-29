#!/usr/bin/python3
"""
This module contains the BankAccount class for managing bank account operations.
"""


class BankAccount:
    """
    A class representing a simple bank account with basic operations.
    """
    def __init__(self, initial_balance=0):
        """
        Initialize a new bank account with an optional initial balance.

        Args:
            initial_balance (float, optional): The starting balance. Defaults to 0.
        """
        self.account_balance = initial_balance

    def deposit(self, amount):
        """
        Add the specified amount to the account balance.

        Args:
            amount (float): The amount to deposit.
        """
        self.account_balance += amount

    def withdraw(self, amount):
        """
        Withdraw the specified amount from the account if sufficient funds are available.

        Args:
            amount (float): The amount to withdraw.

        Returns:
            bool: True if withdrawal was successful, False if insufficient funds.
        """
        if amount <= self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        """
        Display the current account balance in a user-friendly format.
        """
        print(f"Current Balance: ${self.account_balance:.2f}")