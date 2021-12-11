# Take user input for amount and percentage
# print total amount

from calculator import calculateTotal

amount = input("Amount: ")
percentage = input("Tip percentage: ") 

total = calculateTotal(float(amount), float(percentage))

print(total)