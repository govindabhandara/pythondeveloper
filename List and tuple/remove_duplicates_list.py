original = [1, 2, 2, 3, 1, 4]
unique = []

for item in original:
    if item not in unique:
        unique.append(item)

print(unique)  # Output: [1, 2, 3, 4]
