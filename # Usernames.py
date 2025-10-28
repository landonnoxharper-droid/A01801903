# Usernames 

usernames = ["alex", "jordan", "sam", "taylor"]

name = input("Enter a username: ")

while name in usernames:
    print("That username already exists.")
    name = input("Enter another username: ")

usernames.append(name)
print("Username added!")
print("Usernames now:", usernames)
