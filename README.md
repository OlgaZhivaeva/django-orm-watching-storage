# Bank security console

This is an internal repository for employees of the bank "Сияние".
If you got into this repository by accident, then you will not be able to run it,
because you don't have access to the DB, but you can freely use the layout code
or see how database queries are implemented.

Bank security console - this is a website that can be connected to a remote database
with visits and employee pass cards with visits from our bank

### How to install

To connect to your database store the values of env variables in the  `.env` file:
```
 DB_ENGINE='your_DB_ENGINE'
 DATABASE_URL=postgres://USER:PASSWORD@HOST:PORT/NAME
 DEBUG=TRUE
 SECRET_KEY = 'your_SECRET'
 ALLOWED_HOSTS = ['*']
```

Python3 should be already installed. 
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

### Project Goals

The code is written for educational purposes on online-course for web-developers [dvmn.org](https://dvmn.org/).