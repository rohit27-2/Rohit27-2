# Import Json module
import json

# extracting data from Data.json 
data = json.load(open("Python_Projects/data.json"))

def translate(word):
    if word in data:
        return data[word]
    #Title
    elif word.title() in data:
        return data[word.title()]
    #captital letters
    elif data.upper() in data:
        return data[word.upper()]
    
word = input("Enter the word you wannna search : ")
output = translate(word)
if type(output) == list :
    for item in output:
        print(item)
else:
    print(output)

    
