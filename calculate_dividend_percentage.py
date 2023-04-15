from typing import List
from datetime import datetime

def calculate_dividend_percentage(dividend_payments: List[dict]) -> dict:
    dividend_percentage = {}

    # group dividend payments by year
    grouped_dividend_payments = {}
    for payment in dividend_payments:
        year = datetime.strptime(payment['payment_date'], '%Y-%m-%d').year
        if year not in grouped_dividend_payments:
            grouped_dividend_payments[year] = {
                'total_dividend_amount': 0,
                'total_stock_price': 0,
                'num_payments': 0,
            }
        grouped_dividend_payments[year]['total_dividend_amount'] += payment['dividend_amount']
        grouped_dividend_payments[year]['total_stock_price'] += payment['stock_price'] * payment['num_shares']
        grouped_dividend_payments[year]['num_payments'] += 1

    # calculate dividend percentage for each year
    for year, data in grouped_dividend_payments.items():
        avg_stock_price = data['total_stock_price'] / data['num_payments']
        dividend_percentage[year] = (data['total_dividend_amount'] / avg_stock_price) * 100

    return dividend_percentage

