from time import sleep

second = int(input("Enter Seconds:"))

if second > 0:
    while second>= 0:
        mins, secs = divmod(second, 60) #divmod returns a tuple with is quotient and remainder
        time = "{:02d}:{:02d}".format(mins,secs) #minutes and seconds formatting
        print(time)
        sleep(1)
        second -=1

else:
    print("Seconds must be greater than zero")

