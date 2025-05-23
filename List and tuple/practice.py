# Step 1: Create the zoo list
zoo = [
    ["Leo", "mammal", 5],
    ["Tweety", "bird", 2],
    ["Nemo", "fish", 1]
]
print("Original Zoo:", zoo)

# Step 2: Add a new animal
zoo.append(["Ellie", "mammal", 3])
print("After adding Ellie:", zoo)

# Step 3: Print all mammals
print("Mammals in the zoo:")
for animal in zoo:
    if animal[1] == "mammal":
        print(animal[0])  # Prints Leo and Ellie

# Step 4: Find the oldest animal
oldest_age = 0
oldest_animal = ""
for animal in zoo:
    if animal[2] > oldest_age:
        oldest_age = animal[2]
        oldest_animal = animal[0]
print("Oldest animal:", oldest_animal, "is", oldest_age, "years old")

# Step 5: Sort by age
zoo.sort(key=lambda x: x[2])  # Sort by age (index 2 in each sublist)
print("Zoo sorted by age:", zoo)