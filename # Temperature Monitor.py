# Temperature Monitor

temperatures = []

for i in range(7):
    t = float(input("Enter temperature for day " + str(i + 1) + ": "))
    temperatures.append(t)

average = sum(temperatures) / len(temperatures)
print("Average temperature:", average)

for i in range(len(temperatures)):
    if temperatures[i] > average:
        print("Day", i + 1, "is above average.")
    elif temperatures[i] < average:
        print("Day", i + 1, "is below average.")
    else:
        print("Day", i + 1, "is equal to the average.")

