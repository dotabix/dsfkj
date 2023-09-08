import random
import time

characters = 'abcdefghijklmnopqrstuvwxyz'
words = ['zxc', 'dead', 'inside', 'gule', 'pizdos', 'nigga']

def generate_random_sequence(length):
    return ''.join(random.choice(characters) for _ in range(length))

def generate_random_word():
    return random.choice(words)

while True:
    random_word = generate_random_word()  
    print({random_word})
    time.sleep(5)