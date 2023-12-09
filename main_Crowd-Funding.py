import auth
import Projects
import json
from termcolor import colored
from prettytable import PrettyTable

def display_centered_message(message, color='green'):
    terminal_width = 80  # Adjust this based on your terminal width
    centered_message = message.center(terminal_width)
    print(colored(centered_message, color))


def main():
    display_centered_message("*" * 45, 'blue')
    display_centered_message("Welcome to the Crowd-Funding Console App","blue")
    display_centered_message("*" * 45, 'blue')
    while True:
        print("\n=====================")
        print("Please select an option from 1 to 3:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n")
            display_centered_message("*" * 35, 'green')
            display_centered_message("Welcome to the Registration Page")
            display_centered_message("*" * 35, 'green')
            print("\n")
            auth.register_user()

        elif choice == "2":
            print("\n")
            display_centered_message("*" * 35, 'green')
            display_centered_message("Welcome to the Login Page")
            display_centered_message("*" * 35, 'green')
            print("\n")
            user_id = auth.login_user()
            if user_id:
                while True:
                    print("\n=====================")
                    print("Please select an option from 1 to 6:")
                    print("1. Create a project")
                    print("2. View all projects")
                    print("3. Search for a project by date")
                    print("4. Edit a project")
                    print("5. Delete a project")
                    print("6. Logout")
                    choice = input("Enter your choice: ")

                    if choice == "1":
                        Projects.create_project(user_id)
                    elif choice == "2":
                        user_projects = Projects.get_all_projects()
                        print("\nAll Projects:")
                        projects_table = PrettyTable()
                        # Set the field names as keys of the dictionary
                        projects_table.field_names = user_projects[0].keys()
                        # Add rows to the table
                        for project in user_projects:
                            projects_table.add_row(project.values())
                        # Print the table
                        print(projects_table)
                    elif choice == "3":
                        date = input("Enter the date in YYYY-MM-DD format: ")
                        matching_projects = Projects.search_projects_by_date(date)
                        print("\nMatching Projects:")
                        for project in matching_projects:
                            print(json.dumps(project, indent=4))
                    elif choice == "4":
                        project_id = int(input("Enter the project ID: "))
                        Projects.edit_project(user_id, project_id)
                    elif choice == "5":
                        project_id = int(input("Enter the project ID: "))
                        Projects.delete_project(user_id, project_id)
                    elif choice == "6":
                        break
                    else:
                        print("Invalid choice. Please try again.")
        elif choice == "3":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
