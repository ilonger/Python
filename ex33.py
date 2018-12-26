i = 0
numbers = []
maxium = int(input("please input a number!\n"))
step = int(input("please input a number!\n"))

while i < maxium:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1
    print("Numbers now: ", numbers)
    print("At the bottom i is %d" % i)

print("The numbers:")

for num in numbers:
    print(num)


