import pyttsx3
import sqlite3
import time, sys, random, json

conn = sqlite3.connect('main.db')
c = conn.cursor()

engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[2].id)

with open('phrases.json', encoding='utf-8') as phrases_file:
    phrases = json.load(phrases_file)
    
with open('names.json', encoding='utf-8') as names_file:
    names = json.load(names_file)
    
with open('gages.json', encoding='utf-8') as gages_file:
    gages = json.load(gages_file)
    
    
# Mutex functions

def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS main (open TEXT PRIMARY KEY);")
    c.execute("INSERT INTO main (open) VALUES ('1');")
    conn.commit()

def read_bool():
    c.execute('SELECT * FROM main;')
    res = c.fetchall()

    return res[0][0]

def update_bool(bool_):
    c.execute('UPDATE main SET open = {} WHERE open = {};'.format(int(bool_), int(not bool_)))
    conn.commit()
    

def introduce(name):

    value = phrases.get(name, None)

    if value:
        i = random.randrange(len(value))
        to_say = value[i]
    else:
        to_say = 'Je ne sais pas qui vous êtes'
 
    engine.say(to_say)
    engine.runAndWait()

    time.sleep(5)
    
    update_bool(True)



def get_gage(name):
    
    name_values = names.get(name, None)
    name_to_say = ''
    
    value = phrases.get(name, None)

    if value:
        i = random.randrange(len(value))
        name_to_say = value[i]
    else:
        name_to_say = 'Je ne sais pas qui vous êtes'   
    
    engine.say(name_to_say)
    engine.runAndWait()
    time.sleep(0.7)
    
    engine.say("Voici votre gage: ")
    engine.runAndWait()    
    time.sleep(0.7)
    
    j = random.randrange(len(gages))
    gage_value = gages[j]
    
    engine.say(gage_value)
    engine.runAndWait()    
    time.sleep(5)
    
    update_bool(True)  
    


if __name__ == '__main__':
    introduce(sys.argv[1])
    #get_gage(sys.argv[1])
