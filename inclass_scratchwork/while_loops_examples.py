"""
some_number = int(input("Gimme a number to start with: "))

while 2 < some_number < 100:
    print(some_number)
    # some_number = some_number + 1
    some_number += 1
"""

some_other_number = input("What number would you like to square? ")
times_asked = 1

while not some_other_number.isdigit() and times_asked < 3:
    some_other_number = input("Dude, that was whack. I said a number, please: ")
    times_asked += 1

actually_a_number = int(some_other_number)
print(actually_a_number ** 2)

while True:
    print("hello hello hello", end=" ")