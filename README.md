# KSA Money Dispenser

## Introduction
The **KSA Money Dispenser** is a Python-based program that simulates a vending machine-like system where users insert money to pay for randomly generated prices. The program calculates change based on available denominations and ensures proper transaction handling. 

This project is useful for simulating money exchange scenarios, testing currency breakdown logic, and improving user interaction with automated payment systems.

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Dependencies](#dependencies)
- [Challenges and Solutions](#challenges-and-solutions)
- [License](#license)
- [Contact Information](#contact-information)

## Installation
To run the **KSA Money Dispenser**, follow these steps:

1. Ensure you have Python installed (version 3.6 or higher).
2. Clone or download this repository.
3. Navigate to the project directory.
4. Run the script using the command:

   ```bash
   python money_dispenser.py
No additional installation of dependencies is required.

## Usage
Run the program.
A random total price will be generated.
Insert money using valid denominations.
The program will provide change if needed.
A transaction summary will be displayed after each purchase.
You can continue transactions or exit the program.

Example Run:
Welcome to the KSA Money Dispenser!

Total price: 175.49 SAR
Insert money (0.05, 0.1, 0.25, 0.5, 1, 2, 5, 10, 20, 50, 100, 200, 500 SAR) or 'exit' to quit: 200
Inserted: 200.00 SAR, Remaining: 0.00 SAR
Change: 24.51 SAR
Warning: Unable to return exact change. Remaining balance retained: 0.01 SAR
 - 1 x 20.00 SAR
 - 2 x 2.00 SAR
 - 1 x 0.50 SAR

Transaction Summary:
 - Total transactions: 1
 - Total amount processed: 175.49 SAR
 - Total change given: 24.50 SAR
 - Total retained balance due to unavailable change: 0.01 SAR
Continue? (yes/no): no

Thank you for using the KSA Money Dispenser!

## Features
Simulates real-world money transactions.
Handles various denominations.
Provides accurate change with a breakdown of bills and coins.
Manages floating-point precision issues.
Maintains transaction history.

## Dependencies
Python's built-in random module.

## Challenges and Solutions
Challenge: Floating-Point Precision Issues
Issue: When performing calculations on money values, floating-point precision errors caused incorrect change calculations.

Solution: Used round(amount, 2) consistently after each mathematical operation to ensure accurate currency representation.

Challenge: Handling Invalid Inputs
Issue: Users might enter invalid denominations or non-numeric values.

Solution: Implemented exception handling (try-except) and conditional checks to ensure only valid numerical inputs are accepted.

Challenge: Providing Exact Change
Issue: Some transactions resulted in leftover amounts that could not be returned due to the absence of exact denominations.

Solution: The program notifies the user if exact change cannot be given and keeps track of unreturned amounts.

## License
This project is licensed under the MIT License.

## Contact Information
For any questions or feedback, feel free to reach out at [Sultanalbayyat@gmail.com].

