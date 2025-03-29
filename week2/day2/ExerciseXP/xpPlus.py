#1

student_grades = {
    "Alice": [88, 92, 100],
    "Bob": [75, 78, 80],
    "Charlie": [92, 90, 85],
    "Dana": [83, 88, 92],
    "Eli": [78, 80, 72]
}

student_averages = {}
student_letter_grades = {}
total_average = 0

for student, grades in student_grades.items():
    average = sum(grades) / len(grades)
    student_averages[student] = average
    
    if average >= 90:
        letter_grade = "A"
    elif average >= 80:
        letter_grade = "B"
    elif average >= 70:
        letter_grade = "C"
    elif average >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"
    
    student_letter_grades[student] = letter_grade
    total_average += average

class_average = total_average / len(student_grades)

print("Class average:", round(class_average, 2))
print("\nStudent Summary Report:")
for student in student_averages:
    print(f"{student}: Average Grade = {round(student_averages[student], 2)}, Letter Grade = {student_letter_grades[student]}")

#2
sales_data = [
    {"customer_id": 1, "product": "Smartphone", "price": 600, "quantity": 1, "date": "2023-04-03"},
    {"customer_id": 2, "product": "Laptop", "price": 1200, "quantity": 1, "date": "2023-04-04"},
    {"customer_id": 1, "product": "Laptop", "price": 1000, "quantity": 1, "date": "2023-04-05"},
    {"customer_id": 2, "product": "Smartphone", "price": 500, "quantity": 2, "date": "2023-04-06"},
    {"customer_id": 3, "product": "Headphones", "price": 150, "quantity": 4, "date": "2023-04-07"},
    {"customer_id": 3, "product": "Smartphone", "price": 550, "quantity": 1, "date": "2023-04-08"},
    {"customer_id": 1, "product": "Headphones", "price": 100, "quantity": 2, "date": "2023-04-09"},
]

total_sales = {}
for transaction in sales_data:
    product = transaction["product"]
    total_price = transaction["price"] * transaction["quantity"]
    if product in total_sales:
        total_sales[product] += total_price
    else:
        total_sales[product] = total_price

customer_spending = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    total_price = transaction["price"] * transaction["quantity"]
    if customer_id in customer_spending:
        customer_spending[customer_id] += total_price
    else:
        customer_spending[customer_id] = total_price

for transaction in sales_data:
    transaction["total_price"] = transaction["price"] * transaction["quantity"]

high_value_transactions = [transaction for transaction in sales_data if transaction["total_price"] > 500]
high_value_transactions.sort(key=lambda x: x["total_price"], reverse=True)

purchase_counts = {}
for transaction in sales_data:
    customer_id = transaction["customer_id"]
    if customer_id in purchase_counts:
        purchase_counts[customer_id] += 1
    else:
        purchase_counts[customer_id] = 1
loyal_customers = [customer_id for customer_id, count in purchase_counts.items() if count > 2]

print("Total Sales:", total_sales)
print("Customer Spending:", customer_spending)
print("First Two Sales Data Entries:", sales_data[:2])
print("Loyal Customers:", loyal_customers)

average_transaction_value = {}
for product in total_sales.keys():
    total_quantity = sum(transaction["quantity"] for transaction in sales_data if transaction["product"] == product)
    average_transaction_value[product] = total_sales[product] / total_quantity

product_quantities = {product: sum(transaction["quantity"] for transaction in sales_data if transaction["product"] == product) for product in set(transaction["product"] for transaction in sales_data)}
most_popular_product = max(product_quantities, key=product_quantities.get)

print("Average Transaction Value:", average_transaction_value)
print("Most Popular Product:", most_popular_product)