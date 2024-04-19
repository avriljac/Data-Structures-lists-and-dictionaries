# Create a list containing 4 items in the cafe
menu_list = [ "Bolognaise",  "Pizza", "Fried Chips", "Burger" ]

# Create a dictionary called stock.
# Assign a stock value for each menu item
# Be mindful that calculations will be done wit the assigned numbers
# It's for this reason that we convert the string values to integers
stock_dict = {"Bolognaise": int("500"), "Pizza": int("150"), "Fried Chips": int("60"), "Burger": int("75")}

# Create a dictionary called price - for each menu item
# Be mindful that calculations will be done wit the assigned numbers
# It's for this reason that we convert the string values to integers
price_dict = {"Bolognaise": int("200"), "Pizza": int("189"), "Fried Chips": int("95"), "Burger": int("149")}

# Calculate the total stockworth
# We need to differentiate the key and the value
# In the 1st instance, item is the key  & no. of items the value
# In the 2nd instance item is the key & price is the value
# The formula: itemvalue = stock items xprice
# We want to iterate through the items on the menu list. 
# This will help us calulate the total sum of all stock value
total_stockworth = 0
for item in menu_list:
    item_value = stock_dict[item] * price_dict[item]
    total_stockworth += item_value
    
print("Total stock worth: R",total_stockworth )    