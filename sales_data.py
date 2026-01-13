import csv
from faker import Faker
from datetime import date

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
            fake.random_int(min=50, max=999),
            fake.random_int(min=1, max=10),
            fake.name(),
            fake.city(),
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
num_entries = 10

# Generate the fake data
sales_data = generate_fake_data(num_entries)

# Write the data to a CSV file
with open('salesfakecsvdata.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['order_id', 'product_id', 'store_id', 'product_name', 'city', 'date_of_sale', 'quantity', 'sales_amout'])
    writer.writerows(sales_data)

print(f"{num_entries} fake entries have been generated and written to fakecsvdata.csv")
