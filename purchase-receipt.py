"""
Tasks:

    Ask the user for their name and the amount of their purchase.
    Calculate tax, assuming a tax rate of 10%.
    Display an attractive report showing the results, match the example below:

Hello John, here is your sales receipt:
Subtotal = $ 1,234.56
     Tax = $   123.46
             --------
   Total = $ 1,358.02

"""
name = input("Enter your name: ")
amount = float(input("Enter the amount for the purchase. Do not include the $ sign: "))
tax = 0.1 * amount 
Total = amount + tax 
msg = "Hello {}, here is your sales receipt: \nSubtotal = ${:.2f} \nTax = ${:.2f} \n........... \nTotal = ${:.2f}"
print(msg.format(name, amount, tax, Total))