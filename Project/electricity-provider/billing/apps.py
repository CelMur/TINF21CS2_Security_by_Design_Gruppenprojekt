from django.apps import AppConfig


class BillingConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'billing'

from datetime import datetime, timedelta

class Customer:
    def __init__(self, pricing_plan): # Müssen wir aus einer Datenbank ziehen
        self.pricing_plan =  {} # Vertrag
        self.past_value = 0
        self.complete_value = 0
        self.current_value = 0
        self.current_bill = 0
        self.bill_history = []


    def calculate_bill(self):
        # Assuming the function is called at the end of the month
        now = datetime.now()
        last_day_of_month = (datetime(now.year, now.month % 12 + 1, 1) - timedelta(days=1)).day

        # Calculate the bill for the current month
        self.current_bill = self.current_value * self.pricing_plan
        self.past_value += self.current_value

        # Record the bill in the history
        bill_entry = {
            "month": now.month,
            "year": now.year,
            "past_value": self.past_value,
            "current_value": self.current_value,
            "pricing_plan": self.pricing_plan,
            "bill_amount": self.current_bill
        }
        self.bill_history.append(bill_entry)

        # Reset current value for the next month
        self.current_value = 0

        return self.current_bill

    def view_bill_history(self):
        return self.bill_history

# Example usage:
customer = Customer(pricing_plan=0.30)
customer.current_value = 150  # Example current consumption
bill_amount = customer.calculate_bill()
print(f"Current bill: ${bill_amount}")
print("Bill history:")
for entry in customer.view_bill_history():
    print(entry)
