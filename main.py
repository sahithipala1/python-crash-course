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
