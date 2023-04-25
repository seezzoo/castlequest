import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT

superuser = 'postgres'
superpass = 'goober'

con = None

def main():
    print("Creating Database:")
    connectAsSuperuser()
    deleteDatabase()
    createRoles()
    createDatabase()

    print("Creating Schema:")
    connectAsAdmin()
    print("\tRunning schema.sql...")
    con.cursor().execute(open("database/schema.sql", "r").read())
    listTables()

    print("\tRunning testData.sql...")
    con.cursor().execute(open("database/testData.sql", "r").read())

def listTables():
    print("\tCreated Tables:")
    with con.cursor() as curs:
        curs.execute('''
        SELECT table_name 
            FROM information_schema.tables 
            WHERE table_schema = 'public'
        ''')
        for record in curs:
            print(f"\t\t{record[0]}")

def connectAsAdmin():
    print("\tConnecting as castlequest_admin")
    global con
    con = psycopg2.connect(
        host='localhost',
        database='castlequest',
        user='castlequest_admin',
        password='Woodruff1787')
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

def connectAsSuperuser():
    print("\tConnecting as superuser")
    global con
    con = psycopg2.connect(
        host='localhost',
        database='postgres',
        user=superuser,
        password=superpass)
    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)

def deleteDatabase():
    print("\tDropping old database...")
    con.cursor().execute('DROP DATABASE IF EXISTS castlequest')
    con.cursor().execute('DROP ROLE IF EXISTS castlequest_admin')
    con.cursor().execute('DROP ROLE IF EXISTS castlequest')

def createRoles():
    print("\tCreating roles...")
    print("\t\tCreating castlequest_admin")
    con.cursor().execute('''
        CREATE ROLE castlequest_admin WITH
        LOGIN
        NOSUPERUSER
        INHERIT
        NOCREATEDB
        CREATEROLE
        NOREPLICATION
        PASSWORD 'Woodruff1787'
    ''')

def createDatabase():
    print("\tCreating castlequest database...")
    con.cursor().execute('''
        CREATE DATABASE castlequest
        WITH
        OWNER = castlequest_admin
        ENCODING = 'UTF8'
        CONNECTION LIMIT = -1
        IS_TEMPLATE = False;
    ''')

main()
