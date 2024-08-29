def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    
    :param price: Original price of the item
    :param discount_percent: Discount percentage to apply
    :return: Final price after discount or original price if discount is less than 20%
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Prompt user for input
original_price = float(input("Enter the original price of the item: "))
discount_percentage = float(input("Enter the discount percentage: "))

# Calculate final price using the function
final_price = calculate_discount(original_price, discount_percentage)

# Print the final price
if final_price == original_price:
    print(f"No discount applied. The price remains: ${original_price:.2f}")
else:
    print(f"The final price after applying the discount is: ${final_price:.2f}")
