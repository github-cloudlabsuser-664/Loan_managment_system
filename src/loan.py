import csv
import os
from datetime import datetime

LOAN_FILE = 'data/loans.csv'

def get_next_loan_id():
    """
    Retrieves the next available loan ID from the loans file.

    Returns:
    - int: The next available loan ID.
    """
    if not os.path.exists(LOAN_FILE):
        return 1
    with open(LOAN_FILE, mode='r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        return int(rows[-1][0]) + 1 if rows else 1

def apply_loan(customer_id, amount, term, interest_rate):
    """
    Applies for a loan and writes the details to the loans file.

    Parameters:
    - customer_id (int): The customer's ID.
    - amount (float): The amount of the loan.
    - term (int): The term of the loan in months.
    - interest_rate (float): The interest rate of the loan.

    Returns:
    - int: The loan ID of the newly applied loan.
    """
    loan_id = get_next_loan_id()
    with open(LOAN_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([loan_id, customer_id, amount, term, interest_rate, datetime.now().date(), 'PENDING'])
    return loan_id

def update_loan_status(loan_id, new_status):
    """
    Updates the status of a loan in the loans file.

    Parameters:
    - loan_id (int): The loan ID.
    - new_status (str): The new status of the loan.
    """
    temp_file = LOAN_FILE + '.tmp'
    with open(LOAN_FILE, mode='r') as infile, open(temp_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)
        header = next(reader)  # Read the header row
        writer.writerow(header)  # Write the header row to the temp file

        for row in reader:
            if int(row[0]) == loan_id:
                row[-1] = new_status  # Update the status
            writer.writerow(row)
    
    os.replace(temp_file, LOAN_FILE)  # Replace the original file with the updated temp file