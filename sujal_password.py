import string #used this lib for generating ascii letter
import random #used this lib for shuffle function

if __name__ == "__main__":
    s1 = string.ascii_lowercase
    s2 = string.ascii_uppercase
    s3 = string.digits
    s4 = string.punctuation
    password_len = int(input("Enter your password length:"))
    s = []
    s.extend(s1) #extend is function used to completely merge the list as compared to append
    s.extend(s2)
    s.extend(s3)
    s.extend(s4)
    random.shuffle(s)
    print("Your password is:")
    print("".join(s[0:password_len]))


