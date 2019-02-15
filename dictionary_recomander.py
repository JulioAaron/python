import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys()))>0:
        yn = input("Quizo de decir %s? escriba Y para si, o N para no: " % get_close_matches(w, data.keys())[0])
        if yn=='Y' or yn=='y':
            return  data[get_close_matches(w, data.keys())[0]]
        elif yn=='N' or yn=='n':
            return "La palabra no existe, revise, intente nuevamente"
        else:
            return "No se se entiendo su elección Y o N"
    else:
        return "La palabra no existe, revise, intente nuevamente"

word = input("Ingrese una palabra: ")
output=translate(word)

if type(output)==list:
    for item in output:
        print(item)
else:
    print(output)
