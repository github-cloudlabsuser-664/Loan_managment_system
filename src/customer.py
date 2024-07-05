# Standard library imports
import csv
import os

# Constants
CUSTOMER_FILE = 'data/customers.csv'

def add_customer(name, age, income, credit_score):
    """
    Adds a new customer to the customer file.

    Parameters:
    - name (str): The name of the customer.
    - age (int): The age of the customer.
    - income (float): The income of the customer.
    - credit_score (int): The credit score of the customer.

    Returns:
    - int: The customer ID of the newly added customer.
    """
    customer_id = get_next_customer_id()
    with open(CUSTOMER_FILE, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([customer_id, name, age, income, credit_score])
    return customer_id

def get_next_customer_id():
    """
    Retrieves the next available customer ID.

    Returns:
    - int: The next available customer ID.
    """
    if not os.path.exists(CUSTOMER_FILE):
        return 1
    with open(CUSTOMER_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        rows = list(reader)
        return int(rows[-1][0]) + 1 if rows else 1

def get_customer(customer_id):
    """
    Retrieves a customer's information by their ID.

    Parameters:
    - customer_id (int): The unique identifier for the customer.

    Returns:
    - dict: A dictionary containing the customer's information if found, otherwise None.
    """
    with open(CUSTOMER_FILE, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            if int(row[0]) == customer_id:
                return {
                    'id': int(row[0]),
                    'name': row[1],
                    'age': int(row[2]),
                    'income': float(row[3]),
                    'credit_score': int(row[4])
                }
    return None