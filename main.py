import json  # using it as database for the system
import random  # using it to get random number


def addBook():  # function to add book to the database system, to add book it asks for three
    print('Welcome to the process of adding book into database system!')
    while True:
        database = open("bookDatabase.json")  # every function has those three lines at the start because
        data = json.load(database)  # everytime it will use updated information from database
        len_data = len(data)

        name = input('Please, enter name of the book: ')
        author = input('Please, enter the author of the book: ')
        year = input('Please, enter the year when book was published: ')

        existence = 0
        for book in range(len_data):
            if name == data[book]["name"]:
                if author == data[book]["author"]:
                    if year == data[book]["year"]:
                        print('')
                        print('This book already exists in database')   # also, we have to check if the book already
                        # exists
                        print('')
                        existence = 1

        if existence == 0:
            data.append({
                "name": name,
                "author": author,
                "year": year
            })
            with open("bookDatabase.json", 'w') as json_file:
                json.dump(data, json_file, indent=4, separators=(',', ': '))

            print('')
            print('The book has been added to the database!')
            print('')

            continue_way = 0
            while True:
                print('Would you like to add another book? ("YES" or "NO")')
                continue_choice = input('Enter your choice here: ')
                continue_choice = continue_choice.upper()

                if continue_choice == 'YES':
                    print('')
                    continue_way = 1
                    break
                elif continue_choice == 'NO':
                    print('')
                    continue_way = 0
                    break
                else:
                    print('')
                    print('!WRONG INPUT!')
                    print('')
                    continue
            if continue_way == 1:
                continue
            elif continue_way == 0:
                break
        else:
            existence = 0
            continue


def updateBook():   # process of updating information about book, it asks for name, author and year of the book
    print("Welcome to the process of updating book's information!")
    while True:
        database = open("bookDatabase.json")
        data = json.load(database)
        len_data = len(data)

        print('Please type full information about the book in format: Name - Author - Year')
        print('Example: A Tale of Two Cities - Charles Dickens - 1859')
        information = input('Type here: ')
        print('')

        information = information.strip()
        spl_information = information.split(' - ')
        matched_info = 0
        book_index = 0

        try:
            for book in range(len_data):
                if data[book]["name"] == spl_information[0]:
                    if data[book]["author"] == spl_information[1]:
                        if data[book]["year"] == spl_information[2]:
                            matched_info = 1
                            book_index = book
        except IndexError:
            matched_info = 0

        if matched_info == 0:
            print('The book has not been found')
            print('')
            continue
        else:
            while True:
                print('What information you like to update?')
                print('1. Name')
                print('2. Author')
                print('3. Year')
                print('4. Exit')
                upd_choice = input('Enter your choice: ')
                print('')

                if upd_choice == '1':
                    while True:
                        new_name = input('Type new name: ')

                        confirmation = input(f'Are you sure you want to change from "{data[book_index]["name"]}" to '
                                             f'"{new_name}" (YES or NO)?: ')
                        print('')
                        confirmation = confirmation.upper()

                        if confirmation == 'YES':
                            print("The book's name has been updated")
                            print('')
                            data[book_index]["name"] = new_name
                            with open("bookDatabase.json", 'w') as json_file:
                                json.dump(data, json_file, indent=4, separators=(',', ': '))

                            break
                        elif confirmation == 'NO':
                            break
                        else:
                            print('!WRONG INPUT!')
                            print('')
                            continue
                elif upd_choice == '2':
                    while True:
                        new_author = input('Type new author: ')

                        confirmation = input(f'Are you sure you want to change from "{data[book_index]["author"]}" to '
                                             f'"{new_author}" (YES or NO)?: ')
                        print('')
                        confirmation = confirmation.upper()

                        if confirmation == 'YES':
                            print("The book's author has been updated")
                            print('')
                            data[book_index]["author"] = new_author
                            with open("bookDatabase.json", 'w') as json_file:
                                json.dump(data, json_file, indent=4, separators=(',', ': '))

                            break
                        elif confirmation == 'NO':
                            break
                        else:
                            print('!WRONG INPUT!')
                            print('')
                            continue
                elif upd_choice == '3':
                    while True:
                        new_year = input('Type new year: ')

                        confirmation = input(f'Are you sure you want to change from "{data[book_index]["year"]}" to '
                                             f'"{new_year}" (YES or NO)?: ')
                        print('')
                        confirmation = confirmation.upper()

                        if confirmation == 'YES':
                            print("The book's year has been updated")
                            print('')
                            data[book_index]["year"] = new_year
                            with open("bookDatabase.json", 'w') as json_file:
                                json.dump(data, json_file, indent=4, separators=(',', ': '))

                            break
                        elif confirmation == 'NO':
                            break
                        else:
                            print('!WRONG INPUT!')
                            print('')
                            continue
                elif upd_choice == '4':
                    break
                else:
                    print('!WRONG INPUT!')
                    print('')
                continue
        break


def listAllBook():  # listing all the books
    database = open("bookDatabase.json")
    data = json.load(database)
    len_data = len(data)

    print("Here's the list of all books in database: ")
    list_counter = 1

    for book in range(len_data):
        print(f'{list_counter}. "{data[book]["name"]}" by {data[book]["author"]}, {data[book]["year"]}')
        list_counter += 1
    print('')


