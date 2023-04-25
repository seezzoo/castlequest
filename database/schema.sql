--Tell me about each table
CREATE TABLE table_one (
    column1 TEXT PRIMARY KEY NOT NULL,
    column2 INTEGER
);

CREATE TABLE table_two (
    columna TEXT NOT NULL,
    columnb INTEGER,
    --Describe each constraint
    CONSTRAINT my_constraint
        FOREIGN KEY(columna)
        REFERENCES table_one(column1)
);

DROP ROLE IF EXISTS castlequest;

CREATE ROLE castlequest WITH
    LOGIN
    NOSUPERUSER
    INHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION
    PASSWORD 'HudenBurger23';