# To host the app locally:

### change to source code directory
cd src/

### download all required libraries
pip3 install -r requirements.txt

### host server locally
python3 manage.py runserver


# To access the app deployed by GCP:
Go to: https://bball-analytics.appspot.com/

# Information regarding Milestone 01:

### Report.pdf can found under the /Report directory

### You can find the schema definition of all the tables under /sql/tables 
### You can find test-sample.sql and test-sample.output under /sql

### Within our application, see /src/teams/models.py:
### 1. For code that creates our tables
### 2. For code that uses pandas to scrape real data from csv files to populate the tables "TeamsInfo" and "TeamStats"

### We used Django to implement a simple Database-Driven Application:
### 1. That displays all unique basketball teams that have played since the 1930's
### 2. That takes year as a user input and displays all basketball teams that played in that particular year. User Input comes through a drop-down menu of years

### Source code can be found under /src directory
 
