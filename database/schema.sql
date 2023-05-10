--Tell me about each table
CREATE TABLE public.characters
(
    character_id integer NOT NULL,
    character_name text,
    experience_points integer,
    hit_points integer,
    PRIMARY KEY (character_id)
);

CREATE TABLE public.guilds
(
	guild_id integer NOT NULL,
	guild_name text,
    PRIMARY KEY (guild_id)
);

CREATE TABLE public.players
(
    player_id integer NOT NULL,
    username text,
    character_id integer,
    guild_id integer,
    first_name text,
    last_name text,
    email_address text,
    player_password text,
    gold_bars integer,
    PRIMARY KEY (player_id)
);

CREATE TABLE public.items
(
	item_name text NOT NULL,
	item_id integer,
    PRIMARY KEY (item_name)
);

CREATE TABLE public.inventory
(
	item_id integer NOT NULL,
	player_id integer NOT NULL,
	quantity integer,
    PRIMARY KEY (item_id, player_id)
);

CREATE TABLE public.item_price
(
	item_id integer NOT NULL,
	item_price integer,
    PRIMARY KEY (item_id)
);

CREATE MATERIALIZED VIEW player_leaderboard AS
SELECT username, character_name, experience_points
FROM public.players
JOIN public.characters ON players.character_id = characters.character_id
ORDER BY experience_points DESC
LIMIT 10;

--CREATE MATERIALIZED VIEW guild_leaderboard AS
--SELECT 

DROP ROLE IF EXISTS castlequest;
CREATE ROLE castlequest WITH
    LOGIN
    NOSUPERUSER
    INHERIT
    NOCREATEDB
    NOCREATEROLE
    NOREPLICATION
    PASSWORD 'HudenBurger23';
GRANT CONNECT ON DATABASE castlequest TO castlequest;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO castlequest;
GRANT SELECT ON players TO castlequest;
GRANT SELECT ON player_leaderboard TO castlequest;
--GRANT SELECT ON guild_leaderboard TO castlequest;

DROP ROLE IF EXISTS castlequest_game;
CREATE ROLE castlequest_game WITH
    LOGIN
    NOSUPERUSER
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD 'gameUser23';
GRANT CONNECT ON DATABASE castlequest TO castlequest_game;
GRANT USAGE ON SCHEMA public to castlequest_game;
GRANT SELECT ON player_leaderboard TO castlequest_game;
--GRANT SELECT ON guild_leaderboard TO castlequest_game;

DROP ROLE IF EXISTS castlequest_login;
CREATE ROLE castlequest_login WITH
    LOGIN
    NOSUPERUSER
    NOCREATEROLE
    NOINHERIT
    NOREPLICATION
    PASSWORD 'gameLogin23';
GRANT CONNECT ON DATABASE castlequest TO castlequest_login;
GRANT USAGE ON SCHEMA public to castlequest_login;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO castlequest_login;
GRANT SELECT ON players TO castlequest_login;
GRANT SELECT ON player_leaderboard TO castlequest_login;
--GRANT SELECT ON guild_leaderboard TO castlequest_login;