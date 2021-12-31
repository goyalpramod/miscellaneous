import json
import difflib
data = json.load(open(r"C:\Users\rajag\Desktop\data.json"))

word = input("Enter the word")

def output(w):
    if(w.lower() in data):
        return data[w.lower()]
    elif(w.title() in data):
        return data[w.title()]
    elif(w.upper() in data):
        return data[w.upper()]
    elif(w not in data):
        if(len(difflib.get_close_matches(w, data.keys(), cutoff= 0.7)) > 0):
            return ("did u mean any of these %s"  %difflib.get_close_matches(w, data.keys(), cutoff= 0.7))
        else:
            return("word doesn't exist")

if(type(output(word))) == list:
    for item in output(word):
        print(item)
else:
    print(output(word))