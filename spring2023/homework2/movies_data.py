
# @file_name:   homework2.py
# @author:      Hashim Rauf
# #datetime:    3/19/2023 6:00 PM
# @description: Homework assignment 2


import sqlite3


def main():
    """makes a connection to movie.db database and gives the user a menu to
    make requests to the movie_cast database"""
    conn = sqlite3.connect("movie.db")
    conn.execute("PRAGMA foreign_keys = 1")
    create_table(conn)
    display_menu(conn)


def create_table(conn):
    """creates a table called movie_cast if it does not already exist"""
    command = "CREATE TABLE IF NOT EXISTS movie_cast(" \
              "movie_id INTEGER NOT NULL, " \
              "actor_first_name TEXT NOT NULL, " \
              "actor_last_name TEXT NOT NULL," \
              "PRIMARY KEY(movie_id, actor_first_name, actor_last_name)," \
              "FOREIGN KEY (movie_id) REFERENCES movies(id)" \
              ");"

    conn.execute(command)


def display_menu(conn):
    """provides a menu for the user to add data, display it, or alter the structure of the table"""
    while True:
        user_choice = get_user_int(prompt="1. Add movie data\n2. Display data\n3. Alter Table Structure\n4. Exit"
                            "\nEnter desired action: ", error_message="Value must be an integer from 1 - 4",
                                   low_range=1, high_range=4)
        if user_choice == 1:
            add_data(conn)
        elif user_choice == 2:
            display_data_interface(conn)
        elif user_choice == 3:
            alter_structure(conn)
        elif user_choice == 4:
            conn.close()
            print("connection to db is closed")
            break


def add_data(conn):
    """allows the user to make entries to the movie_cast table and indicates failed insertions"""
    same_movie = False
    while True:
        if not same_movie:
            movie_name = input("Enter the name of the movie: ").strip()
            movie_id = find_movie_id(conn, movie_name)

        if movie_id == 0:
            print("Movie not in the database")
            continue

        first_name = input("Enter the first name of the actor: ").strip()
        last_name = input("Enter the last name of the actor: ").strip()

        if not execute_add_data(conn, movie_id, first_name, last_name):
            print("That entry is already in the table\n")
            continue

        stop = input("Enter N to stop adding movies or press anything to add another: ").upper()

        if stop == 'N':
            break
        use_same_movie = input("Use the same movie? Y/N: ").upper()
        if use_same_movie == 'Y':
            same_movie = True
        else:
            same_movie = False


def find_movie_id(conn, movie_name: str) -> int:
    """finds the movie ID from the movies table that corresponds to a movie title passed to the function"""
    command = "SELECT id " \
              "FROM movies " \
              "WHERE title = ?"
    cur = conn.execute(command, (movie_name, ))
    answer = cur.fetchall()
    return answer[0][0] if len(answer) > 0 else 0


def get_user_int(prompt: str, error_message: str, low_range: int, high_range: int) -> int:
    """takes a prompt and error message string and returns an integer within the range of the values provided"""
    while True:
        try:
            value = int(input(prompt))
            if not low_range <= value <= high_range:
                raise ValueError
        except ValueError:
            print(error_message)
        else:
            return value


def execute_add_data(conn, movie_id: int, first_name: str, last_name: str) -> bool:
    """takes a sqlite connection object and movie_cast table parameters and returns a boolean value indicating if an
    insertion into the movie_cast table was successful or not"""
    status_check = True
    data_to_insert = (movie_id, first_name, last_name)
    command = "INSERT INTO movie_cast " \
              "VALUES (?, ?, ?)"
    while True:
        try:
            conn.execute(command, data_to_insert)
        except sqlite3.IntegrityError:
            status_check = False
        except sqlite3.OperationalError:
            data_to_insert = (movie_id, first_name, last_name, 'ACTOR')
            command = "INSERT INTO movie_cast VALUES(?, ?, ?, ?)"
            try:
                conn.execute(command, data_to_insert)
            except sqlite3.IntegrityError:
                status_check = False
            else:
                conn.commit()
        else:
            conn.commit()
        return status_check


def display_data_interface(conn):
    """lets the user display data from the table"""
    while True:
        user_choice = get_user_int(prompt="1. Display All Movies\n2. Display count of movies by director name\n"
                            "3. Display the average revenue of all movies\n4. Display list of movies with a "
                            "certain tagline\n5. Display cast for a given movie\n6. Display list of movies "
                            "in descending order of release date\n7. Return to main menu\nEnter desired action: ",
                                   error_message="Value must be an integer from 1 - 7", low_range=1, high_range=7)

        if user_choice == 7:
            break

        print_data(conn, user_choice)


def print_data(conn, user_choice: int):
    """Takes an integer corresponding to a choice from the display_data_interface function and selects the proper
    SQL query from the dictionary in the function. User input is also requested when necessary"""
    sql_commands = {
        1: "SELECT * FROM movies;",
        2: "SELECT directors.name, count(*) "
             "FROM movies "
             "JOIN directors "
             "ON movies.director_id = directors.id "
             "GROUP BY directors.name "
             "HAVING count(*) > 1;",
        3: "SELECT avg(revenue) FROM movies;",
        4: "SELECT title FROM movies WHERE tagline LIKE ?;",
        5: "SELECT actor_first_name, actor_last_name "
           "FROM movie_cast "
           "JOIN movies "
           "ON movie_cast.movie_id = movies.id "
           "AND title = ?;",
        6: "SELECT title, release_date FROM movies "
           "ORDER BY release_date DESC;",
    }
    if user_choice == 4:
        tagline_search = input("Enter a tagline to search for: ").strip()
        tagline_search += '%'
        command = sql_commands.get(user_choice)
        result = conn.execute(command, (tagline_search, ))
    elif user_choice == 5:
        movie_title = input("Enter movie title to find the cast: ")
        command = sql_commands.get(user_choice)
        result = conn.execute(command, (movie_title, ))
    else:
        command = sql_commands.get(user_choice)
        result = conn.execute(command)

    for row in result:
        print(row)


def alter_structure(conn):
    """alters table structure to add the role column and updates all rows to have 'ACTOR' in their role column"""
    try:
        command = "ALTER TABLE movie_cast " \
                  "ADD COLUMN role TEXT NULL"
        conn.execute(command)
        print("Added column 'role' to table")
    except sqlite3.OperationalError:
        pass

    command = "UPDATE movie_cast SET role='ACTOR'"
    conn.execute(command)
    conn.commit()
    print("Updated all values in the role column to 'ACTOR'")


main()