def searchBook():   # searching for book; do not need the full name of the book or author, search by three or more
    # consecutive similar letters
    print("Welcome to the process of finding book!")
    while True:
        database = open("bookDatabase.json")
        data = json.load(database)
        len_data = len(data)

        print('Choose the criteria to find the book: ')
        print('1. by Name')
        print('2. by Author')
        print('3. by Year')
        print('4. Exit')
        find_choice = input('Enter your choice here: ')
        print('')

        if find_choice == '1':
            while True:
                find_name = input('Please, enter the name (min 3 characters): ')
                print('')
                if len(find_name) < 3:
                    print('Minimum 3 characters')
                    print('')
                else:
                    break
            find_name = find_name.upper()
            list_counter = 0
            print("Here's the results: ")
            for book in range(len_data):
                book_name_upper = data[book]["name"].upper()
                if find_name in book_name_upper:
                    list_counter += 1
                    print(f'{list_counter}. "{data[book]["name"]}" by {data[book]["author"]}, {data[book]["year"]}')
            if list_counter == 0:
                print('No results found')
        if find_choice == '2':
            while True:
                find_author = input('Please, enter the author (min 3 characters): ')
                print('')
                if len(find_author) < 3:
                    print('Minimum 3 characters')
                    print('')
                else:
                    break
            find_author = find_author.upper()
            list_counter = 0
            print("Here's the results: ")
            for book in range(len_data):
                book_author_upper = data[book]["author"].upper()
                if find_author in book_author_upper:
                    list_counter += 1
                    print(f'{list_counter}. "{data[book]["name"]}" by {data[book]["author"]}, {data[book]["year"]}')
            if list_counter == 0:
                print('No results found')
        if find_choice == '3':
            find_year = input('Please, enter the year: ')
            print('')
            list_counter = 0
            print("Here's the results: ")
            for book in range(len_data):
                if data[book]["year"] == find_year:
                    list_counter += 1
                    print(f'{list_counter}. "{data[book]["name"]}" by {data[book]["author"]}, {data[book]["year"]}')
            if list_counter == 0:
                print('No results found')
        if find_choice == '4':
            break
        print('')


def removeBook():   # removes book from the database, needs full info about the book to remove it
    print("Welcome to the process of removing book form the database!")
    while True:
        database = open("bookDatabase.json")
        data = json.load(database)
        len_data = len(data)

        print('Please, type the full information about the book in format: Name - Author - Year')
        print('Example: A Tale of Two Cities - Charles Dickens - 1859')
        information = input('Type here: ')
        information = information.strip()
        div_info = information.split(' - ')

        existence = 0
        for book in range(len_data):
            if data[book]["name"] == div_info[0]:
                if data[book]["author"] == div_info[1]:
                    if data[book]["year"] == div_info[2]:
                        existence = 1
                        data.pop(book)
                        with open("bookDatabase.json", 'w') as json_file:
                            json.dump(data, json_file, indent=4, separators=(',', ': '))
                        print('')
                        print("The book has been removed")
                        print('')
                        break
        if existence == 0:
            print('')
            print('The book has not been found')
            print('')
        else:
            existence = 0

        continue_way = 0
        while True:
            print('Would you like to delete another book? ("YES" or "NO")')
            continue_choice = input('Enter your choice here: ')
            continue_choice = continue_choice.upper()
            print('')

            if continue_choice == 'YES':
                continue_way = 1
                break
            elif continue_choice == 'NO':
                continue_way = 0
                break
            else:
                print('!WRONG INPUT!')
                print('')
                continue

        if continue_way == 1:
            continue
        elif continue_way == 0:
            break


def helpMenu():  # simple help function that every system has, add more functionality to the menu
    print('To interact with the menu you need to type numbers between 1-6. Each number has its own function that can'
          ' help you to interact with the Library Management System')
    goback = input('Type anything to go back to the menu ')
    print('')


def randomBook():   # function to give random book from the database, add more functionality to the menu
    database = open("bookDatabase.json")
    data = json.load(database)
    len_data = len(data)

    randomIndex = random.randint(0, len_data - 1)
    print(f'Random book for you: {data[randomIndex]["name"]} by {data[randomIndex]["author"]}, '
          f'{data[randomIndex]["year"]}')
    goback = input('Type anything to go back to the menu ')
    print('')


def main():  # the main menu of the system
    while True:
        print('***********************')
        print('1. Add Book')
        print('2. Update Book')
        print('3. List All Books')
        print('4. Search Book')
        print('5. Remove Book')
        print('6. Exit')
        print('***********************')
        print("Type 'help' to get more information about menu")
        print('')
        print(
            'Try out our new feature - "Randomizer" to get random book from our database that you might want to read!')
        print("Type 'random' to use it")
        print('')
        choice = input('Enter your choice: ')
        print('')

        if choice == '1':
            addBook()
        elif choice == '2':
            updateBook()
        elif choice == '3':
            listAllBook()
        elif choice == '4':
            searchBook()
        elif choice == '5':
            removeBook()
        elif choice == '6':
            exit()
        elif choice == 'help':
            helpMenu()
        elif choice == 'random':
            randomBook()
        else:
            print('!WRONG INPUT!')
            print('')


if __name__ == "__main__":
    main()
