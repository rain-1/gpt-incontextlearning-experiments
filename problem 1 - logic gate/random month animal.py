import random

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

random_month = random.choice(months)
random_animal = random.choice(animals)

print(f"Random month: {random_month}")
print(f"Random animal: {random_animal}")
