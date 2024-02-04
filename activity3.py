# Activity 3: Generate a Single Random Number
import random
def generate_random_number(min_val, max_val):
    return random.randint(min_val, max_val)

min_val = 1
max_val = 100
print (f"here is a random number:{generate_random_number(min_val, max_val)}")
 #write missing code here. Use“randint”
