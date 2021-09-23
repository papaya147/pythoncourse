sounds = {
    "cat": "meow",
    "dog": ["woof","bark"],
    "cow": "moo",
    "penguin": "meep",
    "fox": "screech",
    "duck": "honk",
    "sheep": "baaaa"
}

sounds["tiger"] = "grrrr" # adding a sound
del sounds["cat"] # deleting a sound

for animal in sounds: # returns keys
    print(animal)

for sound in sounds.values(): # returns values 
    print(sound)
    
for animal in sounds.keys(): # returns keys
    print(animal)
    
for animal, sound in sounds.items(): # returns keys, values
    if isinstance(sound, list):
        print(animal,"goes",sound[0],"and",sound[1])
    else:
        print(animal,"goes",sound)