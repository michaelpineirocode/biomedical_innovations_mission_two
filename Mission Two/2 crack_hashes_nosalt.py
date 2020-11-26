import hashlib as h
import time

veryStart = time.time()

hashes = open("1B password_hashed_sha256_nosalt.txt", "r").readlines()
plain_passwords = open("0 password_plain.txt", "r").readlines()
cracked_passwords = open("2B time_to_crack_ns", "a")


for i in hashes:
    start = time.time()
    while True:
        for x in plain_passwords:
            hash_ = h.sha256(x.encode("utf-8")).hexdigest()
            if hash_ == i[:-1]:
                end = time.time() - start
                cracked_passwords.write(str(round((end * 1000), 4)) + "\n")
                print("Cracked " + str(plain_passwords.index(x) + 1))
                break
            else:
                continue
        break

cracked_passwords.close()

totalTime = time.time() - veryStart
print(totalTime)