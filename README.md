# User Authentication System

## Overview

This project implements a robust User Authentication System, designed to manage user registrations and logins efficiently and securely. It uses Django framework for backend operations, emphasizing security and ease of use.

### Screenshots of the Application
<a href='https://authentication-system-v1.vercel.app' target='_blank'>
    <img src='./assests/image1.png' alt='Image 1'>
</a>

## How to run application
1. Clone the repository
```
git clone https://github.com/juliusmarkwei/auth-system
```
2. Change current directory to /auth-sustem
```
cd /auth-system
```
Configure the database to any of your choise in the 'settings.py' file

3. Migrate into your new database
```
python3 manage.py makemigrations
python3 manage.py migrate
```

4. Set us a superuser account
```
python3 manage.py createsuperuser
```
Privode the neccesary credentials

5. Run the server
```
python3 manage.py runserver
```

!!! Enjoy
