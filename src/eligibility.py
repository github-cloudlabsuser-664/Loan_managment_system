def check_credit_score(customer):
    """
    Check the credit score of a customer to determine loan eligibility.

    Parameters:
    - customer (dict): The customer's information.

    Returns:
    - bool: True if the customer's credit score is above a certain threshold, False otherwise.
    """
    threshold = 700  # Example threshold
    return customer['credit_score'] >= threshold

def check_income_level(customer):
    """
    Check the income level of a customer to determine loan eligibility.

    Parameters:
    - customer (dict): The customer's information.

    Returns:
    - bool: True if the customer's income meets the minimum requirement, False otherwise.
    """
    minimum_income = 30000  # Example minimum income
    return customer['income'] >= minimum_income

def check_loan_eligibility(customer):
    """
    Check the eligibility of a customer for a loan.

    Parameters:
    - customer (dict): The customer's information.

    Returns:
    - bool: True if the customer meets all the eligibility criteria, False otherwise.
    """
    credit_score_eligible = check_credit_score(customer)
    income_level_eligible = check_income_level(customer)

    return credit_score_eligible and income_level_eligible