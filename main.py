import sys
sys.path.append("../")

from libs.foretechx import*

# 'file' class ::

fileName, bytesValue = file.getBytes("C:/Users/acer/Desktop/example-txt.txt")
""" 'example-txt.txt' body:
-+=ENG=+-
First line
Second line
Third line
-+=PL=+-
Pierwsza linia
Druga linia
Trzecia linia """

file.writeBytes("C:/Users/acer/Desktop/folder/" + fileName, bytesValue)
""" 'folder/example-txt.txt' body:
-+=ENG=+-
First line
Second line
Third line
-+=PL=+-
Pierwsza linia
Druga linia
Trzecia linia """

# ::

# 'key' class ::

def outPutFromBind():
	print("'W' key pressed!")

keyB = key.bind("w", outPutFromBind)

while True:
	keyB.isActvie() # Here, this method 'isActive()' check, if the key for this bind has been pressed :D

# ::

# Misc functions ::

sleep(1000) # Makes your Python script sleep for given amount of time (in ms)
char = pause() # Pauses your Python script; returns pressed character (as 'bytes')
cls() # Clears the terminal

string = "abc" # Example variable

outPutFromMatch = match("abc", globals()) # In this case, returns string 'string' (cause 'string' variable's value matches); 'container' (second) argument must be always defined (as a dict)

# ::

# 'cursor' class

cursor.setPos(5, 5) # Will set terminal's cursor on x: 5 and y: 5

# ::

# Colors ::

""" Well, I'll just give a list of them:
black
gray
red
green
yellow
blue
magenta
cyan
white
underline
reverse
def """

# As an example this:

print(colors["red"] + "I am red!") # Will print message 'I am red!' in red

# And this:

print(colors["def"], end = "") # Will print the default color (no underlines, reverses, etc.) in the previous line, so all next things will be printed in the default style/color

# ::