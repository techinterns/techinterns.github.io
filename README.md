# techinterns.github.io
a project repository for interns

## Running the Server
To run the server follow these steps:

1. install [Python](https://www.python.org/downloads/) if don't have it. 
2. Open a command prompt/git bash window and run `cntlm -v` if it isn't already running. 
3. Run `py -m pip install --proxy=127.0.0.1:3128 Flask flask-sqlalchemy flask-wtf` to download Flask and dependencies. 
4. `cd` into the *techinterns.guthub.io* folder and enter the following commands in Git Bash
 
    `export FLASK_APP=server.py`    
    `py -m flask run`

## Notes
Flask requires that all the content that it serves (things like html/css files, images, etc) need to be in the *static* folder. 
