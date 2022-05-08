import random

def win_prob(prob):
    a = random.uniform(0, 1)

    if prob > a:
        return True
    else:
        return False

