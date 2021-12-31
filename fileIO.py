file = open("test1", "w")
file.write("white")
file.close()

file = open("test1", "r")
x = file.read()

print(x)

file.close()

file = open("test1", "w")
file.write("pink")
file.close()

file = open("test1", "r")
x = file.read()

print(x)
file.close()

x = ["apple","banana","orange","grape"]

file = open("test1", "w")
x = ["apple","banana","orange","grape"]
for a in x:
    file.write(a + "\n")

file.close()

file = open("test1", "r")
x = file.read()

print(x)
file.close()
