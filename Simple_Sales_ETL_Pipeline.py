
#Step 1 — Extract (E)

# Raw sales data (like from a CSV or API)

sales_data = [
    {"id": 1, "product": "Laptop", "price": 900, "quantity": 1, "status": "completed"},
    {"id": 2, "product": "Mouse", "price": 20, "quantity": 5, "status": "completed"},
    {"id": 3, "product": "Keyboard", "price": 45, "quantity": 2, "status": "failed"},
    {"id": 4, "product": "Monitor", "price": 200, "quantity": 1, "status": "completed"},
    {"id": 5, "product": "Cable", "price": None, "quantity": 3, "status": "completed"}
]

#Step 2 — Transform (T)

#Remove any records with missing prices

#Keep only completed transactions

#Add a new field — total_amount = price * quantity

cleaned_sales = []

for sale in sales_data:
    if sale["status"] == "completed" and sale["price"] is not None:
        total = sale["price"] * sale["quantity"]
        sale["total_amount"] = total
        cleaned_sales.append(sale)

#Step 3 — Load (L)

#Now, we’ll calculate total revenue and show the final cleaned dataset.

total_revenue = 0

for record in cleaned_sales:
    total_revenue += record["total_amount"]

print("Cleaned Data:")
for record in cleaned_sales:
    print(record)

print("\nTotal Revenue:", total_revenue)
