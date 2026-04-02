# ML_Community-Dental-Clinic
This repository is for collaboration on designing and implementing the health information management system for the Community Dental Clinic. Collaborators are required to create their own branches and push requests regularly. I have created a base  project structure with Python Flask, which will be used to get started.

First, create a virtual environment
python -m venv venv 
venv\Scripts\activate
Inside the virtual environment, install all requirements: “pip install flask flask_sqlalchemy flask_login flask_migrate & pip -m install requirements.txt.”
Run the app to test and install the missing requirements by running “python run.py” inside the virtual environment 
Each feature is isolated with a unique directory inside the app directory, and all the routes are defined in the route directories of those directories.
Equally, all the models are separated by features (with a separate file for each feature model) in the models’ sub-directory of the app directory. 
All the flask extensions live in the extensions.py file
