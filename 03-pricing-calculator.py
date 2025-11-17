# 03-pricing-calculator.py
def calculate_price():
    cost = float(input("Enter cost price: ₹"))
    profit_margin = float(input("Profit margin % (e.g. 50): "))
    discount = float(input("Discount % (optional, 0 if none): ") or 0)
    
    selling_price = cost * (1 + profit_margin/100)
    gst = selling_price * 0.18
    final_price = selling_price + gst
    after_discount = final_price * (1 - discount/100)
    
    print("\nPricing Breakdown")
    print(f"Cost Price       : ₹{cost:.2f}")
    print(f"Selling Price    : ₹{selling_price:.2f}")
    print(f"GST (18%)        : ₹{gst:.2f}")
    print(f"Final Price      : ₹{final_price:.2f}")
    if discount > 0:
        print(f"After {discount}% off → ₹{after_discount:.2f}")

calculate_price()
