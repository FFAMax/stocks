from calculate_dividend_percentage import *

dividend_payments = [
    {
        'payment_date': '2023-04-14',
        'dividend_amount': 4.96,
        'num_shares': 8,
        'stock_price': 17.27,
    },
    {
        'payment_date': '2023-01-13',
        'dividend_amount': 1.24,
        'num_shares': 2,
        'stock_price': 17.27,
    },
    {
        'payment_date': '2022-10-14',
        'dividend_amount': 0.25,
        'num_shares': 0.4016,
        'stock_price': 22.32,
    },
    {
        'payment_date': '2022-06-15',
        'dividend_amount': 0.25,
        'num_shares': 0.4016,
        'stock_price': 22.32,
    },
    {
        'payment_date': '2022-04-14',
        'dividend_amount': 0.12,
        'num_shares': 0.2016,
        'stock_price': 22.32,
    },
    {
        'payment_date': '2022-01-14',
        'dividend_amount': 0.12,
        'num_shares': 0.2016,
        'stock_price': 22.32,
    },
]

dividend_percentage = calculate_dividend_percentage(dividend_payments)
print(dividend_percentage) # {2023: 7.180081065431384, 2022: 10.992745976060771}

