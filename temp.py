import time
from tqdm import tqdm


# Print locations
Super_admin_print = '''

  _      __    __                     ______       ____                    ___     __      _        ___                __
 | | /| / /__ / /______  __ _  ___   /_  __/__    / __/_ _____  ___ ____  / _ |___/ /_ _  (_)__    / _ \___ ____  ___ / /
 | |/ |/ / -_) / __/ _ \/  ' \/ -_)   / / / _ \  _\ \/ // / _ \/ -_) __/ / __ / _  /  ' \/ / _ \  / ___/ _ `/ _ \/ -_) / 
 |__/|__/\__/_/\__/\___/_/_/_/\__/   /_/  \___/ /___/\_,_/ .__/\__/_/   /_/ |_\_,_/_/_/_/_/_//_/ /_/   \_,_/_//_/\__/_/  
                                                        /_/                                                              
'''
Login_print = """
 __      _____ _    ___ ___  __  __ ___   _____ ___    _    ___   ___ ___ _  _   ___  _   _  _ ___ _    
 \ \    / / __| |  / __/ _ \|  \/  | __| |_   _/ _ \  | |  / _ \ / __|_ _| \| | | _ \/_\ | \| | __| |   
  \ \/\/ /| _|| |_| (_| (_) | |\/| | _|    | || (_) | | |_| (_) | (_ || || .` | |  _/ _ \| .` | _|| |__ 
   \_/\_/ |___|____\___\___/|_|  |_|___|   |_| \___/  |____\___/ \___|___|_|\_| |_|/_/ \_\_|\_|___|____|
                                                                                                        
        
"""
Teacher_print = """
 __          __  _                            _______      _______              _                     _____                 _  
 \ \        / / | |                          |__   __|    |__   __|            | |                   |  __ \               | | 
  \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___      | | ___  __ _  ___| |__   ___ _ __ ___  | |__) |_ _ _ __   ___| | 
   \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \     | |/ _ \/ _` |/ __| '_ \ / _ \ '__/ __| |  ___/ _` | '_ \ / _ \ | 
    \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |    | |  __/ (_| | (__| | | |  __/ |  \__ \ | |  | (_| | | | |  __/ | 
     \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/     |_|\___|\__,_|\___|_| |_|\___|_|  |___/ |_|   \__,_|_| |_|\___|_| 


"""
Student_print ="""
     __          __  _                            _______       _____ _             _            _     _____                 _ 
     \ \        / / | |                          |__   __|     / ____| |           | |          | |   |  __ \               | |
      \ \  /\  / /__| | ___ ___  _ __ ___   ___     | | ___   | (___ | |_ _   _  __| | ___ _ __ | |_  | |__) |_ _ _ __   ___| |
       \ \/  \/ / _ \ |/ __/ _ \| '_ ` _ \ / _ \    | |/ _ \   \___ \| __| | | |/ _` |/ _ \ '_ \| __| |  ___/ _` | '_ \ / _ \ |
        \  /\  /  __/ | (_| (_) | | | | | |  __/    | | (_) |  ____) | |_| |_| | (_| |  __/ | | | |_  | |  | (_| | | | |  __/ |
         \/  \/ \___|_|\___\___/|_| |_| |_|\___|    |_|\___/  |_____/ \__|\__,_|\__,_|\___|_| |_|\__| |_|   \__,_|_| |_|\___|_|



    """
# End
class clr:
    HDR = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    WNG = '\033[93m'
    FAIL = '\033[91m'
    END = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLINK = "\033[9m"
    RED = "\033[31m"
    Default = "\033[39m"
    Black = "\033[30m"
    Red = "\033[31m"
    Green = "\033[32m"
    Yellow = "\033[33m"
    Blue = "\033[34m"
    Magenta = "\033[35m"
    Cyan = "\033[36m"
    LightGray = "\033[37m"
    DarkGray = "\033[90m"
    LightRed = "\033[91m"
    LightGreen = "\033[92m"
    LightYellow = "\033[93m"
    LightBlue = "\033[94m"
    LightMagenta = "\033[95m"
    LightCyan = "\033[96m"
    White = "\033[97m"


homework_id_counter = 1
# Book database
book_database = []
homework_database = {}
# User database

bus_routes = {}

