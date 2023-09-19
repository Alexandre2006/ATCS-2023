def alpha_slices():
    alpha_ten = "abcdefghij"
    alpha_ten.find
    print("Initial value: " + alpha_ten)
    print("First three letters: " + alpha_ten[0:3])
    print("Middle three letters: " + alpha_ten[4:7])
    print("Middle to end letters: " + alpha_ten[5:10])

def this_to_that(sentence):
    print("New sentence:\n")
    print(sentence.replace("this", "that").replace("This", "That"))

def clean_string(sentence):
    print("Initial value: " + sentence)
    print("New value: " + sentence.strip())

def count_email_domains():
    emails = ["example@thinkalex.dev", "example@gmail.com", "examplealt@gmail.com", "example.example-example@menloschool.org", "example@stanford.edu", "example@icloud.com"]
    print("Emails: " + str(emails))

    domains = {}

    for email in emails:
        domain = email[email.find("@") + 1:len(email)]
        domains[domain] = domains.setdefault(domain, 0) + 1
    print("Domains: " + str(domains))

def pet_names():
    animal_dict = {
        'fred' : 'cat',
        'poppy': 'dog',
        'jerry': 'fish',
        'jessie': 'dog',
        'jimmy': 'fish',
    }
    print("Animal Dictionary: " + str(animal_dict))

    for animal in animal_dict:
        print(animal.title() + " is a " + animal_dict[animal])

def are_anagrams(word1, word2):
    word1 = word1.lower()
    word2 = word2.lower()
    word1_letters = {}
    for i in word1:
        word1_letters[i] = word1_letters.setdefault(i, 0) + 1
    
    word2_letters = {}
    for i in word2:
        word2_letters[i] = word2_letters.setdefault(i, 0) + 1
    
    print("Are anagrams? " + str(word1_letters == word2_letters))

if __name__ == "__main__":
    while True:
        print("""
1. Alpha Slices
2. This to that
3. Clean String
4. Count Email Domains
5. Pet Names
6. Are Anagrams
Q. Quit
""")
        selection = input("Enter a selection: ")
        if selection == "1":
            alpha_slices()
        elif selection == "2":
            sentence = input("Please select an input sentence: ")
            this_to_that(sentence)
        elif selection == "3":
            clean_string("    this string has a lot of spaces preceding and trailing it       ")
        elif selection == "4":
            count_email_domains()
        elif selection == "5":
            pet_names()
        elif selection == "6":
            are_anagrams(input("Word 1: "), input("Word 2: "))
        elif selection.lower() == "q":
            break