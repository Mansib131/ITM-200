import csv
import matplotlib.pyplot as plt

# Step 1: Reading CSV File
with open('Data.csv') as file:
    reader = csv.reader(file)
    data = [row for row in reader]

# Print the contents
for row in data:
    print(row)

# Step 2: Total Sale
total_sales = {}
for row in data[1:]:
    year = row[0][:4]
    if year not in total_sales:
        total_sales[year] = 0
    total_sales[year] += int(row[1])

# Write to stats.txt file
with open('stats.txt', 'w') as file:
    for year, sales in total_sales.items():
        file.write(f'Total sales in {year}: {sales}\n')

# Step 3: Bar Plot
years = list(total_sales.keys())
sales = list(total_sales.values())
plt.bar(years, sales)
plt.xlabel('Year')
plt.ylabel('Total Sales')
plt.title('Total Automotive Sales per Year')
plt.show()

# Step 4: Sale Estimation
total_sales_2021 = sum([int(row[1]) for row in data[1:13]])
total_sales_2022 = sum([int(row[1]) for row in data[13:]])

SGR = (total_sales_2022 - total_sales_2021) / total_sales_2021
with open('stats.txt', 'a') as file:
    file.write(f'Sales Growth Rate: {SGR:.2%}\n')

estimated_sales_2022 = {}
for i in range(13, len(data)):
    month = data[i][0][-2:]
    prev_sales = int(data[i-12][1])
    estimated_sales = prev_sales + (prev_sales * SGR)
    estimated_sales_2022[month] = estimated_sales

with open('stats.txt', 'a') as file:
    file.write('Estimated sales for last 6 months of 2022:\n')
    for month, sales in estimated_sales_2022.items():
        file.write(f'{month}-2022: {sales:.0f}\n')

# Step 5: Horizontal Bar Plot
months = list(estimated_sales_2022.keys())
sales = list(estimated_sales_2022.values())
plt.barh(months, sales)
plt.xlabel('Estimated Sales')
plt.ylabel('Month')
plt.title('Estimated Automotive Sales for Last 6 Months of 2022')
plt.show()
