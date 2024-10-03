DICT={'A':'apple','B':'banana','C':'cat','D':'dog','E':'elephant','F':'fan','G':'goat','H':'horse','I': 'ice-cream','J':'jelly','K':'kite','L':'lion','M':'monkey','N':'nest','O':'orange','P':'pig','Q':'queen','R':'rat','S':'snake','T':'tiger','U':'umbrella','V':'van','W':'watch','X':'xylophone','Y':'yak','Z':'zebra'} 

# Prompting the user for the operation they want to perform
option=int(input("Enter a number for the operation. The options are:\n1. Accept a word and find out whether it is present in the dictionary or not\n2. Accept a key for which you want to display its respective word and print it on the screen.\n3. Accept a key for which you want to change its respective value and change and print the dictionary\n4. Find out how many values in the dictionary end with vowel\n5. Find out how many values in the dictionary are of 5 letters\n6. Print all words of keys which are vowels.\n7. Find out the length of the dictionary.\n\n"))

if(option==1):
    # 1. Accept a word and find out whether it is present in the dictionary or not
    word = input("Enter a word to find: ")
    word_list = list(DICT.values())
    if(word in word_list):
        print("Present in the dictionary")
    else:
        print("Not present in the dictionary")

elif(option==2):
    # 2. Accept a key for which you want to display its respective word and print it on the screen
    print("Dictionary contains these keys\n", DICT.keys())
    key = input("Enter the key you want to know its respective word: ")
    print(key, "\nIts respective word is:", DICT.get(key))

elif(option==3):
    # 3. Accept a key for which you want to change its respective value and print the dictionary
    print("Original dictionary: \n", DICT)
    key = input("Enter the key you want to change value for: ")
    new_value = input("Enter the new value: ")
    DICT[key] = new_value
    print("After changing value:\n", DICT)

elif(option==4):
    # 4. Find out how many values in the dictionary end with a vowel
    vowel = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
    count = 0
    word_list = list(DICT.values())
    print("Values ending with a vowel are:")
    for item in word_list:
        if item.endswith(vowel):
            count += 1
            print(item)
    print("Total number of values that end with a vowel are:", count)

elif(option==5):
    # 5. Find out how many values in the dictionary have 5 letters
    count = 0
    word_list = list(DICT.values())
    print("Values with five letters are:")
    for item in word_list:
        if len(item) == 5:
            count += 1
            print(item)
    print("Number of values with 5 letters are:", count)

elif(option==6):
    # 6. Print all words corresponding to vowel keys
    vowel_keys = ('A', 'E', 'I', 'O', 'U')
    print("The words of the vowel letter keys are:")
    for key in DICT:
        if key in vowel_keys:
            print(DICT[key])

elif(option==7):
    # 7. Find out the length of the dictionary
    length = len(DICT)
    print("Length of dictionary is", length)

else:
    print("Invalid choice, please enter a correct choice.")
