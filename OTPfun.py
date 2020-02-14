from random import *
import string
print("String OTP:")
def randomstring(length=10):
    l=string.ascii_uppercase
    return " ".join(choice(l) for i in range(length))
print(randomstring(5))

print("Digit OTP:")
def randomstring(length=10):
    l=string.digits
    return " ".join(choice(l) for i in range(length))
print(randomstring(5))

print("Sting+Digit OTP:")
def randomstring(length=10):
    l=string.ascii_uppercase+string.digits
    return " ".join(choice(l) for i in range(length))
print(randomstring(5))

print("Sting+Digit+punctuation OTP:")
def randomstring(length=10):
    l=string.ascii_letters+string.digits+string.punctuation
    return " ".join(choice(l) for i in range(length))
print(randomstring(6))
