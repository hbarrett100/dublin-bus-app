# Research Project
### Research practicum for UCD MSc Comp-Sci Conversion 2020/21
>A web based application for generating and serving journey-time predictions for Dublin Bus
>Django, Python 3.7, JavaScript, jQuery

## Installation
### Create a project Directory
- Create a directory to house this project
```
$ mkdir my_project_dir
```
### Get the Project Files
- Browse to your new project directory and clone this repository to your local machine using git
```
$ cd my_project_dir
$ git clone https://csgitlab.ucd.ie/work-in-progress/research-project.git
```
### Create a Virtual Environment and Set up Dependencies
- Create a python virtual environment in the project directory using virtualenv, venv, etc...
- The version of python used should be python 3.7
```
~/my_project_dir$ python3.7 -m venv my_project_env
```
- Activate the virtual environment using
```
~/my_project_dir$ source my_project_env/bin/activate
```
- Install dependencies from the requirements.txt file
```
~/my_project_dir$ pip install -r /research_project/web_app/requirements.txt
```
### Create a .env file with login information
```
/my_project_dir/research_project/web_app$ vim .env
```
```
database="<database_name>"
user="<database_username>"
password="<database_password>"
host="<database_host>"
port="<database_communication_port>"
traffic_key="<api_key_for_traffic_alerts>"
weather_key="<api_key_for_weather_data>"
```
### Run Locally for Development
- To host the web app on a local machine for development
```
~/my_project_dir/research_project$ python web_app/manage.py runserver
```
- Weather & Traffic scrappers are run separately from the main web app and can be called using

### Deploy to Production
#### Configure Gunicorn Application Server

#### Install & Configure Nginx


## Features
- Journey Planner
- Prediction Models


## Team