user_database = {
    "Principal": {
        "password": "pr",
        "type": "super_admin"
    },
    "Vice-Principal": {
        "password": "vp",
        "type": "admin"

    },
    "Tech-admin": {
        "password": "tchadmn",
        "type": "super_admin"

    },
    "Co-ordinator": {
        "password": "vp",
        "type": "admin"

    },
    "t": {
        # for checking purposes:
        "password": "t",
        "type": "teacher",
        "subject": "CD",
        "standard": "1",
        "section": "A,B,C,D",
        "teacher_id": "001",
        "Transport": "A1"

    },
    "s": {
        "password": "s",
        "type": "student",
        "admission_no": "001",
        "class": "1",
        "section": "A",
        "Transport": "A1"

    }
}


def add_bus_route():
    print("Add Bus Route:")
    route_name = input("Enter route name: ")
    starting_point = input("Enter starting point: ")
    ending_point = input("Enter ending point: ")
    stops = input("Enter stops along the route (comma-separated): ").split(",")

    route = {
        "starting_point": starting_point,
        "ending_point": ending_point,
        "stops": stops
    }

    bus_routes[route_name] = route
    print("Bus route added successfully.")


# Function to view all bus routes
def view_bus_routes():
    print("Bus Routes List:")
    if not bus_routes:
        print("No bus routes found.")
    else:
        for route_name, route in bus_routes.items():
            print(f"Route Name: {route_name}")
            print(f"Starting Point: {route['starting_point']}")
            print(f"Ending Point: {route['ending_point']}")
            print(f"Stops: {', '.join(route['stops'])}")
            print()


# Function to delete a bus route
def delete_bus_route():
    print("Delete Bus Route:")
    route_name = input("Enter route name to delete: ")

    if route_name in bus_routes:
        del bus_routes[route_name]
        print("Bus route deleted successfully.")
    else:
        print(f"Bus route '{route_name}' not found.")


# Assigned books database
assigned_books_database = {}


# Add book in admin panel
def add_book():
    print("Add Book:")
    book_name = input("Enter book name: ")
    subject = input("Enter subject: ")
    book_type = input("Enter book type (NCERT/GUIDE/REFERENCE BOOKS/MODULE): ")

    # Validate book type
    valid_book_types = ["NCERT", "GUIDE", "REFERENCE BOOKS", "MODULE"]
    if book_type not in valid_book_types:
        print("Invalid book type. Please try again.")
        return

    book = {
        "book_name": book_name,
        "subject": subject,
        "book_type": book_type,
        "status": "Available"
    }

    book_database.append(book)
    print("Book added successfully.")


# Edit user in admin panel
def edit_user(username):
    if username == "admin":
        print("Cannot edit admin user.")
        return

    if username not in user_database:
        print("User not found.")
        return

    user = user_database[username]

    print(f"Edit User: {username}")
    print("1. Edit Password")
    print("2. Edit Type")

    if user["type"] == "teacher":
        print("3. Edit Subject")
        print("4. Edit Sections Taken")
        print("5. Edit Standard")
        print("6. Edit Section")
        print("7. Edit Teacher ID")
    else:
        print("3. Edit Admission No")
        print("4. Edit Class")
        print("5. Edit Section")

    choice = input("Enter your choice (1-7): ")

    if choice == "1":
        password = input("Enter new password: ")
        user["password"] = password
        print("Password updated successfully.")
    elif choice == "2":
        user_type = input("Enter new user type (teacher/student): ")

        if user_type not in ["teacher", "student"]:
            print("Invalid user type. Please try again.")
            return

        user["type"] = user_type
        print("User type updated successfully.")
    elif choice == "3":
        if user["type"] == "teacher":
            subject = input("Enter new subject: ")
            user["subject"] = subject
            print("Subject updated successfully.")
        else:
            admission_no = input("Enter new admission number: ")
            user["admission_no"] = admission_no
            print("Admission number updated successfully.")
    elif choice == "4":
        if user["type"] == "teacher":
            section = input("Enter new sections taken (comma-separated): ").split(",")
            user["section"] = section
            print("Sections taken updated successfully.")
        else:
            class_name = input("Enter new class: ")
            user["class"] = class_name
            print("Class updated successfully.")
    elif choice == "5":
        if user["type"] == "teacher":
            standard = input("Enter new standard: ")
            user["standard"] = standard
            print("Standard updated successfully.")
        else:
            section = input("Enter new section: ")
            user["section"] = section
            print("Section updated successfully.")
    elif choice == "6":
        if user["type"] == "teacher":
            teacher_id = input("Enter new teacher ID: ")
            user["teacher_id"] = teacher_id
            print("Teacher ID updated successfully.")
        else:
            print("Invalid choice.")
            return
    else:
        print("Invalid choice. Please try again.")
        return

    user_database[username] = user


