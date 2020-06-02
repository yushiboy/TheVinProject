####Clayton Yushi Robbins####

#This program must include the following features:
##Ability to take the vin number from a car and search a database.
##Ability to take the information that is obtained in step one and display and store as a str()
##Bonus:
###Have a search window pop up with videos and documnets pertaining to the car.
###

import bs4
import urllib

def split(vin):
    return [char for char in vin]

##Input the vin and use the split script to make an aray of useable charactors.

print("Thank you for using my software.")
print("Please enter your vin number.")
vin = input("Please enter the VIN: ")
charVIN = []
charVIN = split(vin)
print(split(vin))
print(charVIN)

##The logic aspect of the program

###Takes the first digit and gives the country of origin

###Takes the second digit and gives the manufacturer
###Takes the thrid digit and tells the vehicle type
###The fourth through the eight digit are the vehicle discriptor
###The ninth digit is the "check digit" 
###The tenth is the year
###The eleventh is the assembly plant
###THe twelvth through seventheen is the production number