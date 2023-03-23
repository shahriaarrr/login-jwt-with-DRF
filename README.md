# Django User Registration and Authentication API

This project is a simple Django REST API for user registration and authentication. It provides two endpoints:

1.  `/api/register`: This endpoint accepts a `POST` request with the user's username, password, first name, and last name. If the data is valid, a new user will be created and a response will be returned with the user's data and a success message.
2.  `/api/login`: This endpoint accepts a `POST` request with the user's username and password. If the data is valid, a response will be returned with the user's username, first name, last name, staff status, and a token for authentication.

## Installation

1.  Clone the repository:

`git clone https://github.com/example/django-authentication-api.git`

2.  Create a virtual environment and activate it:

`python -m venv env
source env/bin/activate`

3.  Install the dependencies:

`pip install -r requirements.txt`

4.  Run migrations:

`python manage.py migrate`

5.  Start the development server:

`python manage.py runserver`

## Endpoints

### Register

`POST /api/register`

Create a new user account.

#### Request

##### Parameters

- `username` (string): The username of the user. Required.
- `password` (string): The password of the user. Required.
- `first_name` (string): The first name of the user. Required.
- `last_name` (string): The last name of the user. Required.

##### Example

`curl --location --request POST 'http://localhost:8000/api/register' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "exampleuser",
    "password": "examplepassword",
    "first_name": "Example",
    "last_name": "User"
}'`

#### Response

##### Success

If the user is created successfully, a response with a status code of `201 Created` will be returned.

`{
    "user": {
        "id": 1,
        "username": "exampleuser",
        "first_name": "Example",
        "last_name": "User"
    },
    "message": "User Created Successfully.  Now perform Login to get your token"
}`

##### Error

If the request is invalid or the user already exists, a response with a status code of `400 Bad Request` will be returned.

`{
    "username": [
        "A user with that username already exists."
    ]
}`

### Login

`POST /api/login`

Authenticate a user and return a token.

#### Request

##### Parameters

- `username` (string): The username of the user. Required.
- `password` (string): The password of the user. Required.

##### Example

`curl --location --request POST 'http://localhost:8000/api/login' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "exampleuser",
    "password": "examplepassword"
}'`

#### Response

##### Success

If the user is authenticated successfully, a response with a status code of `200 OK` will be returned.

`{  "username":  "myusername",
  "first_name":  "John",
  "last_name":  "Doe",
  "is_staff":  false,
  "access":  "<access-token>",
  "refresh":  "<refresh-token>"  
 }
`

### Code Structure

#### urls.py

The `urls.py` file defines the URL patterns for the API endpoints using Django's `path()` function. The `RegisterApi` and `LoginApi` views are imported from the `api.py` module.

#### views.py

The `views.py` module defines the views for the API endpoints. The `RegisterApi` view handles user registration by accepting a POST request with user data and creating a new user in the system. The `LoginApi` view handles user authentication by accepting a POST request with a username and password, checking the credentials against the database, and returning access and refresh tokens if the credentials are valid. Both views inherit from Django's `generics.GenericAPIView` class and use custom serializers to validate input and output data.

#### serializers.py

The `serializers.py` module defines the custom serializers used by the views to validate input and output data. The `RegisterSerializer` is used to validate user registration data and create new users in the system. The `UserSerializer` is used to serialize user objects for output. The `LoginSerializer` is used to validate user credentials for authentication.

#### utils.py

The `utils.py` module provides a utility function `get_tokens_for_user(user)` that generates access and refresh tokens for a given user using Django REST Framework SimpleJWT library.

### Dependencies

This Django project depends on the following Python packages:

- Django (v3.0 or higher)
- djangorestframework (v3.11 or higher)
- djangorestframework-simplejwt (v4.6 or higher)
