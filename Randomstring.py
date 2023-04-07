import random
import string

def Randomstring(length):
    letters = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(random.choice(letters) for i in range(length))

random_string = Randomstring(5)
print(random_string)