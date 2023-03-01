Run the following commands

`sudo apt update`
`sudo apt install python3 python3-dev python3-venv`

`sudo apt-get install wget`
`wget https://bootstrap.pypa.io/get-pip.py`
`sudo python3 get-pip.py`
`rm get-pip.py`

`cd your-project`
`python3 -m venv RealEstateENV`

`source RealEstateENV/bin/activate`
`pip install -r requirements.txt`

`python manage.py makemigrations`

`python manage.py migrate`

`python manage.py runserver 0.0.0.0:8000`

`python manage.py createsuperuser`
