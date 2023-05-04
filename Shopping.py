#!/usr/bin/env python
# coding: utf-8

# In[19]:


limit = 5000
price_sheet={'Laptop': 1500, 'Headset': 100, 'Second monitor': 200, 'Housepad': 50, 'External drive' :250}


# In[21]:


cart=[]
def add_to_cart (item, quantity):
    cart.append((item, quantity))
    item_list.remove(item)


# In[17]:


def create_invoice():
    total=0
    total_amount_inc_tax=0
    for item, quantity in cart:
        price=price_sheet[item]
        tax=0.18*price
        total=(total+price)*quantity
        total_amount_inc_tax += total
        print('Item:', item, '\t', 'Price:', price, '\t', 'Quantity:', quantity, '\t', 'Tax:', tax, '\t', 'Total:', total, '\n')
    
    print("After the taxes are applied the total amount is:", '\t', total_amount_inc_tax)
    return total_amount_inc_tax


# In[22]:


def checkout():
    global limit
    total_amount=create_invoice()
    if limit==0:
        print("You don't have any budget")
    elif total_amount>limit:
        print("The amount you have to pay in above the spending limit. You have to drop some items.")
    else:
        limit -= total_amount
        print(f"The total amount (inc1. taxes) you have paid is {total_amount}. You have {limit} dollars left")


# In[20]:


add_to_cart("Second monitor", 1)
add_to_cart("Housepad", 2)
add_to_cart("Laptop", 1)
add_to_cart("Headset", 3)
add_to_cart("External drive", 4)
checkout()

