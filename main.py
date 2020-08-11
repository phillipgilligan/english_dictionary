import json
from difflib import get_close_matches

data = json.load(open("data.json"))


def get_matches(usrInput):
    match =  get_close_matches(usrInput, data.keys())[0]
    cont_prog(match)
    
def cont_prog(match):
    print (f"Did you mean: '{match}' ?")
    answer = input("Yes/No: ") 
    if answer.lower() == "yes":
        print("Please retype the word.")
        user_input()
    else:
        return "The word doesn't exist, please check it or update definitions."

def find_def(usrInput):
    if usrInput in data:
        return data[usrInput]
    else:
        get_matches(usrInput)
        
def user_input():
    usrInput = input("Enter word: ")
    return find_def(usrInput).lower()

print(user_input())