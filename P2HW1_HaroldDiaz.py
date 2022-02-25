# A brief description of the project
# 2/25/2022
# CTI-110 P2HW1 - Total Purchases
# Harold Diaz
#
# Ask user to enter prices of 5 items INDIVIDUALLY.
# Calculate Subtotal (sum of all item prices entered) 
# Calculate Sales tax of item prices entered. Assume sales tax is 7% (subtotal * 7%)
# Calculate total (subtotal + sales tax)
# Display the Subtotal, Sales Tax, and Total Prices in 3 separate lines under "Results".
# Format calculated amounts rounded to 2 decimal positions.



item_1 = float(input('Enter the price of item #1:'))
item_2 = float(input('Enter the price of item #2:'))
item_3 = float(input('Enter the price of item #3:'))
item_4 = float(input('Enter the price of item #4:'))
item_5 = float(input('Enter the price of item #5:'))

subtotal = item_1 + item_2 + item_3 + item_4 + item_5
sales_tax = (subtotal * 0.07)
total = subtotal + sales_tax

print()
print('--------Results--------')
print('Subtotal:',f'{subtotal:.2f}')
print('Sales Tax:',f'{sales_tax:.2f}')
print('Total:',f'{total:.2f}')
             
