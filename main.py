# Standard library imports
import uuid

# Related third-party imports

# Local application/library specific imports
from src.customer import add_customer
from src.loan import apply_loan
from src.repayment import calculate_monthly_payment, generate_repayment_schedule, handle_late_payment
from src.utils import process_loan_application

def main():
    """
    Main function to demonstrate customer addition, loan application, processing, and repayment calculation.
    """
    # Add customers
    customer_id = add_customer("Anish Talkudar", 30, 45000, 720)
    print(f"Customer added with ID: {customer_id}")

    # Apply for a loan
    loan_id = apply_loan(customer_id, 5000, 24, 5.0)
    print(f"Loan applied with ID: {loan_id}")

    # Process loan application
    if process_loan_application(loan_id, customer_id):
        print("Loan approved")
    else:
        print("Loan denied")

    # Calculate monthly repayment
    monthly_payment = calculate_monthly_payment(5000, 5.0, 24)
    print(f"Monthly payment: ${monthly_payment:.2f}")

    # Generate repayment schedule
    repayment_schedule = generate_repayment_schedule(5000, 5.0, 24)
    print("Repayment Schedule:")
    for payment in repayment_schedule:
        print(payment)

    # # Handle a late payment
    # handle_late_payment(customer_id, loan_id, 100)  # Example late payment amount
    # print("Late payment handled.")

if __name__ == "__main__":
    main()