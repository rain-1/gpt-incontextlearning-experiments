import random

def single_example(mystr):
    print("Q: What is the parity of {}\n".format(' '.join([str(a) for a in mystr])), end='')
    current = 0
    lst = []
    print("A: {} ".format(current), end='')
    for bit in mystr:
        current = (bit + current)%2
        if bit:
            print("flips {} ".format(current), end='')
        else:
            print("stays {} ".format(current), end='')
    print("so the parity is {}\n\n".format(current), end='')

def examples(n, p=1, total=-1):
    bitstrings = []
    for i in range(2**n-1):
        # Convert i to binary and remove the "0b" prefix
        bitstring = bin(i)[2:]
        # Pad the bitstring with leading zeros if necessary
        bitstring = bitstring.zfill(n)
        # Print the bitstring
        bitstrings.append(bitstring)
    
    random.shuffle(bitstrings)
    for bitstring in bitstrings:
        if random.uniform(0, 1) <= p:
            if total == 0:
                break
            total -= 1
            single_example([int(bit) for bit in bitstring])

#single_example([0,1,1,0,1])
examples(1)
examples(2)
examples(3)
examples(5, p=0.1)
examples(6, p=0.1)
examples(7, total=4)
