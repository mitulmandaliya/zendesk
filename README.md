
# Zendesk Integration
This project uses python for backend and React for frontend

## Backend
Change directory to backend
### `cd backend/`
Change zendesk credentials in ```backend/app/database.py```

Create a virtual environment and activate
### `python3 -m venv venv`
### `source venv/bin/activate`

Install python requirements
### `pip install -r requirements.txt`

Export flask app and run
### `export FLASK_APP=run.py`
### `flask run`

API documentation can be accessed at
### `http://127.0.0.1:5000/zd/api/apidocs#`


## Frontend
To run react app move to zendesk directory and run following commands
### `npm install`
### `npm start`
