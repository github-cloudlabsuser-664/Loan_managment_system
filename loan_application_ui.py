import tkinter as tk
from tkinter import messagebox
from src.customer import add_customer
from src.loan import apply_loan
from src.repayment import calculate_monthly_payment, generate_repayment_schedule
from src.utils import process_loan_application

class LoanApplicationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Loan Application")
        self.geometry("400x400")

        # Customer Details
        self.customer_name_label = tk.Label(self, text="Customer Name:")
        self.customer_name_label.pack()
        self.customer_name_entry = tk.Entry(self)
        self.customer_name_entry.pack()

        self.age_label = tk.Label(self, text="Age:")
        self.age_label.pack()
        self.age_entry = tk.Entry(self)
        self.age_entry.pack()

        self.income_label = tk.Label(self, text="Income:")
        self.income_label.pack()
        self.income_entry = tk.Entry(self)
        self.income_entry.pack()

        self.credit_score_label = tk.Label(self, text="Credit Score:")
        self.credit_score_label.pack()
        self.credit_score_entry = tk.Entry(self)
        self.credit_score_entry.pack()

        # Loan Details
        self.loan_amount_label = tk.Label(self, text="Loan Amount:")
        self.loan_amount_label.pack()
        self.loan_amount_entry = tk.Entry(self)
        self.loan_amount_entry.pack()

        self.loan_term_label = tk.Label(self, text="Loan Term (months):")
        self.loan_term_label.pack()
        self.loan_term_entry = tk.Entry(self)
        self.loan_term_entry.pack()

        self.interest_rate_label = tk.Label(self, text="Interest Rate (%):")
        self.interest_rate_label.pack()
        self.interest_rate_entry = tk.Entry(self)
        self.interest_rate_entry.pack()

        # Button
        self.apply_loan_button = tk.Button(self, text="Apply for Loan", command=self.apply_loan)
        self.apply_loan_button.pack()

    def apply_loan(self):
        customer_name = self.customer_name_entry.get()
        age = int(self.age_entry.get())
        income = float(self.income_entry.get())
        credit_score = int(self.credit_score_entry.get())

        loan_amount = float(self.loan_amount_entry.get())
        loan_term = int(self.loan_term_entry.get())
        interest_rate = float(self.interest_rate_entry.get())

        customer_id = add_customer(customer_name, age, income, credit_score)
        loan_id = apply_loan(customer_id, loan_amount, loan_term, interest_rate)

        if process_loan_application(loan_id, customer_id):
            monthly_payment = calculate_monthly_payment(loan_amount, interest_rate, loan_term)
            repayment_schedule = generate_repayment_schedule(loan_amount, interest_rate, loan_term)
            messagebox.showinfo("Loan Status", f"Loan approved\nMonthly Payment: ${monthly_payment:.2f}\nRepayment Schedule:\n{repayment_schedule}")
        else:
            messagebox.showinfo("Loan Status", "Loan denied")

if __name__ == "__main__":
    app = LoanApplicationApp()
    app.mainloop()
