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
        break
    else: 
        print ("Who's Dat?")


#Do they have one to sell?
while val == False:
    itemToSell = input("What would you like to sell? ")
    
    with con.cursor() as curs:
        curs.execute("SELECT item_name FROM public.inventory WHERE LOWER(item_name) = %s", (itemToSell.lower(),))
        for record in curs:
            val = True

    if val:
        print (f'We found this item in your invenotry, {playerName}! ')
    else: 
        print ("We did not find this item! Maybe try another?")
#What is the price?

#This is where you would write a piece of code to identify what the price is. This would look like taking the item that was listed 
#and compare it to the list that we have which is item_prices. Then print that list out. 

#Give them the gold

# run an update statement to change the value of their current gold to the new value. 

#Take it out of their inventory
#remove the item from inventory