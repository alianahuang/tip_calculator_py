
def calculateTip(amount, percentage):
    return amount * percentage

def calculateTotal(amount, percentage):
    return amount + calculateTip(amount, percentage)