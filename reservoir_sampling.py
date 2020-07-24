import random
def peak_a_random(stream = [], k = 0):
    random_number = None
    for i, e in enumerate(stream):
        if i == 0:
            random = e
        elif random.randint(1, i + 1) == 1:
            random_number = e
        return random_number