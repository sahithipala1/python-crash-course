# Alien Colors : Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a
# value of 'green', 'yellow', or 'red'.

# Write an if statement to test whether the alien’s color is green.
# If it is, print a message that the player just earned 5 points.
# Write one version of this program that passes the if test and
# another that fails. (The version that fails will have no output.)


alien_color = ['green', 'yellow', 'red']

if alien_color == 'red':
    print(" you have won! 5 points")

if 'green' in alien_color:
    print(" you have won! 5 points")

if 'red' in alien_color:
    print("you have won! 10 points")

else:
    print("you have won! 5 points")

# 3 rd examples

if 'green' in alien_color:
    print(" you have won! 5 points")

if 'yellow' in alien_color:
    print(" you have won! 10 points")

if 'red' in alien_color:
    print(" you have won! 15 points")

#  Stages of Life: Write an if-elif-else chain that determines a
#  person’s stage of life. Set a value for the variable age, and then:


age = 55

if age < 2:
    print(" you are a baby")

elif age < 4:
    print("you are a toddler")

elif age < 13:
    print("you are a kid")
elif age < 20:
    print("you are a teenager")

elif age < 65:
    print("you are adult")

elif age > 65:
    print("you are older")

alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby', 'phil': 'python',
}
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll.")

alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}
aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# Make an empty list for storing aliens.
# aliens = []
# Make 30 green aliens.
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
    print("...")
# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")


message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")

team = input("Please enter your team name: ")
print(f"\nHello ,{team}")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name? "
name = input(prompt)
print(f"\nHello, {name}!")


# If loop

height = input("How tall are you, in inches? ")
height = int(height)
if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")
    
weight = input("what is your weight ? :")

weight = int(weight)

if weight >= 170:
    print("your are overweight. please plan for diet")
else:
    print("You have a normal weight")


# When you use numerical input to do calculations
# and comparisons, be sure to convert the input value to a numerical representation first.

# Restaurant seating

seat = input("how many people are in dinner group: ")
seat = int(seat)
if seat >= 8:
    print("You have to wait for 20minutes")
else:
    print("your table is ready")
    
