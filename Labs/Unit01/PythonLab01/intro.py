def count_duplicate(lst):
    print(lst)
    found = []
    duplicates = 0
    for i in lst:
        if i not in found:
            found.append(i)
        else:
            duplicates += 1
    return duplicates

def famous_people():
    famous = []
    # Get famous people
    for i in range(0,4):
        famous.append(input("Enter a famous person: "))

    # Original List
    print(famous)
    
    # Remove last element
    famous.pop()
    print(famous)

    # Pop any value that is not the last element (lets do the first one then)
    famous.pop(0)
    print(famous)

    # Remove one item by its value
    famous.remove(famous[0])
    print(famous)

    # Remove last item I want in any way (yay)
    famous = list(filter(lambda x: x != x, famous))
    print(famous)

def working_list():
    careers = ["Graphic Designer", "Software Developer", "Data Analyst", "Fast Food Employee"]
    print(careers)

    # Find index of a carreer
    print("Index of graphic designer: ", careers.index("Graphic Designer"))

    # Show that graphic designer is in the list using in
    print("Graphic Designer in list: ", "Graphic Designer" in careers)

    # Add a carreer to list
    careers.append("Tow Truck Driver")
    print(careers)

    # Add carreer to beggining of list
    careers.insert(0, "Police Officer")
    print(careers)

    # Loop to print all carreers
    for i in careers:
        print(i)

def alpha_slices():
    # Store first ten letters of alphabet in list
    alphabet10 = []
    for i in range(0,10):
        # Gets character from ASCII code
        alphabet10.append(chr(i + 65))
    
    # Use slice to print out first 3 letters
    print(alphabet10[0:3])

    # Print any 3 letters from middle of list
    print(alphabet10[4:7])
    
    # Print letters from middle to end
    print(alphabet10[5:10])

def get_prime():
    # Get number from user
    number = int(input("Please choose a number: "))

    # Get next prime number
    prime = False
    while not prime:
        # increment number, assume it is prime
        number += 1
        prime = True
        # Check if it is divisible by any number (not 1 or itself)
        for i in range(2, number):
            if number % i == 0:
                prime = False
                break
        if prime:
            print(number)
            break
    
def running_sum(lst):
    new_lst = []
    for i in lst:
        if len(new_lst) == 0:
            new_lst.append(i)
        else:
            new_lst.append(i + new_lst[len(new_lst) - 1])
    return new_lst

def add_digits(num):
    sum = 0
    while num > 0:
        sum += (num % 10)
        num = int(num / 10)
        print(num)
    return sum

        
    

if __name__ == "__main__":
    while True:
        print("""
1. Count Duplicates
2. Famous People
3. Working List
4. Alphabet Slices
5. Get Prime
6. Running Sum
7. Add Digits
Q. Quit
""")
        selection = input("Enter a selection: ")

        if selection == "1":
            lst = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
            print(count_duplicate(lst))
        elif selection == "2":
            famous_people()
        elif selection == "3":
            working_list()
        elif selection == "4":
            alpha_slices()
        elif selection == "5":
            get_prime()
        elif selection == "6":
            print(running_sum([4, 5, 1, 7, 12, 9]))
        elif selection == "7":
            print(391839)
            print(add_digits(391839))
        elif selection.lower() == "q":
            break