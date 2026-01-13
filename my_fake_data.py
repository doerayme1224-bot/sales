import csv
from faker import Faker
from faker_commerce import Provider
from datetime import date, datetime


# Initialize the Faker object
fake = Faker()
fake.add_provider(Provider)

# Syntax: date(year, month, day)
start_date = date(1996, 1, 1)
end_date = date(2025, 12, 31)

# Function to generate fake data
def generate_fake_data(num_entries):
    data = []
    for _ in range(num_entries):
        entry = [
            fake.random_int(min=0, max=1000),
            fake.random_int(min=1, max=2000),
            fake.random_int(min=1, max=600),
            fake.ecommerce_name(),
            fake.city(),
            fake.date_between(start_date='-5y', end_date='today'),
            fake.random_int(min=0, max=30),
            fake.pyfloat(
                min_value=10.5,
                max_value=350.5,
                right_digits=2,
                positive=True)
            
        ]
        data.append(entry)
    return data

# Number of fake entries you want to generate
num_entries = 5000

# Generate the fake data
sales_data = generate_fake_data(num_entries)

# Write the data to a CSV file
with open('salesfakecsvdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amout'])
    writer.writerows(sales_data)

print(f"{num_entries} fake entries have been generated and written to fakecsvdata.csv")
