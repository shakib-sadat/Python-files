print("Welcome to tip calculator.")
total_bill = float(input("What was the total bill?"))
percentage_bill = int(
    input("What percentage tip would you like to give? 10,12, or 15?"))
percentage_calc = (percentage_bill / 100) * total_bill + total_bill
people = int(input("How many people to slit the bill?"))
pay_bill = (percentage_calc / people)
final_amount = "{:.2f}".format(pay_bill)

print(f"Each person should pay: {final_amount}")
