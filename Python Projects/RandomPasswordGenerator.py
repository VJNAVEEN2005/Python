import random

print("Pass Word Generator")
randomchar = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz@!#$&%^"
NoOfPass = int(input("Enter the Number of Pass : "))
LenOfPass = int(input("Enter the Length of Pass : "))

print("The Random Pass Words are ")

for i in range(NoOfPass):
    Pass = ""
    for j in range(LenOfPass):
        Letter = random.choice(randomchar)
        Pass = Pass + Letter
    print(Pass)
