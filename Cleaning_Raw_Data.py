
raw_products = ["  apple", "Banana ", "Mango", "banana", " ", "apple  ", "ORANGE", "grapes", "mango  "]

""""
Remove any empty strings or items with only spaces.

Convert all product names to lowercase.

Remove duplicates.

Sort the final list alphabetically.

Print the cleaned list.

"""
# Step 1: Remove spaces
cleaned=[]
for product in raw_products:
    cleaned.append(product.strip())

# Step 2: Remove empty strings
cleaned=[product for product in cleaned if product!="" ]

# Step 3: Convert all to lowercase
cleaned=[product.lower() for product in cleaned]

# Step 4: Remove duplicates
cleaned=list(set(cleaned))

# Step 5: Sort alphabetically
cleaned.sort() 

print(cleaned)




