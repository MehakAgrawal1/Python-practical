#Q4. Write a Python program to set a random seed and get a random number between 0 and 1.

import random 
print("Set a random seed and get a random number between 0 and 1:")
random.seed(0)
new_random_value = random.random()
print(new_random_value)
random.seed(1)
new_random_value = random.random()
print(new_random_value)
random.seed(2)
new_random_value = random.random()
print(new_random_value)
