print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage_tip = int(input("What percentage tip would you like to give? "))
people = int(input("How many people to split the bill? "))

total = round((total_bill + (total_bill * percentage_tip / 100)) / people, 2)   # round to 2 digits
print(f"Each person should pay: ${total}")