message = "Hello World!"
print("message:", message)
print(message.title())
print(message.upper())
print(message.lower())
print(3 + 6)
bicycles = ['trek', 'cannon dale', 'redline', 'specialized']
print(bicycles)
print(bicycles[1])
print(bicycles[3])
print(bicycles[-1])

motorcycles = ['honda', 'yamaha', 'suzuki']
last_owned = motorcycles.pop(1)
print(f"The last motorcycle I owned was a {last_owned.title()}.")

cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)
print("\nHere is the sorted list:")
print(sorted(cars))
print("\nHere is the original list again:")
print(cars)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

y = [1, 2, 3, 4]

for x in y:
    print(y)

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    print("Thank you everyone, that was a great magic show!")

y = [1, 3, 9]
for x in y:
    print(f"{x}, that was a great trick!")


def find_max(nums):
    max_num = float("-inf")  # smaller than all other numbers
    for num in nums:
        if num > max_num:
            max_num = num
    return max_num


print(find_max([1, 2, 3, 5, 8]))

for value in range(1, 5):
    print(value)

squares = []
for value in range(1, 11):
    square = value ** 3
    squares.append(square)
print(squares)

# Slicing and dicing of lists

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
print(players[2:])

print("Here are the first three players on my team:")
for player in players[:3]:
    print(player.title())

# example -2

my_foods = ["pizza", "falafel", "carrot cake"]
friends_foods = my_foods[:]

print("my favourite foods are :")
print(my_foods)

print("\n my friend's favourite foods are :")
print(friends_foods)

print(friends_foods.append("Ice cream"))

print(friends_foods)

# Slices: Using one of the programs you wrote in this chapter, add several lines to the end of the program that do
# the following: Print the message The first three items in the list are:.
# Then use a slice to print the first three items from that program’s list.
# Print the message Three items from the middle of the list are:.
# Use a slice to print three items from the middle of the list.
# Print the message The last three items in the list are:. Use a slice to print the last three items in the list.


places = ["chicago", "put-in-bay", "New York", "stow", "Traverse city", "Columbus", "Ohio", "Cleveland", "Hudson"]

print(places[:3])

print(places[3:6])

print(places[-3:])

# ********* Tuples ***************

dimensions = (200, 50)
print("\nOriginal dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (600, 500)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

#  4-13. Buffet: A buffet-style restaurant offers only five basic foods.
#  Think of five simple foods, and store them in a tuple.
#  Use a for loop to print each food the restaurant offers.
#  Try to modify one of the items, and make sure that Python rejects the change.
#  The restaurant changes its menu, replacing two of the items with different foods.
#  Add a line that rewrites the tuple, and then use a for loop to print each of the items on the revised menu.


buffet = ("Biryani", "Raitha", "Dal", "Rice", "Paneer")
print("\nOriginal Items:")
for items in buffet:
    print(items)

buffet = ("Biryani", "Raitha", "Dal", "curry", "kheer")
print("\nModified Items:")

for items in buffet:
    print(items)

# if loop

cars = ["audi", "bmw", "subaru", "toyota"]

for car in cars:
    if car == "bmw":
        print(car.upper())
    else:
        print(car.title())

requested_topping = 'mushrooms'
if requested_topping != 'anchovies':
    print("Hold the anchovies!")

else:
    print("True")

banned_users = ["camila", "samantha", "queen"]
users = ["marie", "rosy", "lilly"]

if users not in banned_users:
    print(f"{users}, you can post a response.")

# Boolean

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')
print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')
print(car == "BMW")

# Simple if statements:
age = 22
if age >= 21:
    print("ITS your birthday")

age = 12
if age < 4:
    print("Your admission cost is $0.")
elif age < 18:
    print("Your admission cost is $25.")
else:
    print("Your admission cost is $40.")

age = 45
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")
