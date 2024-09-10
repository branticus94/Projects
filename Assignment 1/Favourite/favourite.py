# Imports PIL module
from PIL import Image

# Take user input for favourite ice cream flavour printing the output
favourite = input("What is your favourite ice cream flavour?")

print("No way! I love " + favourite + " too!")

# If favourite flavour is chocolate display rick rolls:

if favourite.lower() == 'chocolate':
    image = Image.open('rick_rolls.jpeg')
    image.show()
