import sqlite3
con = sqlite3.connect("games.db")
cur = con.cursor()

def main():
    con = sqlite3.connect("games.db")
    cur = con.cursor()
    create_table()
    display_menu()
    con.close()


def display_menu(): # print menu options for user
    while True:
        print("Menu options:\nEnter C to create a new row\nEnter R to retrieve all rows\nEnter U to update a row\n"
              "Enter D to delete a row\nEnter Q to quit the program")
        choice = input("\nEnter your choice: ").lower()
        if choice == 'c': # creates a new row
            insert_row()
        elif choice == 'r': # retrieve all rows
            select_all()
        elif choice == 'u': # update a row
            update_row()
        elif choice == 'd': # delete a row
            delete_row()
        elif choice == 'q': # quits program
            break
        else:
            print("Enter a valid choice")


def create_table(): # creates a games table if not present
    cur.execute("create table if not exists games(name text, release_year integer, price real)")


def insert_row():
    name = input("Enter the name of the game: ").lower()
    release_year = get_user_input_int("Enter the release year: ", "Enter a valid year (int)")
    price = get_user_input_float("Enter the price of the game: ", "Enter a valid price (float)")

    data = (name, release_year, price)
    cur.execute("insert into games values (?, ?, ?)", data)
    con.commit()


def select_all():
    rows = cur.execute("select * from games")
    print("\n")
    for row in rows:
        print(row)


def update_row():
    key = input("Name of the game whose price you want to update: ")
    new_price = get_user_input_float("New price of the game: ", "Enter a valid price for the game")
    sql = "update games set price = ? where name = ?"

    data = (new_price, key)
    cur.execute(sql, data)
    con.commit()


def delete_row():
    key = input("Enter the name to delete: ")
    sql = "delete from games where name = ?"

    test = (key, )
    cur.execute(sql, test)
    con.commit()


def get_user_input_float(prompt, failure_message):

    while True:
        try:
            value = float(input(prompt))

        except ValueError:
            print(failure_message)
        else:
            return value


def get_user_input_int(prompt, failure_message):
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print(failure_message)
        else:
            return value

main()
