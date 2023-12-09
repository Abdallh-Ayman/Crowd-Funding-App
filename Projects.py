import json
import datetime
from termcolor import colored


def validate_date(date_text):
    try:
        datetime.datetime.strptime(date_text, '%Y-%m-%d')
        return True
    except ValueError:
        return False

def save_project(projects_data):
    try:
        with open("projects.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    
    if isinstance(projects_data, list):
        with open("projects.json", "w") as file:
            json.dump(projects_data, file, indent=4)
    elif isinstance(projects_data, dict):
        data.append(projects_data)
        with open("projects.json", "w") as file:
            json.dump(data, file, indent=4)
    else:
        raise ValueError(colored("Invalid input. Expected a list or a dictionary.","red"))


def create_project(user_id):
    project_data = {}
    project_data['user_id'] = user_id
    project_data['project_id'] = len(get_all_projects()) + 1
    project_data['title'] = input("Enter the project title: ")
    project_data['details'] = input("Enter the project details: ")
    project_data['total_target'] = input("Enter the total target: ")
    while not project_data['total_target'].isdigit():
        project_data['total_target'] = input(colored("Invalid total target format. Enter the total target again: ","red"))
    project_data['total_target'] = int(project_data['total_target'])
    start_date = input("Enter the start date in YYYY-MM-DD format: ")
    while not validate_date(start_date):
        start_date = input(colored("Invalid date format. Enter the start date again: ","red"))
    project_data['start_date'] = start_date
    end_date = input("Enter the end date in YYYY-MM-DD format: ")
    while not validate_date(end_date):
        end_date = input(colored("Invalid date format. Enter the end date again: ","red"))
    project_data['end_date'] = end_date
    save_project(project_data)
    print(colored("Project created successfully!","blue"))



def get_all_projects():
    try:
        with open("projects.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        data = []
    return data

def search_projects_by_date(date):
    projects = get_all_projects()
    matching_projects = [project for project in projects if project['start_date'] == date or project['end_date'] == date]
    return matching_projects

def edit_project(user_id, project_id):
    projects = get_all_projects()
    for project in projects:
        if project['user_id'] == user_id and project['project_id'] == project_id:
            project['title'] = input("Enter the new project title: ")
            project['details'] = input("Enter the new project details: ")
            project['total_target'] = input("Enter the new total target: ")
            while not project['total_target'].isdigit():
                project['total_target'] = input(colored("Invalid total target format. Enter the total target again: ","red"))
            project['total_target'] = int(project['total_target'])
            start_date = input("Enter the new start date in YYYY-MM-DD format: ")
            while not validate_date(start_date):
                start_date = input("Invalid date format. Enter the start date again: ")
            project['start_date'] = start_date
            end_date = input("Enter the new end date in YYYY-MM-DD format: ")
            while not validate_date(end_date):
                end_date = input("Invalid date format. Enter the end date again: ")
            project['end_date'] = end_date
            print("Project edited successfully!")
            save_project(projects)
            return
   
    print(colored("this isn't your project,you can edit only your projects","red"))

def delete_project(user_id, project_id):
    projects = get_all_projects()
    for project in projects:
        if project['user_id'] == user_id and project['project_id'] == project_id:
            projects.remove(project)
            with open("projects.json", "w") as file:
                json.dump(projects, file, indent=4)
            print(colored("Project deleted successfully!","blue"))
            return
    print(colored("this isn't your project,you can delete only your projects","red"))