import sqlite3

connection = sqlite3.connect('Project 2')

cursor = connection.cursor()

def create_table():
    cursor.execute('CREATE TABLE IF NOT EXISTS FiveMoviesTable (movieid REAL, title TEXT, year TEXT, minutes REAL, boxoffice REAL)')



def data_entry():
    cursor.execute('INSERT INTO FiveMoviesTable VALUES(1, "Endgame", 2019, 181, 2797800564)')
    cursor.execute('INSERT INTO FiveMoviesTable VALUES(2, "Infintity War", 2018, 149, 2048359754)')
    cursor.execute('INSERT INTO FiveMoviesTable VALUES(3, "Joker", 2019, 122, 1072651773)')
    cursor.execute('INSERT INTO FiveMoviesTable VALUES(4, "Frozen", 2013, 102, 1290000000)')
    cursor.execute('INSERT INTO FiveMoviesTable VALUES(5, "Toy Story 3", 2010, 103, 1066969703)')

def create_table2():
    cursor.execute('CREATE TABLE IF NOT EXISTS FiveMoviesActors (firstname TEXT, lastname TEXT, age REAL, movieid REAL)')

def data_entry2():
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Robert", "Downey", 56, 1)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Chris", "Evans", 40, 1)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Mark", "Ruffalo", 54, 2)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Chris", "Hemsworth", 38, 2)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Robert", "De Niro", 76, 3)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Joaquin", "Phoenix", 47, 3)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Idina", "Menzel", 50, 4)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Kristen", "Bell", 41, 4)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Tom", "Hanks", 65, 5)')
    cursor.execute('INSERT INTO FiveMoviesActors VALUES("Tim", "Allen", 68, 5)')

def read_from_database():
    cursor.execute('SELECT * FROM FiveMoviesTable WHERE length < 103')
    
    data = cursor.fetchall()
    print("1. ", end = "")
    print(data)
    
    cursor.execute('SELECT * FROM FiveMoviesTable WHERE year >= 2016')
    
    data = cursor.fetchall()
    print("2. ", end = "")
    print(data)
    
    cursor.execute('SELECT * FROM FiveMoviesActors WHERE age > 40')

    data = cursor.fetchall()
    print("3. ", end = "")
    print(data)
    
    cursor.execute('select actors.firstname, movies.title from fivemoviestable movies inner join fivemoviesactors actors on movies.movieid = actors.movieid where movies.year > 2018')

    data = cursor.fetchall()
    print("4. ", end = "")
    print(data)
    

connection.commit()

create_table()
data_entry()
create_table2()
data_entry2()
read_from_database()




