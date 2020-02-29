# To host the app locally:

### change to source code directory
cd src/

### download all required libraries
pip3 install -r requirements.txt

### host server locally
python3 manage.py runserver

### NOTE: You might not be able to host the app locally because the Lib folder is not present.
### We removed Lib folder in order to keep the size within Markus upload maximum.


# To access the app deployed by GCP:
Go to: https://bball-analytics.appspot.com/

# Information regarding Milestone 01:

### Files related to Database Design Schema can be found under /Report directory

### You can find the schema definition of all the tables under /sql/tables 
### You can find test-sample.sql and test-sample.output under /sql

### Within our application, see /src/teams/models.py:
### 1. For code that creates our tables
### 2. For code that uses pandas to scrape real data from csv files to populate the tables "TeamsInfo" and "TeamStats"

### We used Django to implement a simple Database-Driven Application:
### 1. That displays all unique basketball teams that have played since the 1930's
### 2. That takes year as a user input and displays all basketball teams that played in that particular year. User Input comes through a drop-down menu of years

### Relevant source code can be found under /src/teams directory

### Do the following to run the app locally:
### 1. Go to /src and type ./cloud_sql_proxy -instances=bball-analytics:us-central1:bball-analytics-db=tcp:5432
### 2. In a new terminal, type python manage.py runserver

