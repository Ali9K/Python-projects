import random
import string

def create_puzzle(size):
      puzzle = [[random.choice(string.ascii_uppercase) for i in range(size)] for j in range(size)]

      return puzzle


