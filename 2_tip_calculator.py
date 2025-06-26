# This is a tip calculator, it'll take the total bill
# and divide it by the number of people who will pay,
# including the tip in the full price

# Isso é uma calculadora de gorjeta, ela pega o valor total,
# incluindo a gorjeta, e divide pelo número de pessoas que vai pagar

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? "))
percentage = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))
individual_price = (total_bill / people) * ((percentage / 100) + 1)
rounded_price = round(individual_price, 2)
print(f"Each person should pay ${rounded_price: .2f}")