def cls():
    print("\n" * 100)


# Add user in admin panel
def add_user():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print("Add User:")
    username = input("Enter username: ")

    if username in user_database:
        print("Username already exists. Please try again.")
        return

    password = input("Enter password: ")
    user_type = input("Enter user type (teacher/student): ")

    if user_type not in ["teacher", "student"]:
        print("Invalid user type. Please try again.")
        return

    if user_type == "teacher":
        subject = input("Enter subject: ")
        section = input("Enter sections taken (comma-separated): ").split(",")
        standard = input("Enter standard: ")
        teacher_id = input("Enter teacher enrolment ID: ")
        while True:
            bus_route = input("Enter bus route for the teacher (or 'self' for self-transport): ")
            if bus_route.lower() == "self" or bus_route.lower() == "self-transport":
                bus_route = "Self-Transport"
                break
            elif bus_route in bus_routes:
                break
            else:
                print("Invalid bus route. Please enter an existing bus route or 'self' for self-transport.")

        user = {
            "password": password,
            "type": user_type,
            "subject": subject,
            "sections": section,
            "standard": standard,
            "teacher_id": teacher_id,
            "Transport": bus_route

        }
    else:
        admission_no = input("Enter admission number: ")
        class_name = input("Enter class: ")
        section = input("Enter section: ")
        while True:
            bus_route = input("Enter bus route for the teacher (or 'self' for self-transport): ")
            if bus_route.lower() == "self" or bus_route.lower() == "self-transport":
                bus_route = "Self-Transport"
                break
            elif bus_route in bus_routes:
                break
            else:
                print("Invalid bus route. Please enter an existing bus route or 'self' for self-transport.")

        user = {
            "password": password,
            "type": user_type,
            "admission_no": admission_no,
            "class": class_name,
            "section": section,
            "Transport": bus_route
        }

    user_database[username] = user
    print("User added successfully.")


# Assign books in admin panel
def assign_books():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print("Assign Books:")
    book_name = input("Enter book name: ")

    # Check if the book exists in the book database
    book_indices = [i for i, book in enumerate(book_database) if book["book_name"] == book_name]

    if not book_indices:
        print("Book not found.")
        return

    print("Teachers List:")
    teachers = [username for username, user in user_database.items() if user["type"] == "teacher"]
    if not teachers:
        print("No teachers found.")
        return

    print_users(teachers)

    teacher_usernames = input("\nEnter teacher usernames (comma-separated): ").split(",")

    for teacher_username in teacher_usernames:
        teacher_username = teacher_username.strip()

        if teacher_username not in user_database or user_database[teacher_username]["type"] != "teacher":
            print(f"Invalid teacher username '{teacher_username}'. Skipping.")
            continue

        teacher_assigned_books = assigned_books_database.get(teacher_username, [])
        book = book_database[book_indices[0]].copy()  # Copy the book details

        if book not in teacher_assigned_books:
            book["status"] = "Assigned"
            teacher_assigned_books.append(book)

        assigned_books_database[teacher_username] = teacher_assigned_books

    print("Books assigned successfully.")


# Change book status in teacher panel
def change_book_status(username):
    if user_database[username]["type"] != "teacher":
        print("You are not authorized to change book status.")
        return

    print("Change Book Status:")
    book_name = input("Enter book name: ")

    teacher_books = assigned_books_database.get(username, [])
    book_indices = [i for i, book in enumerate(teacher_books) if book["book_name"] == book_name]

    if not book_indices:
        print("Book not found.")
        return

    book = teacher_books[book_indices[0]]
    current_status = book["status"]

    print("Current Status:", current_status)
    if current_status == "Assigned":
        new_status = input("Enter new status (Pick/Drop): ")
        valid_statuses = ["Pick", "Drop"]
        if new_status not in valid_statuses:
            print("Invalid status. Please try again.")
            return
        book["status"] = new_status
        print("Book status updated successfully.")
    else:
        print("Book is not assigned. Cannot change status.")


