# 02-description-generator.py
import random

templates = [
    "Handcrafted {name} made with love using premium {material}. Perfect for {use}.",
    "Beautiful artisanal {name} – {material} finish, {adjective} design, ideal for {use}.",
    "100% handmade {name} crafted from eco-friendly {material}. A timeless piece for {use}."
]

adjectives = ["elegant", "minimalist", "boho", "rustic", "luxurious", "vibrant"]
uses = ["home decor", "gifting", "daily use", "special occasions", "meditation"]

products = [
    {"name": "Terracotta Vase", "material": "clay"},
    {"name": "Macrame Wall Hanging", "material": "cotton rope"},
    {"name": "Scented Soy Candle", "material": "soy wax"},
    {"name": "Beaded Necklace", "material": "glass beads"}
]

for p in products:
    desc = random.choice(templates).format(
        name=p["name"],
        material=p["material"],
        adjective=random.choice(adjectives),
        use=random.choice(uses)
    )
    print(f"✨ {p['name']}\n{desc}\n")
