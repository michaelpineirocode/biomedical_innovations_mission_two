import hashlib as h
import time
from string import ascii_lowercase as letters
import random

veryStart = time.time()

hashes = open("3B password_hashed_sha256_salt.txt", "r").readlines()
plain_passwords = open("0 password_plain.txt", "r").readlines()

def findhash(password, hash_):
    salt = ["a", "a", "a", "a"]
    for a in range(len(letters)):
        salt[0] = letters[a]
        for b in range(len(letters)):
            salt[1] = letters[b]
            for c in range(len(letters)):
                salt[2] = letters[c]
                for d in range(len(letters)):
                    salt[3] = letters[d]
                    test_pass = "".join(salt) + password
                    test_hash = h.sha256(test_pass.encode("utf-8")).hexdigest()
                    if test_hash == hash_[:-1]:
                        return time.time()

for i in hashes:
    start = time.time()
    time_to_crack_salts = open("4B time_to_crack_s", "a")
    for x in plain_passwords:
        try:
            time_to_crack = (findhash(x, i) - start) * 1000
            print(time_to_crack)
            time_to_crack_salts.writelines(str(time_to_crack) + "\n")
            time_to_crack_salts.close()
            break
        except:
            continue


#totalTime = time.time() - veryStart
#print(totalTime)