# Print list of users
def print_users(users):
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print("Username\t\tType")
    for username in users:
        print(username + "\t\t" + user_database[username]["type"])


# Print list of books
def print_books(books):
    print("Index\tBook Name\tSubject\tBook Type\tStatus")
    for i, book in enumerate(books):
        print(f"{i + 1}\t{book['book_name']}\t{book['subject']}\t{book['book_type']}\t{book['status']}")


# Print list of teachers
def teachers_list():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print("Teachers List:")
    teachers = [username for username, user in user_database.items() if user["type"] == "teacher"]
    if not teachers:
        print("No teachers found.")
    else:
        print_users(teachers)


# Print list of students
def students_list():
    print("Students List:")
    students = [username for username, user in user_database.items() if user["type"] == "student"]
    if not students:
        print("No students found.")
    else:
        print_users(students)


def change_book_status():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    book_name = input("Enter book name: ")
    book_status = input("Enter new book status (Available/Assigned/Drop): ")
    valid_statuses = ["Available", "Assigned", "Drop"]
    if book_status not in valid_statuses:
        print("Invalid book status. Please try again.")
    else:
        for book in book_database:
            if book["book_name"] == book_name:
                book["status"] = book_status
                print("Book status updated successfully.")
                break
            else:
                print("Book not found.")


# Admin panel
def admin_panel():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print("\nAdmin Panel:")
    while True:
        print("\n1. Add Book")
        print("2. Assign Books")
        print("3. Add User")
        print("4. Edit User")
        print("5. Print Teachers List")
        print("6. Print Students List")
        print("7. Print Books List")
        print("8. Logout")

        choice = input("Enter your choice (1-8): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            assign_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            username = input("Enter username to edit: ")
            edit_user(username)
        elif choice == "5":
            teachers_list()
        elif choice == "6":
            students_list()
        elif choice == "7":
            books_list()
        elif choice == "8":
            print("Logged out from admin panel.")
            return
        else:
            print("Invalid choice. Please try again.")


# Super Admin panel
def super_admin_panel():
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print(clr.LightCyan + f"{Super_admin_print}" + clr.Green)
    print("-"*120+clr.END)
    while True:
        print("\n1. Add Book")
        print("2. Assign Books")
        print("3. Add User")
        print("4. Edit User")
        print("5. Edit Book Status")
        print("6. Print Teachers List")
        print("7. Print Students List")
        print("8. Print Books List")
        print("9. Delete Teacher")
        print("10. Delete Student")
        print("11. Add Bus Route")
        print("12. View Bus Routes")
        print("13. Delete Bus Route")
        print("14. Logout")

        choice = input("Enter your choice (1-11): ")

        if choice == "1":
            add_book()
        elif choice == "2":
            assign_books()
        elif choice == "3":
            add_user()
        elif choice == "4":
            username = input("Enter username to edit: ")
            edit_user(username)
        elif choice == "5":
            change_book_status()
        elif choice == "6":
            teachers_list()
        elif choice == "7":
            students_list()
        elif choice == "8":
            books_list()
        elif choice == "9":
            delete_teacher()
        elif choice == "10":
            delete_student()
        elif choice == "11":
            add_bus_route()
        elif choice == "12":
            view_bus_routes()
        elif choice == "13":
            delete_bus_route()
        elif choice == "14":
            print("Logged out from Super Admin Panel.")
            return
        else:
            print("Invalid choice. Please try again.")


# Teacher panel
def teacher_panel(username):
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)

    cls()
    print(clr.LightCyan + f"{Teacher_print}" + clr.Green)
    print("-" * 130 + clr.END)
    print(f"\nTeacher Panel - Welcome, {username}!")

    assigned_books = assigned_books_database.get(username, [])
    if not assigned_books:
        print("No books assigned.")
    else:
        print("Assigned Books:")
        print_books(assigned_books)

    while True:
        print("\n1. Change Book Status")
        print("2. Give Homework")
        print("3. Give Special Assignment")
        print("4. Edit Homework")
        print("5. Delete Homework")
        print("6. Logout")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            change_book_status(username)
        elif choice == "2":
            give_homework_class(username)
        elif choice == "3":
            give_homework_student(username)
        elif choice == "4":
            edit_homework(username)
        elif choice == "5":
            delete_homework(username)
        elif choice == "6":
            print("Logged out from teacher panel.")
            return
        else:
            print("Invalid choice. Please try again.")


