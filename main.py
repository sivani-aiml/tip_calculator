print("welcome to tip calculator!")
bill = float(input("what was the total bill?$"))
tip = input("what percent tip you would like to give ? 10 12 15")
people = int(input("how many people is there to split the bill?"))
tip_percent = tip / 100
total_tip_amount = tip_percent * bill
total_amount = bill = total_tip_amount
bill_per_person = total_tip_amount / people
print("{bill_per_person} is the amount per person")
