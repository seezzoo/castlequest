import psycopg2

con = psycopg2.connect(
    host='localhost',
    database='castlequest',
    user='postgres',
    password='swordfish'
)

cur = con.cursor()

cur.execute ('''REFRESH MATERIALIZED VIEW player_leaderboard;''')

cur.execute ('''REFRESH MATERIALIZED VIEW guild_leaderboard;''')


