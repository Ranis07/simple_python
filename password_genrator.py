import random

symbols = "!@#$%^&"
numbers = "123456789"
sm_alpha = "abcdefghijk"
lg_alpha = "ABCDEFGHIJK"

all = symbols+numbers+sm_alpha+lg_alpha
length =17

password = "".join(random.sample(all,length))
print(password)