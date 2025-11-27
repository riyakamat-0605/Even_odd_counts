import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    numbers = [int(x) for x in sys.argv[1:]]
    print("User provided input numbers:")
else:
    script_name = sys.argv[0]
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("No input given – using default list:")

even_count = 0
odd_count = 0

for n in numbers:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Script Name:", script_name)
print("Numbers:", numbers)
print("Count of even numbers:", even_count)
print("Count of odd numbers:", odd_count)
