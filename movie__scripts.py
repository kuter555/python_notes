import keyboard
import time

things = []
beemovie = []
movie = input("What movie do you want to experience? ")
minecraft = input("Are you on minecraft? ")
if minecraft == "yes":
      minecraft = True
movie = movie + ".txt"
if movie == "Room.txt":
      f = open(movie, "r", encoding="utf8")
else:
      f = open(movie, "r", encoding="utf8")
emptystring = ""
for letter in f.read():
      try:
            ord(letter)
            if ord(letter) >= 65 and ord(letter) <= 90 or ord(letter) >= 97 and ord(letter) <= 122 or ord(letter) == 39 or letter == "j" or letter == "C":
                  emptystring += letter
            else:
                  things.append(emptystring)
                  emptystring = ""
      except:
            pass
f.close()

input("Press anything to begin the movie experience... ")
print("5")
time.sleep(1)
print("4")
time.sleep(1)
print("3")
time.sleep(1)
print("2")
time.sleep(1)
print("1")
time.sleep(1)
for item in things:
      for letter in item:
            keyboard.press(letter)
            keyboard.release(letter)
            time.sleep(0.05)
      time.sleep(0.2)
      keyboard.press("Enter")
      keyboard.press(",")
      time.sleep(0.1)
      if minecraft == True:
            keyboard.press("t")
            time.sleep(3.2)
            
