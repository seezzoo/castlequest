import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='castlequest',
    user='castlequest',
    password='HudenBurger23')

print("=== Welcome to the Trading Post ===")
playerName = input("What's your name? ")

#Does the player even exist?

#It would be nice to show them their inventory.
#Maybe include the price for each item

itemToSell = input("What would you like to sell? ")

#Do they have one to sell?

#What is the price?

#Give them the gold

#Take it out of their inventory