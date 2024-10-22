cart = ShoppingCart()
cart.add_item('Apple', 0.5, 3)
cart.add_item('Banana', 0.3, 5)
cart.add_item('Apple', 0.5, 2)
# You may implement fluent interface as well:
# cart.add_item('Apple', 0.5, 3).add_item('Banana', 0.3, 5).add_item('Apple', 0.5, 2)
print(cart)  # Should display the items and total cost
print(f"Total items: {len(cart)}")  # Should display total unique items in the cart
