# klypp_with_python
This is a site aims to provide independent hairstylists with a place to connect with potential clients.
I personally have had difficulty making appointments with independent stylists and would like to ease that process for
other people.

Please note that this project is still in progress.

# To set up your environment, run the following commands:
python -m venv env
source env/bin/activate (or env\Scripts\activate on a Windows machine)
python -m pip install -r requirements.txt

Then, run
python klypp_project/manage.py makemigrations
python klypp_project/manage.py migrate
python klypp_project/manage.py runserver
