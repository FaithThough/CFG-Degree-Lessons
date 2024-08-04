# Example: Storing Product Prices
# Imagine you are managing a store's inventory, and you want to keep track of the prices of various products.
# Sometimes, the price of a product might not be entered yet, and in such cases, you want the price to be automatically set to 0

from collections import defaultdict

# Create a defaultdict with int as the default factory
product_prices = defaultdict(int) # Will set the default value to zero
# product_prices = defaultdict(lambda: 2) # Will set the default value to two
# Add product prices
product_prices['mango'] = 1.2
product_prices['cherries'] = 2.4

print("Mango price: ", product_prices['mango'])
print("Cherries price: ", product_prices['cherries'])
print("Dragonfruit price (not stored in system):", product_prices['dragonfruit'])

product_prices['dragonfruit'] = 1.6
print("Dragonfruit price (after entering) ", product_prices['dragonfruit'])