# Student panel
def student_panel(username):
    print(clr.GREEN)
    for i in tqdm(range(101),
                  desc="Loading…",
                  ascii=False, ncols=75):
        time.sleep(0.01)
    print(clr.LightCyan + f"{Student_print}" + clr.Green)
    print("-" * 130 + clr.END)

    print(f"\nStudent Panel - Welcome, {username}!" + clr.END)

    user = user_database[username]
    user_class = user["class"]
    user_section = user["section"]

    assigned_books = []
    for teacher_username, books in assigned_books_database.items():
        teacher_user = user_database.get(teacher_username, {})
        if teacher_user["type"] == "teacher" and user_class in teacher_user.get("sections_taken", []):
            assigned_books.extend(books)

    if not assigned_books:
        print("No Status of Books assigned by teachers handling your class.")
    else:
        print("Assigned Books:")
        print_books(assigned_books)

    print("\nHomework List:")
    if user_section in homework_database:
        print_homework(homework_database[user_section])

    if username in homework_database:
        print_homework(homework_database[username])

    while True:
        print(clr.GREEN + "\nStudent Menu" + clr.END)
        print("------------")
        choice = input("Logout??(Press 0)")
        if choice == "0":
            print("Logging out")
            break

        # Books list


def books_list():
    print("Books List:")
    if not book_database:
        print("No books found.")
    else:
        print_books(book_database)


# Login panel
def login_panel():
    print("Login Panel:")

    while True:
        print("-"*105)
        print(clr.LightCyan + f"{Login_print }\n" + clr.GREEN)
        print("-"*105)
        print("             Enter exit or 0 to exit" + clr.END)
        username = input("Enter username: ")
        if username == "exit" or username == "0":
            print("Thank you!")
            exit()

        password = input("Enter password: ")

        if username in user_database and user_database[username]["password"] == password:
            user_type = user_database[username]["type"]
            if user_type == "admin":
                admin_panel()
            elif user_type == "super_admin":
                super_admin_panel()
            elif user_type == "teacher":
                teacher_panel(username)
            elif user_type == "student":
                student_panel(username)
            break

        print(clr.FAIL + "Invalid username or password. Please try again." + clr.END)


def delete_teacher():
    print(clr.GREEN + "----------------------------------------------")
    print("\b           Delete Teacher:")
    print("----------------------------------------------\n" + clr.END)
    username = input("Enter username to delete: ")

    if username not in user_database or user_database[username]["type"] != "teacher":
        print("Invalid teacher username. Please try again.")
        return

    del user_database[username]
    del assigned_books_database[username]
    print("Teacher deleted successfully.")


# Delete student in super admin panel
def delete_student():
    print(clr.GREEN + "Delete Student:")
    username = input("Enter username to delete: " + clr.END)

    if username not in user_database or user_database[username]["type"] != "student":
        print("Invalid student username. Please try again.")
        return

    del user_database[username]
    print("Student deleted successfully.")


def give_homework(username):
    print(clr.GREEN + "Give Homework:" + clr.GREEN)
    section = input("Enter section to assign homework to: ")

    # Check if the teacher takes this section
    teacher_sections = user_database[username].get("sections", [])
    if section not in teacher_sections:
        print(f"Invalid section '{section}'. You are not authorized to assign homework to this section.")
        return

    subject = input("Enter subject: ")
    topic = input("Enter homework topic: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")

    homework = {
        "subject": subject,
        "topic": topic,
        "due_date": due_date
    }

    specific_student = input("Enter a specific student username (press Enter to make it visible to all students): ")
    if specific_student and specific_student != "admin":
        if specific_student not in user_database or user_database[specific_student]["type"] != "student":
            print(f"Invalid student username '{specific_student}'. Homework not assigned.")
            return

        if specific_student not in homework_database:
            homework_database[specific_student] = []

        homework_database[specific_student].append(homework)
        print(f"Homework assigned successfully to student '{specific_student}'.")
    else:
        if section not in homework_database:
            homework_database[section] = []

        homework_database[section].append(homework)
        print("Homework assigned successfully.")


