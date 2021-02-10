from users import User

list_users = []
input_error_msg = "Wrong input! \n"
user_not_found_msg = "User not found \n"


def new_user():
    name = input("Full name: ")
    username = input("Username: ")
    e_mail = input("E-mail: ")
    return User(name, username, e_mail)


def find_user():
    print("Enter 1 to search by e-mail, 2 to search by username")
    try:
        search = int(input("Your input: "))
    except ValueError:
        print(input_error_msg)
    else:
        if search == 1:
            search_email = input("Enter e-mail: ")
            for user in list_users:
                if user.e_mail == search_email:
                    return user
        elif search == 2:
            search_username = input("Enter username: ")
            for user in list_users:
                if user.username == search_username:
                    return user
        else:
            print(input_error_msg)


while True:
    print("Enter 1 to print information about user, 2 to add new user, 3 to delete user, 4 to quit")
    try:
        action = int(input("Your input: "))
    except ValueError:
        print(input_error_msg)
    else:
        if action == 1:
            found_user = find_user()
            try:
                print(found_user.info())
            except AttributeError:
                print(user_not_found_msg)
        elif action == 2:
            list_users.append(new_user())
            print("Added user \n")
        elif action == 3:
            delete_user = find_user()
            try:
                list_users.remove(delete_user)
            except ValueError:
                print(user_not_found_msg)
            else:
                print("Removed user \n")
        elif action == 4:
            break
        else:
            print(input_error_msg)
