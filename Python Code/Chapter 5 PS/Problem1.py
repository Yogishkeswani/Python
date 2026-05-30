# Write a program to create a dictionary of Hindi words with values as their English translation. Provide user with an option to look it up! 

words = {
    "madad": "help",
    "bili": "cat",
    "gari": "car",
    "maderchod": "motherfucker"
}

user_word = input("Enter any Hindi word: ")
print(words[user_word])  # Look up USER'S INPUT, not the dictionary itself 