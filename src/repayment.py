import csv

def calculate_monthly_payment(loan_amount, interest_rate, loan_term):
    """
    Calculates the monthly payment for a loan based on the loan amount, interest rate, and loan term.

    Parameters:
    - loan_amount (float): The total amount of the loan.
    - interest_rate (float): The annual interest rate of the loan.
    - loan_term (int): The term of the loan in years.

    Returns:
    - float: The monthly payment amount.
    """
    monthly_interest_rate = interest_rate / 12 / 100
    num_payments = loan_term * 12
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -num_payments)
    return monthly_payment

def generate_repayment_schedule(loan_amount, interest_rate, loan_term):
    """
    Generates a repayment schedule for a loan based on the loan amount, interest rate, and loan term.

    Parameters:
    - loan_amount (float): The total amount of the loan.
    - interest_rate (float): The annual interest rate of the loan.
    - loan_term (int): The term of the loan in years.

    Returns:
    - list of dict: A list of dictionaries, each representing a monthly payment.
    """
    monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)
    remaining_balance = loan_amount
    repayment_schedule = []

    for month in range(1, loan_term * 12 + 1):
        interest_payment = remaining_balance * (interest_rate / 12 / 100)
        principal_payment = monthly_payment - interest_payment
        remaining_balance -= principal_payment

        repayment_schedule.append({
            'Month': month,
            'Principal Payment': principal_payment,
            'Interest Payment': interest_payment,
            'Remaining Balance': remaining_balance
        })

    return repayment_schedule


def read_csv_to_dict(filename):
    """
    Reads a CSV file and returns a list of dictionaries, one per row.
    """
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        return list(reader)

def find_customer_by_id(customer_id, customers):
    """
    Finds a customer by ID in the list of customer dictionaries.
    """
    for customer in customers:
        if customer['customer_id'] == str(customer_id):
            return customer
    return None

def find_loan_by_id(loan_id, loans):
    """
    Finds a loan by ID in the list of loan dictionaries.
    """
    for loan in loans:
        if loan['loan_id'] == str(loan_id):
            return loan
    return None

def handle_late_payment(customer_id, loan_id, late_payment_amount):
    """
    Handles a late payment for a customer's loan by updating the remaining balance and payment status.
    """
    customers = read_csv_to_dict('customers.csv')
    loans = read_csv_to_dict('loans.csv')

    customer = find_customer_by_id(customer_id, customers)
    loan = find_loan_by_id(loan_id, loans)

    if not customer:
        print(f"No customer found with ID {customer_id}.")
        return
    if not loan:
        print(f"No loan found with ID {loan_id}.")
        return
    if loan['customer_id'] != str(customer_id):
        print(f"Loan ID {loan_id} does not belong to customer ID {customer_id}.")
        return

    # Assuming loans.csv has a 'remaining_balance' field for simplicity
    remaining_balance = float(loan['amount']) + late_payment_amount  # Simplified calculation
    loan['status'] = 'Late'

    print(f"Late payment of ${late_payment_amount} processed for loan ID {loan_id}. Remaining balance: ${remaining_balance}.")

