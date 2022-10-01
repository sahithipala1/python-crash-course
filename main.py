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


