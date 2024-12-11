a=int(input("Enter the number of items you want to purchase: "))
items=[]
item_price=[]
#inputs
for i in range (a):
    item=str(input(f"\nEnter item{i+1}'s name : "))
    price=int(input(f"Enter {item}'s price per unit: "))
    qty=int(input(f"Enter item {item}'s quantity: "))
    items.append(item)
    total_item=price*qty
    item_price.append(total_item)
#bill
print("\nITEMS PURCHASED:")
for j in range(a):
    print(f"{j+1}. {items[j]}-{item_price[j]} rupees")

thousand=sum(item_price) 
discount = thousand*0.15
thousand = thousand-discount
if thousand < 1000:
    print("\n\nTOTAL BILL")
    print(f"{sum(item_price)} only")
else:
    print(f"\n\nTOTAL BILL: {sum(item_price)}.00 only")
    print("Discount applied: 15%")
   
    print(f"Discounted price: {thousand}")
