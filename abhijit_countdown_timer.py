#program for countdown timer
import time

countdown_time = int(input("Enter the time in seconds: "))

for i in range(1, countdown_time+1):
    seconds = i % 60
    minutes = int(i / 60) % 60
    hours = int(i / 3600)

    print("\r", f"{minutes:02}:{seconds:02}", end="")
    time.sleep(1)

print("\nTime's Up!")