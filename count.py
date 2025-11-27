import sys

if len(sys.argv) > 1:
    nums = list(map(int, sys.argv[1:]))
    print("User provided list:")
else:
    nums = [1, 2, 3, 4, 5, 6]
    print("No input given — using default list [1, 2, 3, 4, 5, 6]:")

even_count = 0
odd_count = 0

for n in nums:
    if n % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)
