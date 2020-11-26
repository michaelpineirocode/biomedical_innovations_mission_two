import hashlib as h
import time

start = time.time()

f = open("0 password_plain.txt", "r").readlines()
w = open("1B password_hashed_sha256_nosalt.txt", "a")

for word in f:
    hash_ = h.sha256(word.encode("utf-8")).hexdigest()
    w.write(hash_ + "\n")

w.close()
print("1000 passwords hashed and saved in " + str(time.time() - start) + " seconds")