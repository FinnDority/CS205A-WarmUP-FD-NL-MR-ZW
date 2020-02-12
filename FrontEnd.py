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
    c.execute("CREATE TABLE teams (team_name VARCHAR(32), location VARCHAR(32), stadium VARCHAR(32), capacity INTEGER,"
              "conference VARCHAR(32), region VARCHAR(32), PRIMARY KEY (team_name))")
    
    # read data from the csv file into the table 
    with open('teams.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO teams (team_name, location, stadium, capacity, conference, region) VALUES (?, ?, ?, ?, ?, ?)",
                      (row[0].lower(), row[1].lower(), row[2].lower(), int(row[3].replace(',', '')), row[4].lower(), row[5].lower(),))
    conn.commit()
    

    # do the same steps as above for the other table
    c.execute("CREATE TABLE players (rank INTEGER, player_name VARCHAR(32), position VARCHAR(32), team_name VARCHAR(32), PRIMARY KEY (rank),"
              "FOREIGN KEY (team_name) REFERENCES teams (team_name))")
    
    with open('players.csv', newline='', encoding='utf-8-sig') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO players (rank, player_name, position, team_name) VALUES (?, ?, ?, ?)",
                      (int(row[0]), row[1].lower(), row[2].lower(), row[3].lower(),))
    
    conn.commit() # save the changes
    # close the connection
    conn.close()

# example() is an example of how to access the database
def example():
    # open a connection to the database
    db_file = "football.db"
    conn = sqlite3.connect(db_file)
    c = conn.cursor()
    
    sql_command = "select p.player_name from teams t, players p where t.team_name = p.team_name and t.team_name = 'rams';"
    for row in c.execute(sql_command):
        print(row[0])
    
    #close the connection
    conn.close()

# help() prints information to help the user use the system.     
def help():
    print("User Commands                                                Description")
    print("  help                                                        displays this menu")
    print("  load data                                                   loads data to database")
    print("  quit                                                        quits program")
    print("  <column to display> <column to search> <value searched>     queries database")
    print()
    print("Example of valid query:")
    print('  stadium team_name "Bills"')
    print("      -prints the stadium name of the Bills team")
    print("      -NOTE: double quotation marks are required ")
    print("             around values being searched for")
    print()
    print("Example of valid query:")
    print('  team_name player_name "Aaron Donald"')
    print("      -prints the team that Aaron Donald belongs to")
    print()
    print("Example of valid query:")
    print('  team_name conference "afc" region "east"')
    print("      -prints teams that are in the AFC and located in the east")
    print()
    print("Example of valid query:")
    print('  team_name rank region "east"')
    print("      -prints teams located in the east along with their ranks")
    print()
    print("Valid Column Names:")
    print("  team_name, location, stadium, capacity, conference, division,") 
    print("  rank, player_name, position")
    print()
    print("NOTE: load data must be run before any queries can be executed")
    