from forex_python.converter import CurrencyRates 
c = CurrencyRates()
amount = int(input("Enter the amount :"))
from_currency = input("Enter From Currency :")
to_currency = input("Enter To Currency :")

result = c.convert(from_currency, to_currency, amount)
print(result)
