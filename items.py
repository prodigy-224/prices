def calculate_discount(price, discount_percent):

    if(discount_percent >= 20):
        final_price = price - (discount_percent * price / 100)
        print("The final buying price of the item is: ",final_price)
    else:
        print("The final price of the item is : ", price)

price =float(input("Enter the price: "))
discount_percent =float(input("Enter the discount: "))


calculate_discount(price, discount_percent)


