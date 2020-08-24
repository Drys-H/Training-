import json 
from random import randint 
from datetime import date

# summary
# 1 create a json file
# 2 create a new character
# 3 amend charactere to the json file 
# 4 delete charactere from the json file
# 5 save the json file 


# 1 create a json file
def load_db():
    with open('db2.json','r') as json_file:
        data = json.load(json_file)
        return data
  
# 2 create a new character     
def new_character(first_name, last_name, dob, location, backstory, characteristics):
     return {
        "first_name": first_name,
        "last_name": last_name,
        "dob": dob,
        "location": location,
        "backstory": backstory,
        "characteristics": characteristics,
    }     
    
# 3 amend charactere to the json file 
def add_db(db, character) : 
    db.append(character)
    return db


# save db into json file
def save_db(db) :
    with open('db2.json','w') as outfile:
        json.dump(db, outfile, indent=4)

def print_characters(db) :
    for character in db :
        print(character)


# select characters from London
def select_from_london(characters) : # list of character ---> value---> location ---> list 
    res = []
    for elt in characters:
        if elt.location == 'London':
            res.append(elt)
    return res

# select characters under 18
def select_minors(characters) : #list of character --> value --> dob(dd/mm/yy) --> compare to today's year --> if less then 18 --> list
#date.today().year 
#dd/mm/yyyy
#elt.dob.split('/')
#['dd','mm','yyyy']
#dob = ['dd','mm','yyyy']
#int(dob[2])
#today -int(dob[2]) < 18
#today = date.today().year
    res = []
    for elt in characters : 
       if date.today().year - int(elt.dob.split("/")[2]) < 18 : 
            res.append(elt)
    return res
 

# select characters with an age in the range [min, max]
def select_interval(characters, min, max) : 
    res = []
    for elt in characters : 
       if date.today().year - int(elt.dob.split("/")[2]) > min and date.today().year - int(elt.dob.split("/")[2]) < max : 
            res.append(elt)
    return res


cities = ["London", "Paris", "Roma", "Madrid", "Geneva", "Dublin"]

def main() : 
    

    # creating db
    db = load_db()
    characters = []
    
    # creating caracters
    for i in range(10) : 
        
        # creating character
        character = new_character(f"persos_{i}", f"lastname_{i}", f"{randint(1, 31)}/{randint(1, 12)}/{randint(1900, 2020)}", cities[randint(0, len(cities) - 1)], "...", "...")
            
        # adding character to db
        characters = add_db(characters, character)
        

    # select characters from London
    characters_from_london = select_from_london(characters)
    print_characters(characters_from_london)
    
    # selecting minor characters
    characters_minor = select_minors(characters)
    print_characters(characters_minor)
    
    # selecting minor characters
    min, max = 22, 46
    characters_interval = select_interval(characters, min, max)
    print_characters(characters_interval)

    # save db into json file
    db['characters'] = characters
    
    
    print_characters(characters)
    
    save_db(db)

if __name__ == '__main__':
    main()
    
