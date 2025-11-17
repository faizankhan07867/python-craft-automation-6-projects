# 04-csv-parser.py
import csv
from collections import Counter

# Sample CSV data (save as products.csv or run directly)
csv_data = """name,price,category,stock
Terracotta Vase,899,Pottery,15
Macrame Hanging,1299,Macrame,8
Soy Candle,449,Candles,25
Beaded Necklace,1599,Jewelry,5
Ceramic Mug,599,Pottery,20"""

with open('products.csv', 'w', newline='') as f:
    f.write(csv_data)

total_value = 0
categories = []
low_stock = []

with open('products.csv') as f:
    reader = csv.DictReader(f)
    for row in reader:
        value = int(row['price']) * int(row['stock'])
        total_value += value
        categories.append(row['category'])
        if int(row['stock']) < 10:
            low_stock.append(row['name'])

print("Product Report")
print(f"Total Inventory Value: ₹{total_value}")
print(f"Categories: {', '.join(set(categories))}")
print(f"Low Stock Items (<10): {', '.join(low_stock) if low_stock else 'None'}")
