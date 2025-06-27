# <!-- 10. Exponential Backoff
# Problem: Implement an exponential backoff strategy that doubles the wait time between retries, starting from 1 second, but stops after 5 retries. -->
import time

wait_time = 1

max_tries = 5

attempt = 0

while attempt < max_tries:

    print(f"Attempt {attempt+1} wait time {wait_time}")

    time.sleep(wait_time)

    wait_time *= 2

    attempt += 1
