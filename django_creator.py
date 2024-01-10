import os
import sys
import subprocess
import time
import argparse

parser = argparse.ArgumentParser(description='Create a Django project')
parser.add_argument('project_name', metavar='project_name', type=str, help='The name of the project')
parser.add_argument('project_folder', metavar='project_folder', type=str, help='The name of the folder')
parser.add_argument('project_location', metavar='project_location', type=str, help='The location of the project')
parser.add_argument('full_feature', metavar='full_feature', nargs='?', type=str, help='Quick or full feature')
args = parser.parse_args()

project_name = args.project_name
project_folder = args.project_folder
project_location = args.project_location
full_feature = args.full_feature

def create_project(project_name):
    try:
        os.system('conda deactivate')
    except:
        pass

    location_string = f'{project_location}/{project_folder}'
    os.chdir(project_location)
    print(os.getcwd())
    os.mkdir(project_folder)
    os.chdir(project_folder)
    print(os.getcwd())
    subprocess.run(['python3', '-m', 'venv', f'{project_name}env'])
    os.system(f'cd {location_string}')
    os.system(f'source {project_name}env/bin/activate')
    subprocess.run(['pip3', 'install', 'django'])
    subprocess.run(['django-admin', 'startproject', project_name])
    os.chdir(project_name)
    print(os.getcwd())
    subprocess.run(['python3', 'manage.py', 'startapp', 'main'])
    subprocess.run(['python3', 'manage.py', 'makemigrations'])
    subprocess.run(['python3', 'manage.py', 'migrate'])

    if full_feature:
        if full_feature == 'y':
            create_admin = input('Would you like to create a superuser? (y/n): ')
            if create_admin == 'y':
                subprocess.run(['python3', 'manage.py', 'createsuperuser'])
            else:
                pass
            open_vscode = input('Would you like to open the project in VSCode? (y/n): ')
            if open_vscode == 'y':
                subprocess.run(['code', '.'])
            else:
                pass
            
        else:
            pass
    else:
        pass

create_project(project_name)
