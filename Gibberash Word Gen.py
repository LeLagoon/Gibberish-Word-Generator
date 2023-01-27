import random
num = input("")
if int(num) <= 0:
    print("Write a natural number")
    num = input("")
if int(num) > 0:
    print(chr(random.randrange(65, 90)), end= "")
for i in range(int(num)-1):
    print(chr(random.randrange(97, 121)), end="")