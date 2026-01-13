# import csv
# from faker import Faker
# from faker_commerce import Provider
# from datetime import date, datetime


# # Initialize the Faker object
# fake = Faker()
# fake.add_provider(Provider)

# # Syntax: date(year, month, day)
# start_date = date(1996, 1, 1)
# end_date = date(2025, 12, 31)

# # Function to generate fake data
# def generate_fake_data(num_entries):
#     data = []
#     for _ in range(num_entries):
#         entry = [
#             fake.random_int(min=0, max=1000),
#             fake.random_int(min=1, max=2000),
#             fake.random_int(min=1, max=600),
#             fake.ecommerce_name().split(' ')[-1], # the .split(' ')[-1] comes from daniel 
#             fake.city(),
#             fake.date_between(start_date='-5y', end_date='today'),
#             fake.random_int(min=0, max=30),
#             fake.pyfloat(
#                 min_value=10.5,
#                 max_value=350.5,
#                 right_digits=2,
#                 positive=True)
            
#         ]
#         data.append(entry)
#     return data

# # Number of fake entries you want to generate
# num_entries = 5000

# # Generate the fake data
# sales_data = generate_fake_data(num_entries)

# # Write the data to a CSV file
# with open('salesfakecsvdata.csv', 'w', newline='') as csvfile:
#     writer = csv.writer(csvfile)
#     writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amout'])
#     writer.writerows(sales_data)

# print(f"{num_entries} fake entries have been generated and written to fakecsvdata.csv")


import csv
from faker import Faker
from datetime import date, datetime
import random

product_items = ['Laptop', 'Smartphone', 'Tablet', 'Headphones', 'Monitor', 'Keyboard', 'Mouse', 'Printer', 'Scanner', 'Webcam']
cities = ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix', 'Philadelphia', 'San Antonio', 'San Diego', 'Dallas', 'San Jose']

# Initialize the Faker object
fake = Faker()

start_date = date(2000, 1, 1)
end_date = date(2026, 12, 31)

# Function to generate fake data
def generate_fake_data(num_entries=10):
    data = []
    for _ in range(num_entries):
        entry = [
            fake.random_int(min=0, max=100),
            fake.random_int(min=50, max=999),+
            fake.random_int(min=1, max=10),
            product := random.choice(product_items), # walrus operator `:=`, will call the function everytime the loop runs, instead of just storing the value and returning the stored value each time
                                                     # pulls a random choice from a list called product items, and uses the walrus operator to reassign it each time the for loop runs
            city := random.choice(cities),

            # fake.random_company_product(),
            # fake.city(),
            fake.date_between(start_date='-5y', end_date='today'),
            fake.random_int(min=0, max=10),
            fake.pyfloat(
                min_value=10.5,
                max_value=75.5,
                right_digits=2,
                positive=True)

        ]
        data.append(entry)
    return data

# Number of fake entries you want to generate
num_entries = 1000

# Generate the fake data
sales_data = generate_fake_data(num_entries)

# Write the data to a CSV file
with open('salesfakecsvdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amount'])
    writer.writerows(sales_data)

print(f"{num_entries} fake entries have been generated and written to salesfakecsvdata.csv")