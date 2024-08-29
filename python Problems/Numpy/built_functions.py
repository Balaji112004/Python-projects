import numpy as np;
print(np.char.title("how are you?"))
name="Balaji";
print(np.char.capitalize(name))
print(np.char.lower(name))
print(np.char.upper(name))
print(np.char.split("I am coding"))
print(np.char.splitlines("Hi\nI am Typing"))
print(np.char.strip(['Gopal','Hari','Bhavan','Bharani'],'B'))
print(np.char.join([":","-"],['dmy','ymd']))
print(np.char.replace("He is gopal","gopal","Bharani"))