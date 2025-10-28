# Shopping List

items = ["Milk", "Bread", "Eggs", "Butter", "Apples"]
purchased = [False, True, False, False, True]

for i in range(len(items)):
    if not purchased[i]:
        print("You have not purchased:", items[i])
        answer = input("Have you bought it now? (yes/no): ")
        if answer == "yes":
            purchased[i] = True

print("Updated list:")
for i in range(len(items)):
    if purchased[i]:
        print(items[i], "- Purchased")
    else:
        print(items[i], "- Not purchased")
