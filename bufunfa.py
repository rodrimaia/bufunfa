#!/usr/bin/env python3

import sys
import requests

SOURCE = "https://api.exchangeratesapi.io/latest?base=USD"


def output(raw_conversion, converted_salary, dollar_price, exchange_rate):
    fix = lambda value: round(value, 2)

    return " raw conversion: {}\n Your salary: {}\n conversion loss: {}\n dollar price: {}\n dollar prince considering conversion loss: {}".format( fix(raw_conversion), fix(converted_salary), fix(raw_conversion - converted_salary), fix(dollar_price), fix(exchange_rate)
    )

def calculate(salary, dollar):
    dollar_price = dollar
    raw_conversion = salary * dollar_price
    exchange_rate = dollar_price - (dollar_price * 0.02)
    converted_salary = (salary - 3) * exchange_rate

    return output(raw_conversion, converted_salary, dollar_price, exchange_rate)

if __name__ == "__main__":
    params = sys.argv[1:]

    salary = 0
    dollar_price = requests.get(SOURCE).json()['rates']['BRL']

    if len(params) > 0:
        salary = params[0]

        if len(params) > 1:
            dollar_price = params[1]

    print(calculate(float(salary), float(dollar_price)))
