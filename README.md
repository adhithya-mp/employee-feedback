Employee Feedback Management System

This is a Django REST API project for managing employee feedbacks in an organization. It includes secure authentication using JWT, feedback submission features, and feedback viewing functionality.

## Features

- JWT Authentication (Registration and Login)
- Role-based employee model with designations
- Feedback question types (text/rating)
- Feedback submission with multiple answers
- View feedback submitted by employees

##  Tech Stack

- Python 3.10
- Django 5.x
- Django REST Framework
- djangorestframework-simplejwt
- SQLite (default)
- 
## Installation & Setup

1. Clone the repository

git clone https://github.com/your-username/employee-feedback.git
cd employee-feedback


2. Create and activate a virtual environment

python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate


3. Install dependencies

pip install -r requirements.txt


4. Apply migrations

python manage.py makemigrations
python manage.py migrate


5. Create a superuser 

python manage.py createsuperuser

## API Endpoints

Authentication

Register

POST /api/register/

{
  "username": "johndoe",
  "password": "yourpassword"
}

Login (JWT Token)

POST /api/token/

{
  "username": "adhithya",
  "password": "pass"
}

 Refresh Token

POST /api/token/refresh/

{
  "refresh": "refreshtoken"
}


👨‍💼 Employees

 List Employees

GET /api/employees/
Feedback Questions

 List Feedback Questions by Type

GET /api/question/?type=rating
or
GET /api/question/?type=text

 Submit Feedback

POST /api/submit/
Headers:
Authorization: Bearer <token>
Body:

{
  "feedback_answers": [
    {
      "question": 1,
    "text_answer": "Great work environment",
      "rating_answer": null
    },
    {
      "question": 2,
      "text_answer": null,
      "rating_answer": 4
    }
  ]
}


 View Feedback

View Feedback for an Employee

GET /api/feedback/<employee_id>/
Headers:
Authorization: Bearer <token>

