# Standard library imports

# Related third-party imports

# Local application/library specific imports
from src.customer import get_customer
from src.loan import update_loan_status
from src.eligibility import check_loan_eligibility

def process_loan_application(loan_id, customer_id):
    """
    Processes a loan application based on customer eligibility.

    Parameters:
    - loan_id (int): The unique identifier for the loan.
    - customer_id (int): The unique identifier for the customer.

    Returns:
    - bool: True if the loan application is approved, False otherwise.
    """
    customer = get_customer(customer_id)
    if customer:
        eligible = check_loan_eligibility(customer)
        if eligible:
            update_loan_status(loan_id, 'APPROVED')
            return True
        else:
            update_loan_status(loan_id, 'DENIED')
            return False
    else:
        update_loan_status(loan_id, 'CUSTOMER_NOT_FOUND')
        return False