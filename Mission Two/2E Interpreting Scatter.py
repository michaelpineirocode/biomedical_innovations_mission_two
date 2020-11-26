
times = open("2B time_to_crack_ns", "r").readlines()
passwords = open("0 password_plain.txt", "r").readlines()
second_trail_times = open("2F second_trail_times", "a")

for i in range(len(times)):
    if float(times[i]) >= 3:
        second_trail_times.write(passwords[i][:-1] + " " + "(" + str(i) + ", " + str(times[i][:-1]) + ")" + "\n")

second_trail_times.close()