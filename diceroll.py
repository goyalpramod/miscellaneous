import random
x = ("[-----------]\n[           ]\n[     0     ]\n[           ]\n[-----------]",
     "[-----------]\n[     0     ]\n[           ]\n[     0     ]\n[-----------]",
     "[-----------]\n[     0     ]\n[     0     ]\n[     0     ]\n[-----------]",
     "[-----------]\n[   0   0   ]\n[           ]\n[   0   0   ]\n[-----------]",
     "[-----------]\n[   0   0   ]\n[     0     ]\n[   0   0   ]\n[-----------]",
     "[-----------]\n[  0  0  0  ]\n[           ]\n[  0  0  0  ]\n[-----------]")

n = random.randint(0,5)
print(x[n])
z = input("Enter r to roll again")
while (z == "r"):
     print(x[n])
     z = input("Enter r to roll again")
     n = random.randint(0, 5)


