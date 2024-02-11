# Intro to this Python File
print("Hello, World!")
print("Hour of Code file about Built-in Functions")

# .format()
pi = 3.12159
formatted = format(pi, '.2f')
print(formatted)

# abs()
positive = 10
negative = -2.5

print(abs(positive))

print(abs(negative))

# all()
# Code-1
my_list = [True, "Hello", 25]

print(all(my_list))

my_list = [False, "Hello", 25]

print(all(my_list))

# Lists
my_list = [5, 5, 0, True]

print(all(my_list))

# Sets
my_set = {1, "False", True, 8}
print(all(my_set))

# Dictionaries
my_dict = {0: "zero", 1: "one", 2: "two"}

print(all(my_dict))

# ascii()
print(ascii('Computer Science'))

# bin()
print(bin(25))

# bool()
print(bool('True'))
print(bool('False'))

print(bool(25))

# bytearray()
array_1 = bytearray("Welcome to GitHub!", "utf-8")
array_2 = bytearray("Welcome to GitHub!", "utf-32")

print(array_1)
print(len(array_1))

print(array_2)
print(len(array_2))










