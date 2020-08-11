import json
from difflib import get_close_matches

#Importing our json data and saving it to an object
data = json.load(open("data.json"))

#Function gets posible matches when a user mistypes a word
def get_matches(user_input):
    match_word =  get_close_matches(user_input, data.keys())[0]
    cont_prog(match_word)

#Prompts user to continue program when user enters wrong word
def cont_prog(match_word):
    print (f"Did you mean: '{match_word}' ?")
    user_answer = input("Yes/No: ") 
    if user_answer.lower() == "yes":
        print (data[match_word])
    else:
        return "The word doesn't exist, please check it or update definitions."

#Finds definition of the word given
def find_def(user_input):
    if user_input in data:
        print (data[user_input])
    else:
        get_matches(user_input)

#Gets user input for find_def      
def get_word():
    user_input = input("Enter word: ")
    user_input = user_input.lower()
    return find_def(user_input)

print(())