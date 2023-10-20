from functools import reduce

def combination_sum(numbers, sum, using=[]):
    if reduce(lambda x, y: x + y, using, 0) == sum:
        print(using)
        return

    for i in numbers:
        unusedNums = numbers.copy()
        unusedNums.remove(i)
        combination_sum(unusedNums, sum, using + [i])

def place_1s(numbers, index=0):
    # Base Case
    if (index >= len(numbers) - 1):
        return
    
    # Print initial input
    if (index == 0):
        print(numbers)
    
    # Recursive Cases (only print if there is change)
    num_enabled = numbers.copy()
    num_enabled.insert(index+1, 1)
    print(num_enabled)
    place_1s(num_enabled, index + 2)

    num_disabled = numbers.copy()
    place_1s(num_disabled, index + 1)

if __name__ == "__main__":
    while True:
        print("""
1. Combination Sum  
2. Place 1s
Q. Quit
""")
        selection = input("Enter a selection: ")

        if selection == "1":
            nums=[2, 3, 4, 5, 6, 7, 8, 9]
            target=9
            print("Numbers: ", nums)
            print("Target: ", target)
            print("Combinations:")
            combination_sum(nums, target)
        elif selection == "2":
            nums=[1, 2, 3]
            print("Numbers: ", nums)
            place_1s(nums)