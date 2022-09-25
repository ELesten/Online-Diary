# Project: Online-Diary
## Description:
Api service for the organization of educational processes.
### To test project:

1. Clone the repository:

   `git clone git@github.com:ELesten/Online-Diary.git`

2. Install the dependencies:

   `pip install -r requirements.txt`

3. Run project and filling the database with test data:

   For Unix-systems:
   
   `make migrate`
   
   `make run`
   
   For Windows or for those who can't get Makefile to run:
    
    `python manage.py migrate`
    
    `python manage.py loaddata fixtures.json`
    
    `python manage.py runserver`
    
4. Navigate to http://127.0.0.1:8000/
