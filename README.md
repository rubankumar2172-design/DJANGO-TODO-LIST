# To-Do List Website (Django)

A web application where users can register, log in, and manage their own tasks.

**Live demo:** https://django-todo-list-pnuf.onrender.com/
**Note:** the free hosting may take about a minute to wake up on the first visit.

## Features
- User registration, login, and logout
- Each user can see and manage only their own tasks
- Add, edit, complete, and delete tasks
- Authentication and authorization (access control)
- Tests with Django's test framework (12 tests)

## Tech Stack
- Python, Django
- MySQL (database)
- HTML, CSS (frontend)
- Git, GitHub (version control)
- Render (hosting)

## Try It
Click **Register** to create a free test account. Use a fake email and a throwaway password. Do not reuse a real password.

## Run Locally
1. Clone the project:
```
   git clone https://github.com/rubankumar2172-design/DJANGO-TODO-LIST.git
   cd To_Do_List
```
2. Create and activate a virtual environment:
```
   python -m venv venv
   venv\Scripts\activate
```
3. Install the packages:
```
   python -m pip install -r requirements.txt
```
4. Create a `.env` file in the project folder:
```
   SECRET_KEY=your-secret-key
   DEBUG=True
   DB_NAME=your-database-name
   DB_USER=your-database-user
   DB_PASSWORD=your-database-password
   DB_HOST=localhost
```
5. Create the database tables and start the server:
```
   python manage.py migrate
   python manage.py runserver
```
6. Run the tests:
```
   python manage.py test
```

## Security
- Secrets are stored in environment variables, not in the code
- HTTPS redirect and secure cookies are enabled in production
- `DEBUG` is off in production

## Author
Ruban Kumar | https://www.linkedin.com/in/ruban-kumar-dev/