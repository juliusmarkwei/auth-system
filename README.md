# User Authentication System

## Overview

This project implements a robust User Authentication System, designed to manage user registrations and logins efficiently and securely. It uses Django framework for backend operations, emphasizing security and ease of use.

## Features

- **User Model Customization**: Custom user model defined in `models.py`.
- **Create User Views**: A view to create a user profile in `views.py`
- **Update User Views**: A view to update the user profile in `views.py`
- **Authentication Views**: Includes views for user registration, login, and other authentication-related operations in `views.py`.
- **URL Routing**: Defined URL patterns for authentication endpoints in `urls.py`.
- **Data Serialization**: Utilizes serializers for data handling in `serializers.py`.

## Technologies

- Python 3.10.12
- Django: A high-level Python Web framework.
- Django REST framework: A powerful toolkit for building Web APIs.
- CoreAPI: A format-independent Document Object Model for representing Web APIs

## Installation and Setup

1. Clone the repository.
2. Install dependencies: `pip install -r requirements-dev.txt`.
3. Run migrations: `python manage.py migrate`.
4. Start the Django server: `python manage.py runserver`.

## Usage

- User registration and login endpoints are accessible through the defined URL patterns.
- Utilize the custom user model for extended user management features.
- A custome documentation build witth CoreAPI can also be accessed through `localhost:#port/docs/`

## Contribution

Contributions to enhance or improve this project are welcome. Please fork the repository and open a pull request with your changes.

## License

This project is open-sourced under the <a href="https://github.com/juliusmarkwei/auth-system/blob/main/LICENSE.md">MIT</a> License.

---

Thank you for exploring the User Authentication System project!
