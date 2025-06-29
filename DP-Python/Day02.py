# Using lstrip() Removing the all unwanted elements from left side

# name = "......Rajendra---"
# # newName = name.lstrip()
# newName = name.lstrip(".")
# print(name)
# print(newName)


# Using rstrip() Removing the all unwanted elements form right side

# name = "Rajendra       "
# newName = name.rstrip()
# # Output : Rajendra

# name = "Rajendra           ......"
# newName0 = name.strip('.')
# newName = newName0.rstrip()
# print(newName)

# # Output : Rajendra

# strip() Removing unwanted element from the whole string 

# name = "  Rajendra    "
# newName = name.strip()
# print(newName)

# name = "1RA3"

# newName = name.strip("31")

# print(newName)


# Examples : 

name = "    ----My Name is Rajendra 1 2 3 2 4 _____"

newName = name.strip(" -1234_")
print(newName)