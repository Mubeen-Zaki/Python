import time

wait = 1
attempts = 0
max = 5

while attempts < max:
    print("Attempt : ", attempts + 1, "-wait : ", wait, "s")
    time.sleep(wait)
    wait *= 2
    attempts += 1