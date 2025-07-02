import random
import string
length=int(input("Enter the required length of password:"))
lw=string.ascii_lowercase
up=string.ascii_uppercase
num=string.digits
sym=string.punctuation
all=lw+up+num+sym

temp=random.sample(all,length)
password="".join(temp)
print("The password is:",password)