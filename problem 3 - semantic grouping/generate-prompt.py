import random

# List of animals
animals = ['lion', 'tiger', 'elephant', 'giraffe', 'zebra']

# List of household objects
household_objects = ['chair', 'table', 'lamp', 'couch', 'bookshelf']

# List of vehicles
vehicles = ['car', 'motorcycle', 'bicycle', 'boat', 'airplane']

# List of computer scientists
computer_scientists = ['Ada Lovelace', 'Alan Turing', 'Grace Hopper', 'Tim Berners-Lee', 'Steve Jobs']

# List of viruses
viruses = ['influenza', 'Ebola', 'HIV', 'COVID-19', 'Zika']

# List of weekdays
weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

# List of metals
metals = ['gold', 'silver', 'iron', 'copper', 'aluminum']

# List of electronics_components
electronics_components = ['Resistor', 'Capacitor', 'Diode', 'Transistor', 'Inductor']

lol = [animals, household_objects, computer_scientists, viruses, weekdays, metals, electronics_components]

def random_items(n, lst):
    # Check if the list has at least 3 items
    if len(lst) < n:
        print("List should have at least N items")
        return

    # Choose 3 random items from the list
    random_items = random.sample(lst, n)

    # Print the 3 random items
    return random_items

def shuffle(l):
    random.shuffle(l)
    return l

def generate_entry(ls):
    # run1
    n = 3
    # run 2
    n = random.randint(2, 5)
    ls = [random_items(n, l) for l in ls]
    everything = shuffle(sum(ls, [])) # https://stackoverflow.com/a/716489 ty
    print("")
    print("input: %s" % (', '.join(everything)))
    print("output: %s" % (', '.join([repr(shuffle(l)) for l in ls])))

def run_1():
    generate_entry([animals, household_objects])
    generate_entry([animals, household_objects])
    generate_entry([animals, vehicles])
    generate_entry([animals, vehicles])
    generate_entry([animals, viruses])
    generate_entry([animals, viruses])
    generate_entry([household_objects, vehicles])
    generate_entry([household_objects, computer_scientists])
    generate_entry([household_objects, vehicles, viruses])
    generate_entry([household_objects, vehicles, viruses])
    generate_entry([animals, household_objects, vehicles, computer_scientists])
    generate_entry([animals, household_objects, vehicles, viruses])
    generate_entry([weekdays, metals, electronics_components])


def run_2():
    generate_entry(random_items(random.randint(2, len(lol)), lol))

for _ in range(5):
    run_2()
