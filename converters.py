"""
  converts.py
  This is a program to convert MPG to KPL.
  The user is asked to enter a number and then
  the number is converted and the result output
  to the command line.
"""

# Declaring known constants
KPM = 1.609344     # kilometers per mile
GPL = 0.2641720524 # gallons per liter

def mpg2kpl(mpg):
  """
    Converts MPG to KPL via the formula:
    KPL = MPG * KPM * GPL
  """
  return mpg * KPM * GPL

# ask the user to input an MPG value
mpg = input("What is the MPG? ")

# convert the input into a numeric (float) value
mpg = float(mpg)

# output the converted value rounded to 2 digits
print(round(mpg2kpl(mpg), 2), "kpl")
