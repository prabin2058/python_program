
total_sum=-0
item_list = []
for i in range(5):
    items=(input("enter name of items: "))
    price= int(input("enter a price: "))   
    total_sum +=price
    item_list.append((items,price))
    
print("Total price of items: ",total_sum) 
for items,price in item_list: 
 print(f"{items} : Rs. {price}") 