# Edit homework in teacher panel
def edit_homework(username):
    print(clr.GREEN + "Edit Homework:" + clr.END)
    section = input("Enter section for which you want to edit homework: ")

    # Check if the teacher takes this section
    teacher_sections = user_database[username].get("sections", [])
    if section not in teacher_sections:
        print(f"Invalid section '{section}'. You are not authorized to edit homework for this section.")
        return

    if section not in homework_database or not homework_database[section]:
        print(f"No homework assigned for section '{section}'.")
        return

    print("Homework List:")
    print_homework(homework_database[section])

    homework_index = int(input("Enter the index of homework to edit: ")) - 1

    if 0 <= homework_index < len(homework_database[section]):
        homework = homework_database[section][homework_index]

        print("Current Homework Details:")
        print(f"Subject: {homework['subject']}")
        print(f"Topic: {homework['topic']}")
        print(f"Due Date: {homework['due_date']}")

        new_subject = input("Enter new subject (press Enter to keep the same): ")
        new_topic = input("Enter new topic (press Enter to keep the same): ")
        new_due_date = input("Enter new due date (DD-MM-YYYY) (press Enter to keep the same): ")

        if new_subject:
            homework['subject'] = new_subject
        if new_topic:
            homework['topic'] = new_topic
        if new_due_date:
            homework['due_date'] = new_due_date

        print("Homework updated successfully.")
    else:
        print(clr.FAIL + "Invalid homework index. Please try again." + clr.END)


# Delete homework in teacher panel
def delete_homework(username):
    print(clr.GREEN + "Delete Homework:" + clr.END)
    section = input("Enter section for which you want to delete homework: ")

    # Check if the teacher takes this section
    teacher_sections = user_database[username].get("sections", [])
    if section not in teacher_sections:
        print(f"Invalid section '{section}'. You are not authorized to delete homework for this section.")
        return

    if section not in homework_database or not homework_database[section]:
        print(f"No homework assigned for section '{section}'.")
        return

    print("Homework List:")
    print_homework(homework_database[section])

    homework_index = int(input("Enter the index of homework to delete: ")) - 1

    if 0 <= homework_index < len(homework_database[section]):
        del homework_database[section][homework_index]
        print("Homework deleted successfully.")
    else:
        print("Invalid homework index. Please try again.")


# Print list of homework
def print_homework(homework_list):
    if not homework_list:
        print("No homework found.")
    else:
        print("Index\tSubject\t\tTopic\t\tDue Date")
        for i, homework in enumerate(homework_list):
            print(f"{i + 1}\t{homework['subject']}\t\t{homework['topic']}\t\t{homework['due_date']}")


def give_homework_class(username):
    global homework_id_counter  # Use the global counter for Homework ID

    print("Give Homework for Entire Class:")
    section = input("Enter section to assign homework to: ")

    # Check if the teacher takes this section
    teacher_sections = user_database[username].get("section", [])
    if section not in teacher_sections:
        print(f"Invalid section '{section}'. You are not authorized to assign homework to this section.")
        return

    subject = input("Enter subject: ")
    topic = input("Enter homework topic: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")

    homework = {
        "homework_id": homework_id_counter,  # Assign unique Homework ID
        "subject": subject,
        "topic": topic,
        "due_date": due_date
    }

    homework_id_counter += 1  # Increment the Homework ID counter

    if section not in homework_database:
        homework_database[section] = []

    homework_database[section].append(homework)
    print("Homework assigned successfully for the entire class.")


def give_homework_student(username):
    global homework_id_counter  # Use the global counter for Homework ID

    print("Give Homework for Specific Student:")
    student_username = input("Enter student's username to assign homework to: ")

    # Check if the student exists in the user database and is a student
    if student_username not in user_database or user_database[student_username]["type"] != "student":
        print(f"Invalid student username '{student_username}'. Please enter a valid student username.")
        return

    subject = input("Enter subject: ")
    topic = input("Enter homework topic: ")
    due_date = input("Enter due date (DD-MM-YYYY): ")

    homework = {
        "homework_id": homework_id_counter,  # Assign unique Homework ID
        "subject": subject,
        "topic": topic,
        "due_date": due_date
    }

    homework_id_counter += 1  # Increment the Homework ID counter

    if student_username not in homework_database:
        homework_database[student_username] = []

    homework_database[student_username].append(homework)
    print(f"Homework assigned successfully for student '{student_username}'.")


# Main program
while True:
    print(clr.GREEN)
    for i in tqdm(range(100),
                  desc="Loading…",
                  ascii=False, ncols=85):
        time.sleep(0.02)

    login_panel()
