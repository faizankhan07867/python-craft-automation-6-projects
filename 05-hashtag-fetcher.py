# 05-hashtag-fetcher.py
import random
import time

trending = [
    "#HandmadeWithLove", "#SmallBusiness", "#ShopLocal", "#Handcrafted",
    "#ArtisanMade", "#SupportSmall", "#MadeInIndia", "#EtsyFinds",
    "#HandmadeIsBetter", "#CraftPosh", "#VocalForLocal", "#DesiVibes"
]

print("Fetching trending hashtags...")
time.sleep(2)

selected = random.sample(trending, 8)
print("Recommended Hashtags for your craft post:")
for tag in selected:
    print(tag)
print("\nCopy & paste kar do Instagram pe!")
