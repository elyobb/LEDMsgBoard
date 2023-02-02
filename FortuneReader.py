import random

with open('fortunes.txt', 'r') as f:
    lines = f.readlines()

print(lines[random.randrange(0, len(lines) - 1)])

