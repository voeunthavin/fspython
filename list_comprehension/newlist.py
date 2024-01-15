fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

square_list = [n** 2 for n in range(5)]
print(square_list)

# generator expression

square_generator = (n** 2 for n in range(5))
for square in square_generator:
    print(square)