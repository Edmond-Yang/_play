import random

userID = ['cse0' + str(i) + '_' + str(random.randint(1000,9999)) for i in range(4) for j in range(5)]

print(userID)
