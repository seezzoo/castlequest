import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='castlequest',
    user='postgres',
    password='swordfish')

print("=== Welcome to the Trading Post ===")

cur = con.cursor()

val = False
while val == False:
    playerName = input("What's your name? ")
    
    with con.cursor() as curs:
        curs.execute("SELECT first_name FROM public.players WHERE LOWER(first_name) = %s", (playerName.lower(),))
        for record in curs:
            val = True

    if val:
        print (f'Welcome back, {playerName}! ')
    else: 
        print ("Who's Dat?")
                  

itemToSell = input("What would you like to sell? ")

#Do they have one to sell?

#What is the price?

#Give them the gold

#Take it out of their inventory