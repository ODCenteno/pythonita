# create a product and price for three items
p1_name, p1_price = "Books", 49.95
p2_name, p2_price = "Computer", 579.99
p3_name, p3_price = "Monitor", 124.89

# create a company name and information
company_name = "la buena vida LTD"
company_address = "Caminos de Michoacan 237"
company_city = "México, MX"

# declare ending message
message = "Thanks for shopping with us today!"

# Create a top border
print(f'\n{"*" * 50}')

# Printing the company information
print(f'\n\t\t{company_name}\n\t\t{company_address}\n\t\t{company_city}')

# Printing a line between sections
print(f'\n{"=" * 50}')

# Printing a Header for the products section
print(f'\n\tProduct Name\tProduct Price')

# Create a print statement for each product
print(f'\n\t{p1_name}\t\t$ {p1_price}')
print(f'\n\t{p2_name}\t$ {p3_price}')
print(f'\n\t{p3_name}\t\t$ {p3_price}')

# Printing a line between sections
print(f'\n{"=" * 50}')

# print out header for section of total
print(f"\t\tTotal = $ {p1_price + p3_price + p2_price}")

# Printing a line between sections
print(f'\n{"=" * 50}')

# Out thank you message
print(f'\n\tThanks for shopping with us today!')

# Create a bottom border
print(f'\n{"*" * 50}')