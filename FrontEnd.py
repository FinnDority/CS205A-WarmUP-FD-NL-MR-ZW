import csv
import sqlite3

# load() creates the football database with two tables (teams and players).
# If the database already exists, it overwrites the two tables.
def load():

    # open a connection to the database
    db_file = "football.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
   
    # Drop teams and player tables from database (if they exist) so they can be overwritten
    c.execute("drop table if exists teams")
    c.execute("drop table if exists players")
    conn.commit()   #commit changes to database
    
    # create the teams table
    c.execute("CREATE TABLE teams (team VARCHAR(32), location VARCHAR(32), stadium VARCHAR(32), capacity INTEGER,"
              "conference VARCHAR(32), region VARCHAR(32), PRIMARY KEY (team))")
    
    # read data from the csv file into the table 
    with open('teams.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO teams (team, location, stadium, capacity, conference, region) VALUES (?, ?, ?, ?, ?, ?)",
                      (row[0].lower(), row[1].lower(), row[2].lower(), int(row[3].replace(',', '')), row[4].lower(), row[5].lower(),))
    conn.commit()
    

    # do the same steps as above for the other table
    c.execute("CREATE TABLE players (rank INTEGER, player VARCHAR(32), position VARCHAR(32), team VARCHAR(32), PRIMARY KEY (rank),"
              "FOREIGN KEY (team) REFERENCES teams (team))")
    
    with open('players.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO players (rank, player, position, team) VALUES (?, ?, ?, ?)",
                      (int(row[0]), row[1].lower(), row[2].lower(), row[3].lower(),))
    
    conn.commit() # save the changes
    # close the connection
    conn.close()

def example():
    # open a connection to the database
    db_file = "football.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    sql_command = "select p.player from teams t, players p where t.team = p.team and t.team = 'rams';"
    for row in c.execute(sql_command):
        print(row[0])
      
    conn.close()