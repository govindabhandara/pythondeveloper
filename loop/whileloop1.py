#simple example
'''
i=0
while i<5:
    print(i)
    i+=1'
'''
#conditional check : The loop Continues as long as the condition evalutes to True.
#infinite Loops : If the condition  never becomes False, the loop will run morever.
'''
while True: 
    print("This will run forever!")'

while True:
    user_input = input("Enter 'quit' to exit: ")
    if user_input == 'quit':
        break

num = 0
while num < 10:
    num += 1
    if num % 2 == 0:
        continue
    print(num)
'''
# Write a program that counts down from 10 to 1 and then prints "Blast off!"
'''
count=10
while count > 0:
    print(count)
    count-=1
print("Blast off!")
'''
# Ask the user to enter numbers until they enter 0, then print the sum of all entered numbers.
'''
total = 0
num = float(input("Enter a number (0 to stop): "))
while num != 0:
    total += num
    num = float(input("Enter a number (0 to stop): "))
print("The sum is:", total)
'''
# Factorial
'''
n=int(input("enter number:"))
factorial=1
i=1
while i<=n:
    factorial*=i
    i+=1
print(f"factorial of {n} is {factorial}")
'''

