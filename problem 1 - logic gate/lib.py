import random

# months represent True, animals represent False
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
animals = ['Rat', 'Ox', 'Tiger', 'Rabbit', 'Dragon', 'Snake', 'Horse', 'Goat', 'Monkey', 'Rooster', 'Dog', 'Pig']

def random_month():
    return random.choice(months)

def random_animal():
    return random.choice(animals)

bits = [True, False]

def encode_bit(bit):
    if bit:
        return random_month()
    else:
        return random_animal()

def decode_bit(bit):
    if bit in months:
        return True
    if bit in animals:
        return False
    return "N/A"

logic_gate_false = {
        (False, False): False,
        (False, True ): False,
        (True , False): False,
        (True , True ): False,
    }

logic_gate_or = {
        (False, False): False,
        (False, True ): True,
        (True , False): True,
        (True , True ): True,
    }

logic_gate_and = {
        (False, False): False,
        (False, True ): False,
        (True , False): False,
        (True , True ): True,
    }

logic_gate_xor = {
        (False, False): False,
        (False, True ): True,
        (True , False): True,
        (True , True ): False,
    }

logic_gate = logic_gate_xor

def generate_shot(easy=False, with_solution_key=False):
    x0 = random.choice(bits)
    x1 = random.choice(bits)
    y0 = logic_gate[(x0, x1)]
    if easy:
        print("%s and %s gives %s" % (encode_bit(x0), encode_bit(x1), y0))
    else:
        print("%s and %s gives %s" % (encode_bit(x0), encode_bit(x1), encode_bit(y0)))
    if with_solution_key:
        print("### %s and %s gives %s" % (x0, x1, y0))
