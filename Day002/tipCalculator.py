print("Welcome to the tip calculator.")
bill = float(input("How much was the bill?\n"))
tip_percent = float(input("What percentage tip would you like to give?\n"))
total_people = int(input("How many people are splitting this bill?\n"))

total_bill = ((tip_percent/100)*bill) + bill
amount_payment = total_bill / total_people

print(f"Each person should pay about {amount_payment}")
