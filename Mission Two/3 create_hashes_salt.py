import hashlib as h
import time
import string
import random

start = time.time()

f = open("0 password_plain.txt", "r").readlines()
w = open("3B password_hashed_sha256_salt.txt", "a")

def randomChars():
    chars = string.ascii_lowercase
    word = []
    for i in range(4):
        r = random.randint(0, len(chars)-1)
        word.append(chars[r])
    return "".join(word)

randomChars()

for word in f:
    word =  randomChars() + word
    hash_ = h.sha256(word.encode("utf-8")).hexdigest()
    w.write(hash_ + "\n")

w.close()
print("1000 passwords hashed and saved in " + str(time.time() - start) + " seconds")